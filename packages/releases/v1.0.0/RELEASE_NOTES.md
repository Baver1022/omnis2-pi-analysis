# OMNIS2 - Releases

## Opis

Ten katalog zawiera wydania (releases) projektu OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Liczby Pi.

## Struktura

```
packages/releases/
├── README.md                    # Ten plik
└── v1.0.0/                     # Przykładowa wersja (do utworzenia)
    ├── omnis2-pi-analysis-v1.0.0.tar.gz
    ├── omnis2-pi-analysis-v1.0.0.zip
    └── CHANGELOG.md
```

## Wydania

### v1.0.0 (2026-01-07)
- ✅ 27 testów statystycznych (NIST + SmallCrush)
- ✅ Analiza 10 miliardów cyfr Pi
- ✅ Generatory raportów naukowych (PL i EN)
- ✅ 55 plików JSON z wynikami badań
- ✅ Dokumentacja i wzory matematyczne

## Instalacja

### Z pliku tar.gz:
```bash
tar -xzf omnis2-pi-analysis-v1.0.0.tar.gz
cd omnis2-pi-analysis-v1.0.0
pip install -r requirements.txt
```

### Z pliku zip:
```bash
unzip omnis2-pi-analysis-v1.0.0.zip
cd omnis2-pi-analysis-v1.0.0
pip install -r requirements.txt
```

## Użycie

Po instalacji:
```bash
# Uruchomienie analizy
python3 analysis_orchestrator.py --pi-file pi_10billion.txt

# Generowanie raportu PL
python3 generuj_raport_kompletny_final.py

# Generowanie raportu EN
python3 generuj_raport_kompletny_final_EN.py
```

## Wymagania

- Python 3.8+
- NumPy, SciPy, Pandas
- Matplotlib (dla wizualizacji)
- LaTeX (dla generowania PDF)
- CuPy (opcjonalne, dla GPU acceleration)

Zobacz `requirements.txt` w głównym katalogu projektu.

## Licencja

Zobacz plik LICENSE w głównym katalogu projektu.

