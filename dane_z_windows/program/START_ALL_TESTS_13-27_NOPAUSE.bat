@echo off
echo ========================================
echo URUCHAMIANIE TESTOW 13-27 (10B digits)
echo ========================================
echo Start: %DATE% %TIME%
echo Log: C:\Users\test\Analiza_10B\testy_13-27_live.log
echo.
echo Mozesz zamknac to okno - testy ida w tle!
echo.

cd C:\Users\test\OMNIS2

REM Testy 13-27 po kolei z force
python analysis_orchestrator.py --pi-file C:\Users\test\pi_10billion.txt --output-dir C:\Users\test\Analiza_10B --max-digits 10000000000 --steps 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 --force > C:\Users\test\Analiza_10B\testy_13-27_live.log 2>&1

echo ======================================== >> C:\Users\test\Analiza_10B\testy_13-27_live.log
echo WSZYSTKIE TESTY 13-27 ZAKONCZONE >> C:\Users\test\Analiza_10B\testy_13-27_live.log
echo Koniec: %DATE% %TIME% >> C:\Users\test\Analiza_10B\testy_13-27_live.log
echo ======================================== >> C:\Users\test\Analiza_10B\testy_13-27_live.log

