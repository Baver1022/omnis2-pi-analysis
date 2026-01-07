@echo off
echo ========================================
echo URUCHAMIANIE TESTOW 13-27 (10B digits)
echo ========================================
echo Start: %DATE% %TIME%
echo.

cd C:\Users\test\OMNIS2

REM Testy 13-27 po kolei z force
python analysis_orchestrator.py --pi-file C:\Users\test\pi_10billion.txt --output-dir C:\Users\test\Analiza_10B --max-digits 10000000000 --steps 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 --force > C:\Users\test\Analiza_10B\testy_13-27_live.log 2>&1

echo.
echo ========================================
echo WSZYSTKIE TESTY 13-27 ZAKONCZONE
echo ========================================
echo Koniec: %DATE% %TIME%
echo Log: C:\Users\test\Analiza_10B\testy_13-27_live.log
echo.
type C:\Users\test\Analiza_10B\testy_13-27_live.log
echo.
pause
