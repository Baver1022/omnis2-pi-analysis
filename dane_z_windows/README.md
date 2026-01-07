# Dane z Windows - Analiza Pi 10B

## 📁 Struktura

```
dane_z_windows/
├── Analiza_10B/          # Wyniki analizy (27 testów)
│   ├── 01_results.json   # Frequency Test (NIST)
│   ├── 02_results.json   # Runs Test (NIST)
│   ├── ...
│   ├── 27_results.json   # SmallCrush: RandomWalk1
│   └── analysis_summary.json  # Podsumowanie wszystkich testów
│
└── program/               # Program analizy
    ├── analysis_orchestrator.py  # Główny orchestrator
    ├── analysis_steps/           # 27 modułów testów
    ├── *.bat                     # Skrypty uruchomieniowe
    └── *.ps1                     # PowerShell skrypty
```

## ✅ Status

**WSZYSTKIE 27 TESTOW ZAKOŃCZONE!**

- ✅ Testy 01-12: NIST Statistical Tests
- ✅ Testy 13-17: NIST Advanced Tests  
- ✅ Testy 18-27: TestU01 SmallCrush

## 📊 Statystyki

- **Pliki wyników**: 27 × `*_results.json`
- **Pliki statusu**: 27 × `*_status.json`
- **Podsumowanie**: `analysis_summary.json`
- **Rozmiar**: ~836 KB

## 🗓️ Data kopiowania

2026-01-07 05:34

## 📝 Uwagi

- Wszystkie testy wykonane na **10 miliardach cyfr** Pi
- Analiza wykonana na Windows PC z GPU RTX 4060 Ti 16GB
- Program używa CPU fallback (CuPy nie działał)


