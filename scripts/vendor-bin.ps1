<#
.SYNOPSIS
  Surgically upgrade ONLY the Python-version-sensitive binaries in
  Splunk-Addon-for-OCI\bin\ so the add-on runs on a newer CPython, on Linux x86_64 +
  Windows x86_64. PowerShell mirror of scripts/vendor-bin.sh.

.DESCRIPTION
  The hand-trimmed pure-Python trees committed in bin\ (oci, certifi, the cryptography
  sources, ...) are intentionally LEFT UNTOUCHED. Runs from ANY host with pip >= 22 (it
  never builds extensions, only downloads matching wheels and copies the compiled files).

  (Re)places exactly three version-sensitive things:
    1. cffi's _cffi_backend extension     -> cp<VER> for linux (.so) + windows (.pyd)
    2. cryptography's Windows bindings     -> adds _openssl.pyd / _rust.pyd
       (committed linux _*.abi3.so is stable-ABI, runs on all 3.x -> kept)
    3. multiprocess                        -> the version-tagged py<VER> package

  SCOPE: the Python 3.9 (v3.1.0) branch. The Python 3.13 (v3.2.0) branch bumps
  oci/cryptography/cffi and drops multiprocess for stdlib multiprocessing (see
  requirements-py313.txt / the plan) — that is a version refresh, not this in-place swap.

  GIT NOTE: .gitignore ignores *.so; existing tracked .so were force-added, so after
  running:  git add -f bin/_cffi_backend.cpython-*-x86_64-linux-gnu.so
  Windows .pyd files are not ignored and stage normally.

.EXAMPLE
  scripts\vendor-bin.ps1                 # Python 3.9
.EXAMPLE
  scripts\vendor-bin.ps1 -PyVersion 39
#>
param([string]$PyVersion = "39")

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptDir
$Bin  = Join-Path $Root "bin"
$Req  = Join-Path $Root "requirements-py$PyVersion.txt"

if (-not (Test-Path $Req)) { throw "ERROR: missing $Req" }
if (-not (Test-Path (Join-Path $Bin "cryptography\hazmat\bindings"))) { throw "ERROR: $Bin is not a vendored tree" }

$reqLines = Get-Content $Req
function Spec([string]$name) {
  $line = $reqLines | Where-Object { $_ -match "^(?i)$([regex]::Escape($name))==" } | Select-Object -First 1
  if (-not $line) { throw "ERROR: $name not pinned in $Req" }
  return ((($line -split '#')[0]) -replace '\s', '')
}
function Extract([string]$whl, [string]$dest) {
  & python -c "import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])" $whl $dest
}

$Work = New-Item -ItemType Directory -Path (Join-Path $env:TEMP ("vendor-" + [guid]::NewGuid()))
try {
  Write-Host ">> Surgical binary upgrade of bin/ for Python 3.$($PyVersion.Substring(1))  ($Req)"

  # 1. cffi _cffi_backend — drop existing, copy in cp<VER> for both platforms.
  Get-ChildItem -Path $Bin -Filter "_cffi_backend.cpython-*-x86_64-linux-gnu.so" -Force -ErrorAction SilentlyContinue | Remove-Item -Force
  Get-ChildItem -Path $Bin -Filter "_cffi_backend.cp*-win_amd64.pyd" -Force -ErrorAction SilentlyContinue | Remove-Item -Force
  foreach ($plat in @("manylinux2014_x86_64", "win_amd64")) {
    $d = New-Item -ItemType Directory -Path (Join-Path $Work.FullName "cffi-$plat")
    $x = New-Item -ItemType Directory -Path (Join-Path $d.FullName "x")
    & python -m pip download --no-deps --only-binary=:all: --implementation cp `
      --python-version $PyVersion --abi "cp$PyVersion" --platform $plat -d $d.FullName (Spec "cffi")
    Extract ((Get-ChildItem $d.FullName -Filter *.whl)[0].FullName) $x.FullName
    Get-ChildItem -Path $x.FullName -Filter "_cffi_backend.*" | Copy-Item -Destination $Bin -Force
  }

  # 2. cryptography — add the Windows bindings (.pyd); keep committed linux .abi3.so.
  $d = New-Item -ItemType Directory -Path (Join-Path $Work.FullName "crypto-win")
  $x = New-Item -ItemType Directory -Path (Join-Path $d.FullName "x")
  & python -m pip download --no-deps --only-binary=:all: --implementation cp `
    --python-version $PyVersion --abi abi3 --platform win_amd64 -d $d.FullName (Spec "cryptography")
  Extract ((Get-ChildItem $d.FullName -Filter *.whl)[0].FullName) $x.FullName
  Get-ChildItem -Path (Join-Path $x.FullName "cryptography\hazmat\bindings") -Filter "*.pyd" |
    Copy-Item -Destination (Join-Path $Bin "cryptography\hazmat\bindings") -Force

  # 3. multiprocess — replace with the py<VER> build.
  foreach ($p in @("multiprocess", "_multiprocess")) {
    $t = Join-Path $Bin $p; if (Test-Path $t) { Remove-Item -Recurse -Force $t }
  }
  Get-ChildItem -Path $Bin -Filter "multiprocess-*.dist-info" -Force -ErrorAction SilentlyContinue |
    ForEach-Object { Remove-Item -Recurse -Force $_.FullName }
  & python -m pip install --target $Bin --no-deps --upgrade `
    --only-binary=:all: --python-version $PyVersion (Spec "multiprocess")

  Write-Host ">> compiled binaries now in bin/:"
  Get-ChildItem -Path $Bin -Recurse -Force -Include "_cffi_backend*.so","_cffi_backend*.pyd","_rust.*so","_rust.pyd","_openssl.*so","_openssl.pyd" |
    ForEach-Object { Write-Host "   $($_.FullName)" }
  $stale = Get-ChildItem -Path $Bin -Recurse -Force | Where-Object { $_.Name -match "cp37|cpython-37m|semaphore_tracker" }
  if ($stale) { $stale | ForEach-Object { Write-Error "stale: $($_.FullName)" }; throw "ERROR: stale artifacts remain" }
  Write-Host ">> OK: no cp37 / py37-multiprocess artifacts remain. Done."
} finally {
  Remove-Item -Recurse -Force $Work.FullName
}
