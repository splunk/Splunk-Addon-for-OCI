#!/usr/bin/env bash
# package-addon.sh — build TA-oci-logging-addon.tar.gz using the Splunk Packaging
# Toolkit (slim). Must run inside the builder container where slim is installed.
#
# Usage: docker compose exec builder bash /addon/scripts/package-addon.sh
# Output: /dist/TA-oci-logging-addon-<version>.tar.gz
#
# slim requires the source directory name to match [package]/id in app.conf,
# so the source is copied to /tmp/TA-oci-logging-addon before packaging.
set -euo pipefail

ADDON_SRC=/addon
DIST_DIR=/dist
APP_ID=TA-oci-logging-addon
STAGING="/tmp/${APP_ID}"

# Ensure slim is available
if ! command -v slim &>/dev/null; then
  echo ">> Installing splunk-packaging-toolkit..."
  pip install splunk-packaging-toolkit -q
fi

echo ">> slim $(slim --version 2>&1 | head -1)"

# Clean staging copy using Python shutil — handles deep bin/oci/ paths reliably
# (plain 'cp -r' fails on deeply nested paths like bin/oci/certificates_management/models/)
# Use bash rm -rf first so the overlay filesystem releases the directory cleanly,
# then Python shutil.copytree does the actual copy.
rm -rf "$STAGING"
echo ">> Copying source to $STAGING ..."
python3 - <<'PYEOF'
import sys, os, shutil

src = '/addon'
dst = '/tmp/TA-oci-logging-addon'

def _ignore(directory, contents):
    ignored = set()
    # top-level exclusions
    if directory == src:
        ignored.update({'.git', 'scripts', 'app.manifest'})
    for name in contents:
        if name.endswith('.pyc'):
            ignored.add(name)
        if name.startswith('requirements') and name.endswith('.txt'):
            ignored.add(name)
    return ignored

# Belt-and-braces: rmtree with ignore_errors in case bash rm -rf didn't finish
if os.path.exists(dst):
    shutil.rmtree(dst, ignore_errors=True)
shutil.copytree(src, dst, ignore=_ignore, symlinks=False)

# Remove pycache dirs and egg-info after copy
for root, dirs, files in os.walk(dst, topdown=False):
    for d in dirs:
        if d in ('__pycache__',) or d.endswith('.egg-info'):
            shutil.rmtree(os.path.join(root, d))

print(f'  Staging: {dst}')
PYEOF

echo ">> Staging copy: $STAGING"

mkdir -p "$DIST_DIR"

# Run slim package — writes app.manifest into staging dir, outputs .tar.gz to /dist
echo ">> Running slim package..."
slim package "$STAGING" --output-dir "$DIST_DIR" 2>&1

# Show result
PKG=$(ls -t "$DIST_DIR/${APP_ID}"*.tar.gz 2>/dev/null | head -1)
if [ -z "$PKG" ]; then
  echo "ERROR: no package found in $DIST_DIR" >&2; exit 1
fi

SIZE=$(du -sh "$PKG" | cut -f1)
echo ">> Package: $PKG  (${SIZE})"
echo ">> Contents (top-level):"
tar -tzf "$PKG" | grep -E "^${APP_ID}/[^/]+/?$" | sort

# Clean up staging dir
rm -rf "$STAGING"
