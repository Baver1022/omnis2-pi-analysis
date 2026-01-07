@echo off
echo ========================================
echo URUCHAMIANIE WSZYSTKICH 27 TESTOW (10B)
echo ========================================
echo Start: %DATE% %TIME%
echo Log: C:\Users\test\Analiza_10B\full_27_live.log
echo.
echo Mozesz zamknac to okno - testy ida w tle!
echo.

cd C:\Users\test\OMNIS2

REM Wszystkie 27 testow z force
python analysis_orchestrator.py --pi-file C:\Users\test\pi_10billion.txt --output-dir C:\Users\test\Analiza_10B --max-digits 10000000000 --force > C:\Users\test\Analiza_10B\full_27_live.log 2>&1

echo ======================================== >> C:\Users\test\Analiza_10B\full_27_live.log
echo WSZYSTKIE 27 TESTOW ZAKONCZONYCH >> C:\Users\test\Analiza_10B\full_27_live.log
echo Koniec: %DATE% %TIME% >> C:\Users\test\Analiza_10B\full_27_live.log
echo ======================================== >> C:\Users\test\Analiza_10B\full_27_live.log
