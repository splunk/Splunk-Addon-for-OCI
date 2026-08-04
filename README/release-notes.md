# OCI Logging Add-On 
## Release 3.2.0
- Upgraded Python dependencies to resolve security vulnerabilities: `cryptography` to `48.0.1`, `pyopenssl` to `26.0.0`, and `certifi` to `2024.7.4` (0 vulnerabilities reported by `grype` scan).
- Added multi-platform binary support for `cryptography` by bundling both Linux `_rust.abi3.so` and Windows `_rust.pyd` extensions.
- Resolved Python 3.12+ (Splunk 10.x+) compatibility issues by introducing `SplunklibSixRedirectFinder` inside `oci_logging.py` to dynamically intercept and redirect legacy `splunklib.six.moves` imports.
- Moved all vendored third-party libraries from `bin/` into `bin/lib/` to stop generically-named packages (`OpenSSL`, `cryptography`, `six`, `certifi`, `oci`, etc.) from shadowing, or being shadowed by, other Splunk apps' same-named vendored copies when Splunk reuses a shared Python worker process across apps.
- Removed the stale `bin/linux_x86_64/bin/oci_logging.py` duplicate (2021-era, inert — outside the path Splunk actually resolves platform-specific scripts from).
- Completed `README/inputs.conf.spec` to also declare the bare `[oci_logging]` stanza (matching the scheme-default values in `default/inputs.conf`), clearing "Invalid key in stanza [oci_logging]" warnings at Splunk startup.
- Removed unreachable dead code in `stream_events()`'s multiprocessing result handling (`isinstance(results, str)`/`isinstance(results, int)` branches could never match, since `results` is always a list of `AsyncResult` objects).
- Added a GitHub Actions CI matrix (`tests/test_bin_lib_imports.py`, Python 3.9/3.13 on Windows and Linux — the exact CPython tags `cffi`'s `_cffi_backend` is vendored for) exercising the vendored `bin/lib` import chain on clean runners. This is what caught two real gaps that manual verification had missed, both masked by ambient packages already present on the machines used to verify by hand (this dev machine and the Splunk Docker container): `cffi`/`_cffi_backend` actually being required by the vendored `cryptography` build (a same-day attempt to remove it as "unused" got reverted once CI caught it), and `typing_extensions` (needed by `pyOpenSSL` 26.0.0's `OpenSSL/crypto.py` for Python 3.8-3.12) never having been vendored at all.
- Confirmed and documented that Python 3.7 is **not** supported: `cryptography` 48.0.1's vendored wheel is built `cp39-abi3` (checked the actual `WHEEL` metadata, not just classifiers) and hard-fails to load under 3.7 (`DLL load failed`) — an ABI floor, not a missing file. The now-unusable cp37 `_cffi_backend` binary was removed accordingly.

## Release 3.1.0
- Added Python 3.9 compatibility support for Splunk Enterprise 9.x+ (Linux and Windows x86_64).
- Bundled Python 3.9 compiled libraries for both Linux (`bin/_cffi_backend.cpython-39-x86_64-linux-gnu.so`) and Windows (`bin/_cffi_backend.cp39-win_amd64.pyd`).
- Scoped the `python.version = python3.9` configuration strictly under the `[oci_logging]` modular input stanza in `default/inputs.conf`.
- Removed global `default/server.conf` configuration to prevent settings pollution and dependency conflicts with other Splunk add-ons (Sophos, AWS, GCP, MSCS).

## Release 3.0.0
- Validating OCI Streaming endpoint URL for HTTPS 
- Added support for pasting in OCI API Key.  This can be an RSA key or an OCI Console Key for a LOCAL OCI IAM user.
- Depreciated OCI API key upload feature

## Release 2.3.2
- Added retry logic for 50x responses from OCI Streaming
- Moved README.txt for Splunkbase AppInspect 
- Update OCI SDK to 2.99.0
## Release 2.3.0
- Native integration for Cloud Guard problems written to OCI Streams via OCI Events.
    - This allows any OCI Event written to the OCI Stream to be written into Splunk
- Improved Error handling for 401 and 404 errors
- Updated Splunk Lib
- Updated OCI SDK to 2.90.3
- Updated app file permissions
- Added a README.txt with binary documentation

## Release 2.2.2
- Updated OCI SDK to 2.88.1

## Release 2.2.1
- Local File System Key is the default
- Support for upload of OCI API Key file is moved to `More settings`
- Updated OCI Python SDK to 2.54.0
- Updated [README.md](README.md) with prerequisites and troubleshooting

## Release 2.2.0
- Added help text to inputs screen
- Restored Support for uploading an RSA OCI API Key 
- Support for local file system key file is moved to `More settings`
    - Local File System Key is required for Splunk Version 8.0
- Added logger.info message for unsupported data in the stream
- Added logger.info for when data is not returned.  This is track the plugin is running without using DEBUG
- PEP8 clean up

## Release 2.1.1
- Added release notes
- Converted to an OCI API key stored on the Heavy Forwarder instead of uploaded via the Web UI
- Support for OCI API Keys generated from the console
- Updated OCI Python SDK to 2.45.1
- Removed __pycache__ and other clean up
- Renamed input variable *Worker Processes* to *Number of partitions*