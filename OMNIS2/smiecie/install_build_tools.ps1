# PowerShell Script: Instalacja Microsoft C++ Build Tools i CuPy
# Uruchom jako Administrator: Right-click → Run as Administrator

Write-Host "=== INSTALACJA MICROSOFT C++ BUILD TOOLS ===" -ForegroundColor Green

# Sprawdź czy winget jest dostępny
if (Get-Command winget -ErrorAction SilentlyContinue) {
    Write-Host "✅ winget dostępny" -ForegroundColor Green
    
    # Instalacja Build Tools
    Write-Host "Instalowanie Visual Studio Build Tools..." -ForegroundColor Yellow
    winget install Microsoft.VisualStudio.2022.BuildTools `
        --silent `
        --accept-package-agreements `
        --accept-source-agreements `
        --override "--quiet --wait --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
    
    Write-Host "✅ Build Tools zainstalowane" -ForegroundColor Green
} else {
    Write-Host "❌ winget nie dostępny" -ForegroundColor Red
    Write-Host "Pobierz ręcznie: https://visualstudio.microsoft.com/visual-cpp-build-tools/" -ForegroundColor Yellow
    exit 1
}

# Czekaj na zakończenie instalacji
Write-Host "Czekanie na zakończenie instalacji (może zająć 30-60 minut)..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Sprawdź czy kompilator jest dostępny
Write-Host "Sprawdzanie kompilatora..." -ForegroundColor Yellow
$clPath = Get-Command cl -ErrorAction SilentlyContinue
if ($clPath) {
    Write-Host "✅ Kompilator C++ dostępny: $($clPath.Path)" -ForegroundColor Green
} else {
    Write-Host "⚠️ Kompilator nie znaleziony - może wymagać restartu lub ręcznej konfiguracji" -ForegroundColor Yellow
}

# Instalacja CuPy
Write-Host "`n=== INSTALACJA CUPY ===" -ForegroundColor Green
Write-Host "Instalowanie CuPy..." -ForegroundColor Yellow

# Sprawdź wersję CUDA
$cudaVersion = (nvidia-smi --query-gpu=driver_version --format=csv,noheader,nounits | Select-Object -First 1)
Write-Host "CUDA Driver: $cudaVersion" -ForegroundColor Cyan

# Zainstaluj CuPy (spróbuj różne wersje)
$cupyVersions = @("cupy-cuda12x", "cupy-cuda11x", "cupy")
$installed = $false

foreach ($version in $cupyVersions) {
    Write-Host "Próba instalacji: $version" -ForegroundColor Yellow
    $result = py -m pip install $version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ CuPy zainstalowany: $version" -ForegroundColor Green
        $installed = $true
        break
    } else {
        Write-Host "❌ Nie udało się zainstalować: $version" -ForegroundColor Red
    }
}

if ($installed) {
    Write-Host "`n=== SPRAWDZENIE CUPY ===" -ForegroundColor Green
    py -c "import cupy as cp; print('CuPy:', cp.__version__); print('GPU:', cp.cuda.Device(0).compute_capability)"
    Write-Host "`n✅ INSTALACJA ZAKOŃCZONA!" -ForegroundColor Green
} else {
    Write-Host "`n❌ Nie udało się zainstalować CuPy" -ForegroundColor Red
    Write-Host "Możliwe przyczyny:" -ForegroundColor Yellow
    Write-Host "  1. Build Tools nie zostały poprawnie zainstalowane" -ForegroundColor Yellow
    Write-Host "  2. Wymagany restart systemu" -ForegroundColor Yellow
    Write-Host "  3. Spróbuj użyć Conda zamiast pip" -ForegroundColor Yellow
}

