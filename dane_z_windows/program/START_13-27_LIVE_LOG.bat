@echo off
title ANALIZA PI - TESTY 13-27 (10B) - LIVE + LOG
color 0A
echo ========================================
echo ANALIZA PI - TESTY 13-27 (LIVE + LOG)
echo ========================================
echo Start: %DATE% %TIME%
echo.
echo [LIVE] Widok na zywo w tym oknie
echo [LOG]  Zapis: C:\Users\test\Analiza_10B\testy_13-27.log
echo.
echo Zostaw to okno otwarte!
echo.
echo ========================================
echo.

cd C:\Users\test\OMNIS2

REM Uruchom z zapisem do logu (PowerShell obsługuje tee)
powershell -Command "python analysis_orchestrator.py --pi-file C:\Users\test\pi_10billion.txt --output-dir C:\Users\test\Analiza_10B --max-digits 10000000000 --steps 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 --force 2>&1 | Tee-Object -FilePath C:\Users\test\Analiza_10B\testy_13-27.log"

echo.
echo ========================================
echo WSZYSTKIE TESTY 13-27 ZAKONCZONE!
echo ========================================
echo Koniec: %DATE% %TIME%
echo Log zapisany: C:\Users\test\Analiza_10B\testy_13-27.log
echo.
pause

