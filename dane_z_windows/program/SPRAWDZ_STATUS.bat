@echo off
echo ========================================
echo STATUS ANALIZY PI - 10B DIGITS
echo ========================================
echo Czas sprawdzenia: %DATE% %TIME%
echo.

cd C:\Users\test\Analiza_10B

echo [1] PROCES PYTHON:
echo ----------------------------------------
powershell -Command "Get-Process python -ErrorAction SilentlyContinue | Format-Table Id,@{N='CPU_min';E={[math]::Round($_.CPU/60,1)}},@{N='RAM_GB';E={[math]::Round($_.WS/1GB,2)}},StartTime -AutoSize"
if %errorlevel% neq 0 (
    echo [BRAK] Python nie dziala - testy zakonczone lub zatrzymane
)
echo.

echo [2] ZAKONCZONE TESTY:
echo ----------------------------------------
powershell -Command "$files = ls *_results.json -ErrorAction SilentlyContinue; if ($files) { $files | ForEach-Object { $json = Get-Content $_.FullName | ConvertFrom-Json; Write-Host \"[OK] Test $($json.step_id): $($json.test_name) - $(if($json.status -eq 'completed'){'GOTOWE'}else{$json.status})\" } } else { Write-Host '[BRAK] Zadnych zakoczonych testow' }"
echo.

echo [3] OSTATNIE 10 LINII LOGU:
echo ----------------------------------------
if exist testy_13-27_live.log (
    powershell -Command "Get-Content testy_13-27_live.log -Tail 10"
) else if exist full_27_live.log (
    powershell -Command "Get-Content full_27_live.log -Tail 10"
) else (
    echo [BRAK] Brak pliku logu
)
echo.

echo [4] PODSUMOWANIE:
echo ----------------------------------------
powershell -Command "$completed = (ls *_results.json -ErrorAction SilentlyContinue).Count; $total = 27; Write-Host \"Zakonczone: $completed / $total testow ($([math]::Round(100*$completed/$total,1))%%)\";"
echo.

echo ========================================
pause

