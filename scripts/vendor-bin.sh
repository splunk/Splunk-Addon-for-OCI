#!/usr/bin/env bash
#
# vendor-bin.sh — Surgically upgrade ONLY the Python-version-sensitive binaries in
# Splunk-Addon-for-OCI/bin/ so the add-on runs on a newer CPython, on Linux x86_64 +
# Windows x86_64. The hand-trimmed pure-Python trees committed in bin/ (oci, certifi,
# the cryptography sources, ...) are intentionally LEFT UNTOUCHED.
#
# Runs from ANY host with pip >= 22 — it never builds extensions, it only downloads the
# matching wheels and copies the compiled files out — so a target-version interpreter is
# not required.
#
# It (re)places exactly three version-sensitive things:
#   1. cffi's _cffi_backend extension      -> cp<VER> for linux (.so) + windows (.pyd)
#   2. cryptography's Windows bindings      -> adds _openssl.pyd / _rust.pyd
#      (the committed linux _*.abi3.so is stable-ABI and already runs on all 3.x — kept)
#   3. multiprocess                         -> the version-tagged py<VER> package
#
# SCOPE: designed for the Python 3.9 (v3.1.0) branch, where the bundled cffi/cryptography
# *versions* are unchanged and only their ABI must move off cp37. The Python 3.13 (v3.2.0)
# branch additionally BUMPS oci/cryptography/cffi and drops multiprocess for stdlib
# multiprocessing — that is a version refresh, not an in-place binary swap; see
# requirements-py313.txt and the plan.
#
# GIT NOTE: .gitignore ignores *.so. The existing tracked .so were force-added, so do the
# same for the new linux extension after running this:
#     git add -f bin/_cffi_backend.cpython-*-x86_64-linux-gnu.so
# The Windows .pyd files are not ignored and stage normally.
#
# Usage: scripts/vendor-bin.sh [PY_VERSION]      # default 39
#
set -euo pipefail
PY_VERSION="${1:-39}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BIN="$ROOT/bin"
REQ="$ROOT/requirements-py${PY_VERSION}.txt"
PIP=(python -m pip)

[ -f "$REQ" ] || { echo "ERROR: missing $REQ" >&2; exit 1; }
[ -d "$BIN/cryptography/hazmat/bindings" ] || { echo "ERROR: $BIN is not a vendored tree" >&2; exit 1; }

# Pinned "name==ver" from the requirements file (inline comments stripped).
spec() { grep -iE "^$1==" "$REQ" | head -1 | sed -E 's/[[:space:]]*#.*$//' | tr -d '[:space:]'; }

extract() { python -c "import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])" "$1" "$2"; }

WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
echo ">> Surgical binary upgrade of bin/ for Python 3.${PY_VERSION#3}  ($REQ)"

# 1. cffi _cffi_backend — drop any existing, copy in cp<VER> for both platforms.
rm -f "$BIN"/_cffi_backend.cpython-*-x86_64-linux-gnu.so "$BIN"/_cffi_backend.cp*-win_amd64.pyd
for PLAT in manylinux2014_x86_64 win_amd64; do
  d="$WORK/cffi-$PLAT"; mkdir -p "$d/x"
  "${PIP[@]}" download --no-deps --only-binary=:all: --implementation cp \
    --python-version "$PY_VERSION" --abi "cp${PY_VERSION}" --platform "$PLAT" -d "$d" "$(spec cffi)"
  extract "$d"/*.whl "$d/x"
  cp "$d"/x/_cffi_backend.* "$BIN"/
done

# 2. cryptography — add the Windows bindings (.pyd); keep the committed linux .abi3.so.
d="$WORK/crypto-win"; mkdir -p "$d/x"
"${PIP[@]}" download --no-deps --only-binary=:all: --implementation cp \
  --python-version "$PY_VERSION" --abi abi3 --platform win_amd64 -d "$d" "$(spec cryptography)"
extract "$d"/*.whl "$d/x"
cp "$d"/x/cryptography/hazmat/bindings/*.pyd "$BIN"/cryptography/hazmat/bindings/

# 3. multiprocess — replace with the py<VER> build (different content per version).
rm -rf "$BIN"/multiprocess "$BIN"/_multiprocess "$BIN"/multiprocess-*.dist-info
"${PIP[@]}" install --target "$BIN" --no-deps --upgrade \
  --only-binary=:all: --python-version "$PY_VERSION" "$(spec multiprocess)"

# Report + assert nothing version-stale survived.
echo ">> compiled binaries now in bin/:"
find "$BIN" \( -name '_cffi_backend*' -o -name '_rust.*' -o -name '_openssl.*' \) \
  \( -name '*.so' -o -name '*.pyd' \) -print | sort
STALE="$(find "$BIN" -regextype posix-extended -regex '.*(cp37|cpython-37m|semaphore_tracker).*' || true)"
if [ -n "$STALE" ]; then echo ">> ERROR: stale artifacts remain:" >&2; echo "$STALE" >&2; exit 1; fi
echo ">> OK: no cp37 / py37-multiprocess artifacts remain. Done."
