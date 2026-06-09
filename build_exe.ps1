$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$venv = Join-Path $root ".venv"
$python = Join-Path $venv "Scripts\python.exe"
$spec = Join-Path $root "StudocuHack.spec"
$output = Join-Path $root "dist\StudocuHack.exe"

if (-not (Test-Path -LiteralPath $python)) {
    Write-Host "Creating build virtual environment..." -ForegroundColor Cyan
    & py -3.11 -m venv $venv
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to create the build virtual environment. Install Python 3.11 first."
    }

    Write-Host "Installing build dependencies..." -ForegroundColor Cyan
    & $python -m pip install -r (Join-Path $root "requirements.txt")
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to install build dependencies."
    }
}

if (-not (Test-Path -LiteralPath $spec)) {
    throw "PyInstaller spec file was not found: $spec"
}

Push-Location $root
try {
    Write-Host "Checking build dependencies..." -ForegroundColor Cyan
    & $python -c "import PyQt5, playwright, PyInstaller"
    if ($LASTEXITCODE -ne 0) {
        throw "Build dependencies are missing. Run: & '$python' -m pip install -r requirements.txt"
    }

    Write-Host "Building StudocuHack.exe. This may take a few minutes..." -ForegroundColor Cyan
    & $python -m PyInstaller --noconfirm --clean $spec
    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller build failed."
    }

    if (-not (Test-Path -LiteralPath $output)) {
        throw "Build finished, but the output file was not found: $output"
    }

    $sizeMb = [math]::Round((Get-Item -LiteralPath $output).Length / 1MB, 1)
    Write-Host ""
    Write-Host "Build completed: $output" -ForegroundColor Green
    Write-Host "File size: $sizeMb MB" -ForegroundColor Green
} finally {
    Pop-Location
}
