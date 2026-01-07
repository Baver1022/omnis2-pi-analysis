@echo off
cd C:\Users\test\OMNIS2
echo Uruchamiam test 13...
python analysis_orchestrator.py --pi-file C:\Users\test\pi_10billion.txt --output-dir C:\Users\test\Analiza_10B --max-digits 10000000000 --steps 13 --force
echo Test zakonczony!
pause

