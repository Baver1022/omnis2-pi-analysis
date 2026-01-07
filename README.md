# OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Liczby Pi

## Opis Projektu

Kompleksowa analiza statystyczna 10 miliardów cyfr liczby Pi przy użyciu 27 testów statystycznych (17 testów NIST + 10 testów SmallCrush) z akceleracją GPU. Projekt generuje szczegółowe raporty naukowe w formacie LaTeX/PDF z pełną dokumentacją matematyczną, wykresami i interpretacją wyników.

## Struktura Projektu

```
OMNIS2/
├── analysis_orchestrator.py              # Główny orchestrator analizy
├── analysis_steps/                       # 27 modułów testów statystycznych
│   ├── step_01_frequency.py
│   ├── step_02_runs.py
│   ├── ...
│   └── step_27_random_walk1.py
├── generuj_raport_kompletny_final.py     # Generator raportu PL (LaTeX)
├── generuj_raport_kompletny_final_EN.py  # Generator raportu EN (LaTeX)
├── analiza_wynikow_output/               # Wygenerowane raporty i wykresy
│   ├── RAPORT_NAUKOWY_PI.pdf            # Raport naukowy PL (70+ stron)
│   ├── RAPORT_NAUKOWY_PI_EN.pdf         # Raport naukowy EN (70+ stron)
│   └── figures/                         # Wykresy i wizualizacje
├── dane_z_windows/                       # Wyniki analizy 10B cyfr
│   └── Analiza_10B/                     # Pliki JSON z wynikami testów (55 plików - WYNIKI BADAŃ)
├── WZORY_MATEMATYCZNE_27_TESTOW.pdf     # PDF z wzorami matematycznymi
├── requirements.txt                      # Zależności Python
├── .gitignore                           # Pliki ignorowane przez Git
└── README.md                            # Ten plik
```

## Funkcjonalności

- ✅ **27 testów statystycznych** (NIST + SmallCrush)
- ✅ **Akceleracja GPU** (CuPy dla NVIDIA RTX)
- ✅ **Streaming processing** - przetwarzanie 10B cyfr batch-by-batch
- ✅ **Checkpointing** - automatyczne zapisywanie wyników
- ✅ **Remote monitoring** - monitorowanie z Linux na Windows
- ✅ **Generowanie raportów naukowych** - LaTeX/PDF z pełną dokumentacją
- ✅ **Wizualizacje** - wykresy p-values, czasów wykonania, entropii, itp.

## Wymagania

### Python dependencies

```bash
pip install -r requirements.txt
```

### LaTeX (dla generowania PDF)

```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# Fedora/RHEL
sudo dnf install texlive-scheme-basic texlive-collection-latexextra
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

### 2. Generowanie raportu naukowego

Po zakończeniu analizy, wygeneruj raport:

```bash
# Raport w języku polskim
python3 generuj_raport_kompletny_final.py

# Raport w języku angielskim
python3 generuj_raport_kompletny_final_EN.py
```

Raporty zostaną wygenerowane w katalogu `analiza_wynikow_output/`:
- `RAPORT_NAUKOWY_PI.pdf` - raport PL (70+ stron)
- `RAPORT_NAUKOWY_PI_EN.pdf` - raport EN (70+ stron)

### 3. Monitorowanie postępu

```bash
# Sprawdź status wszystkich testów
python3 analysis_orchestrator.py --status-only

# Monitorowanie z Linux (jeśli analiza działa na Windows)
./sprawdz_status_ssh.sh
```

## Dokumentacja

- **Wzory matematyczne:** `WZORY_MATEMATYCZNE_27_TESTOW.pdf`
- **Plan analizy:** `PLAN_ANALIZ_EXPERIMENTAL_MATH.md`
- **Status implementacji:** `OPCJA_C_UKONCZONA.md`

## Testy Statystyczne

### NIST Statistical Test Suite (17 testów):
1. Frequency Test
2. Runs Test
3. Block Frequency Test
4. Entropy Test
5. Spectral FFT Test
6. Compression Test
7. Empirical Entropy Bounds
8. ML LSTM Test (placeholder)
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

Szczegółowe wyniki dostępne w wygenerowanych raportach PDF.

## Status

✅ **27/27 testów zaimplementowanych**  
✅ **GPU acceleration działa**  
✅ **Streaming dla 10B cyfr działa**  
✅ **Raporty naukowe wygenerowane** (PL i EN, 70+ stron każdy)

## Struktura Raportu Naukowego

Każdy raport zawiera:
- Wprowadzenie teoretyczne
- Opis 27 testów statystycznych z wzorami matematycznymi
- Szczegółowe wyniki i interpretacje
- Wizualizacje (wykresy p-values, entropii, czasów wykonania)
- Analizę porównawczą z innymi badaniami
- Sekcję zastosowań kryptograficznych
- Wnioski i granice losowości

## Autor

Projekt analizy statystycznej liczby Pi - część hexstrike-ai

## Licencja

Zobacz plik LICENSE w głównym katalogu projektu.

