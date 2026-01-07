# OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Liczby Pi

## Opis Projektu

Kompleksowa analiza statystyczna 10 miliardów cyfr liczby Pi przy użyciu 27 testów statystycznych (17 testów NIST + 10 testów SmallCrush) z akceleracją GPU.

## Struktura Projektu

```
omnis2-pi-analysis/
├── analysis_orchestrator.py              # Główny orchestrator analizy
├── analysis_steps/                       # 27 modułów testów statystycznych
│   ├── step_01_frequency.py
│   ├── step_02_runs.py
│   ├── ...
│   └── step_27_random_walk1.py
├── analiza_wynikow_output/               # Wygenerowane raporty i wykresy
│   ├── figures/                         # Wykresy i wizualizacje
│   └── wyniki_tabela.csv                # Tabela wyników
├── dane_z_windows/                       # Wyniki analizy 10B cyfr
│   ├── Analiza_10B/                     # Pliki JSON z wynikami testów (55 plików - WYNIKI BADAŃ)
│   │   └── README_WYNIKI.md            # Opis wyników
│   └── program/                          # Wersja Windows z batch files
├── packages/
│   └── releases/                        # Struktura dla releases
│       ├── README.md                    # Opis releases
│       └── CHANGELOG.md                 # Historia zmian
├── WZORY_MATEMATYCZNE_27_TESTOW.pdf     # PDF z wzorami matematycznymi
├── requirements.txt                      # Zależności Python
├── .gitignore                           # Pliki ignorowane przez Git
├── LICENSE                              # Licencja projektu
└── README.md                            # Ten plik
```

## Funkcjonalności

- ✅ **27 testów statystycznych** (NIST + SmallCrush)
- ✅ **Akceleracja GPU** (CuPy dla NVIDIA RTX)
- ✅ **Streaming processing** - przetwarzanie 10B cyfr batch-by-batch
- ✅ **Checkpointing** - automatyczne zapisywanie wyników
- ✅ **Remote monitoring** - monitorowanie z Linux na Windows
- ✅ **Wizualizacje** - wykresy p-values, czasów wykonania, entropii, itp.
- ✅ **Wyniki badań** - 55 plików JSON z kompletnymi wynikami analizy

## Wymagania

### Python dependencies

```bash
pip install -r requirements.txt
```

### GPU (opcjonalne)

```bash
# CUDA 12.x
pip install cupy-cuda12x

# CUDA 11.x
pip install cupy-cuda11x
```

## Użycie

### 1. Uruchomienie analizy statystycznej

#### Na Windows (gdzie znajduje się plik pi_10billion.txt):

```batch
cd dane_z_windows\program
START_FULL_27.bat
```

#### Na Linux:

```bash
python3 analysis_orchestrator.py --pi-file pi_10billion.txt --output-dir analiza_wynikow_output
```

### 2. Monitorowanie postępu

```bash
# Sprawdź status wszystkich testów
python3 analysis_orchestrator.py --status-only

# Sprawdź status plików JSON w katalogu dane_z_windows/Analiza_10B/
ls -lh dane_z_windows/Analiza_10B/*.json
```

### 3. Analiza wyników

Wyniki są zapisywane w formacie JSON w katalogu `dane_z_windows/Analiza_10B/`:
- `XX_results.json` - szczegółowe wyniki testu (27 plików)
- `XX_status.json` - status wykonania testu (27 plików)
- `analysis_summary.json` - podsumowanie wszystkich testów

## Dokumentacja

- **Wzory matematyczne:** `WZORY_MATEMATYCZNE_27_TESTOW.pdf` - Kompletne wzory matematyczne dla wszystkich 27 testów
- **Wyniki badań:** `dane_z_windows/Analiza_10B/README_WYNIKI.md` - Opis wyników analizy
- **Releases:** `packages/releases/README.md` - Informacje o wydaniach projektu

## Testy Statystyczne

### NIST Statistical Test Suite (17 testów):

1. Frequency Test
2. Runs Test
3. Block Frequency Test
4. Entropy Test
5. Spectral FFT Test
6. Compression Test
7. Empirical Entropy Bounds
8. ML LSTM Test
9. Cumulative Sums Test
10. Approximate Entropy Test
11. Serial Test
12. Linear Complexity Test
13. Random Excursions Test
14. Random Excursions Variant Test
15. Universal Statistical Test
16. Non-overlapping Template Matching Test
17. Overlapping Template Matching Test

### SmallCrush Test Suite (10 testów):

18. Birthday Spacings Test
19. Collision Test
20. Gap Test
21. Simple Poker Test
22. Coupon Collector Test
23. MaxOft Test
24. Weight Distribution Test
25. Matrix Rank Test
26. Hamming Independence Test
27. Random Walk 1 Test

## Wyniki Analizy

Analiza 10 miliardów cyfr Pi wykazała:

- ✅ **~70% testów PASS** - podstawowe testy potwierdzają lokalną losowość
- ⚠️ **Krytyczne FAIL** w testach Random Excursions (13, 14) i niektórych SmallCrush
- 📊 **Entropia**: H ≈ 3.32 (blisko maksimum dla systemu dziesiętnego)
- 📈 **Kompresja**: R ≈ 0.47 (wysoka nieprzewidywalność)

Szczegółowe wyniki dostępne w plikach JSON w katalogu `dane_z_windows/Analiza_10B/`.

## Status

✅ **27/27 testów zaimplementowanych**  
✅ **GPU acceleration działa**  
✅ **Streaming dla 10B cyfr działa**  
✅ **Wyniki badań dostępne** (55 plików JSON)

## Struktura Wyników

Każdy test generuje:
- Wyniki statystyczne (p-values, statystyki testowe)
- Czas wykonania
- Interpretację wyników
- Metadane wykonania (liczba przetworzonych cyfr, status)

## Autor

Projekt analizy statystycznej liczby Pi - część baver

## Licencja

Zobacz plik LICENSE w głównym katalogu projektu.

## Repozytorium

[View on GitHub](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
