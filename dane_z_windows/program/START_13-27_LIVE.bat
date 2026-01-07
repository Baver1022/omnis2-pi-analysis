@echo off
title ANALIZA PI - TESTY 13-27 (10B) - LIVE
color 0A
echo ========================================
echo ANALIZA PI - TESTY 13-27 (LIVE)
echo ========================================
echo Start: %DATE% %TIME%
echo.
echo Bedziesz widzial kazdy krok na zywo!
echo.
echo ========================================
echo.

cd C:\Users\test\OMNIS2

python analysis_orchestrator.py --pi-file C:\Users\test\pi_10billion.txt --output-dir C:\Users\test\Analiza_10B --max-digits 10000000000 --steps 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 --force

echo.
echo ========================================
echo WSZYSTKIE TESTY 13-27 ZAKONCZONE!
echo ========================================
echo Koniec: %DATE% %TIME%
echo.
pause

