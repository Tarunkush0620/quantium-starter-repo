# PowerShell test runner for Windows
# Mirrors run_tests.sh to run pytest inside venv
$ErrorActionPreference = "Stop"

Write-Host "Activating virtual environment..."

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPython = Join-Path $repoRoot "venv\Scripts\python.exe"

if (-not (Test-Path $venvPython)) {
    Write-Error "Virtual environment Python not found at $venvPython"
    exit 1
}

Write-Host "Running test suite..."
# Prefer headless to avoid browser popups during Selenium tests
& $venvPython -m pytest -q --headless

if ($LASTEXITCODE -eq 0) {
    Write-Host "All tests passed!"
    exit 0
} else {
    Write-Error "Tests failed!"
    exit 1
}
