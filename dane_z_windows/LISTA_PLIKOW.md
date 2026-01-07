# Pełna lista plików - dane_z_windows

**Data kopiowania:** 2026-01-07 05:34  
**Całkowity rozmiar:** 454 KB  
**Liczba plików:** 155  
**Liczba katalogów:** 5

---

## 📁 Struktura katalogów

```
dane_z_windows/
├── Analiza_10B/          (55 KB) - Wyniki analizy
├── program/              (394 KB) - Program analizy
└── README.md            (1.3 KB) - Dokumentacja
```

---

## 📊 Analiza_10B/ (55 KB)

### Wyniki testów (27 testów × 2 pliki = 54 pliki)

#### Testy 01-12 (NIST Statistical Tests)
- `01_results.json` (589 B) - Frequency Test (NIST)
- `01_status.json` (272 B)
- `02_results.json` (469 B) - Runs Test (NIST)
- `02_status.json` (267 B)
- `03_results.json` (418 B) - Block Frequency Test (NIST)
- `03_status.json` (278 B)
- `04_results.json` (478 B) - Entropy Analysis
- `04_status.json` (267 B)
- `05_results.json` (1.5 KB) - Spectral FFT Analysis
- `05_status.json` (278 B)
- `06_results.json` (457 B) - Compression Test
- `06_status.json` (265 B)
- `07_results.json` (1.7 KB) - Empirical Entropy Bounds
- `07_status.json` (275 B)
- `08_results.json` (288 B) - ML LSTM Anomaly Detection
- `08_status.json` (276 B)
- `09_results.json` (488 B) - Cumulative Sums Test (NIST)
- `09_status.json` (274 B)
- `10_results.json` (512 B) - Approximate Entropy Test (NIST)
- `10_status.json` (278 B)
- `11_results.json` (529 B) - Serial Test (NIST)
- `11_status.json` (265 B)
- `12_results.json` (588 B) - Linear Complexity Test (NIST)
- `12_status.json` (280 B)

#### Testy 13-17 (NIST Advanced Tests)
- `13_results.json` (1.9 KB) - Random Excursions Test (NIST)
- `13_status.json` (364 B)
- `14_results.json` (2.9 KB) - Random Excursions Variant (NIST)
- `14_status.json` (367 B)
- `15_results.json` (532 B) - Universal Statistical Test (NIST)
- `15_status.json` (284 B)
- `16_results.json` (1.9 KB) - Non-overlapping Template (NIST)
- `16_status.json` (282 B)
- `17_results.json` (1.9 KB) - Overlapping Template (NIST)
- `17_status.json` (278 B)

#### Testy 18-27 (TestU01 SmallCrush)
- `18_results.json` (480 B) - SmallCrush: BirthdaySpacings
- `18_status.json` (279 B)
- `19_results.json` (381 B) - SmallCrush: Collision
- `19_status.json` (272 B)
- `20_results.json` (401 B) - SmallCrush: Gap
- `20_status.json` (266 B)
- `21_results.json` (251 B) - SmallCrush: SimplePoker
- `21_status.json` (274 B)
- `22_results.json` (273 B) - SmallCrush: CouponCollector
- `22_status.json` (278 B)
- `23_results.json` (241 B) - SmallCrush: MaxOft
- `23_status.json` (269 B)
- `24_results.json` (270 B) - SmallCrush: WeightDistrib
- `24_status.json` (276 B)
- `25_results.json` (247 B) - SmallCrush: MatrixRank
- `25_status.json` (273 B)
- `26_results.json` (268 B) - SmallCrush: HammingIndep
- `26_status.json` (275 B)
- `27_results.json` (251 B) - SmallCrush: RandomWalk1
- `27_status.json` (274 B)

### Pliki dodatkowe
- `analysis_summary.json` (17 KB) - Podsumowanie wszystkich testów
- `test12_live.log` (5.7 KB) - Log testu 12
- `test12.log` (0 B) - Pusty log
- `testy_13-27_error.log` (0 B) - Pusty log błędów
- `testy_13-27_live.log` (0 B) - Pusty log

---

## 💻 program/ (394 KB)

### Główny program
- `analysis_orchestrator.py` (18 KB) - Główny orchestrator analizy

### analysis_steps/ (361 KB)

#### Pliki źródłowe Python (27 testów + base)
- `base_step.py` (5.7 KB) - Klasa bazowa dla wszystkich testów
- `__init__.py` (96 B) - Inicjalizacja modułu
- `gpu_template.py` (580 B) - Szablon GPU (nieużywany)
- `step_01_frequency.py` (2.5 KB) - Frequency Test
- `step_02_runs.py` (2.9 KB) - Runs Test
- `step_03_block_frequency.py` (2.6 KB) - Block Frequency Test
- `step_04_entropy.py` (2.6 KB) - Entropy Analysis
- `step_05_spectral_fft.py` (2.9 KB) - Spectral FFT Analysis
- `step_06_compression.py` (3.2 KB) - Compression Test
- `step_07_entropy_bounds.py` (5.0 KB) - Empirical Entropy Bounds
- `step_08_ml_lstm.py` (5.9 KB) - ML LSTM Anomaly Detection
- `step_09_cumulative_sums.py` (3.1 KB) - Cumulative Sums Test
- `step_10_approximate_entropy.py` (4.0 KB) - Approximate Entropy Test
- `step_11_serial.py` (4.1 KB) - Serial Test
- `step_12_linear_complexity.py` (5.6 KB) - Linear Complexity Test
- `step_13_random_excursions.py` (6.5 KB) - Random Excursions Test
- `step_14_random_excursions_variant.py` (4.9 KB) - Random Excursions Variant
- `step_15_universal_statistical.py` (5.7 KB) - Universal Statistical Test
- `step_16_non_overlapping_template.py` (4.9 KB) - Non-overlapping Template
- `step_17_overlapping_template.py` (4.7 KB) - Overlapping Template
- `step_18_birthday_spacings.py` (5.2 KB) - SmallCrush: BirthdaySpacings
- `step_19_collision.py` (2.9 KB) - SmallCrush: Collision
- `step_20_gap.py` (3.3 KB) - SmallCrush: Gap
- `step_21_simple_poker.py` (2.2 KB) - SmallCrush: SimplePoker
- `step_22_coupon_collector.py` (2.0 KB) - SmallCrush: CouponCollector
- `step_23_maxoft.py` (1.8 KB) - SmallCrush: MaxOft
- `step_24_weight_distrib.py` (1.6 KB) - SmallCrush: WeightDistrib
- `step_25_matrix_rank.py` (2.3 KB) - SmallCrush: MatrixRank
- `step_26_hamming_indep.py` (2.0 KB) - SmallCrush: HammingIndep
- `step_27_random_walk1.py` (1.8 KB) - SmallCrush: RandomWalk1

#### __pycache__/ (255 KB) - Cache Python
Pliki skompilowane dla różnych wersji Pythona (3.11, 3.13, 3.14):
- `base_step.cpython-*.pyc` (9-11 KB)
- `__init__.cpython-*.pyc` (254-269 B)
- `step_01-27_*.cpython-*.pyc` (2.5-7.3 KB każdy)

**Uwaga:** Cache można bezpiecznie usunąć - zostanie wygenerowany ponownie przy uruchomieniu.

### Skrypty uruchomieniowe (.bat)
- `SPRAWDZ_STATUS.bat` (1.6 KB) - Sprawdzanie statusu analizy
- `START_13-27_LIVE.bat` (726 B) - Uruchomienie testów 13-27 z podglądem
- `START_13-27_LIVE_LOG.bat` (1.0 KB) - Uruchomienie testów 13-27 z logiem
- `START_ALL_TESTS_13-27.bat` (780 B) - Uruchomienie testów 13-27
- `START_ALL_TESTS_13-27_NOPAUSE.bat` (958 B) - Uruchomienie testów 13-27 bez pauzy
- `START_FULL_27.bat` (880 B) - Uruchomienie wszystkich 27 testów
- `TEST_13_MANUAL.bat` (246 B) - Ręczne uruchomienie testu 13

### Skrypty PowerShell (.ps1)
- `sprawdz_status.ps1` (4.3 KB) - Szczegółowy skrypt sprawdzania statusu

---

## 📈 Statystyki

### Pliki wyników
- **27 plików** `*_results.json` (razem ~18 KB)
- **27 plików** `*_status.json` (razem ~7.5 KB)
- **1 plik** `analysis_summary.json` (17 KB)

### Pliki programu
- **1 plik** główny orchestrator (18 KB)
- **27 plików** testów Python (razem ~96 KB)
- **1 plik** base_step.py (5.7 KB)
- **~80 plików** cache Python (255 KB) - można usunąć

### Skrypty
- **7 plików** .bat (razem ~5.5 KB)
- **1 plik** .ps1 (4.3 KB)

---

## ✅ Status analizy

**WSZYSTKIE 27 TESTOW ZAKOŃCZONE!**

- ✅ Testy 01-12: NIST Statistical Tests (12 testów)
- ✅ Testy 13-17: NIST Advanced Tests (5 testów)
- ✅ Testy 18-27: TestU01 SmallCrush (10 testów)

**Analiza wykonana na 10 miliardach cyfr Pi**

---

## 📝 Uwagi

1. **__pycache__/** - Cache Python można bezpiecznie usunąć (zostanie wygenerowany ponownie)
2. **Puste logi** - `test12.log`, `testy_13-27_error.log`, `testy_13-27_live.log` są puste (0 B)
3. **gpu_template.py** - Nieużywany szablon, można usunąć
4. Wszystkie pliki skopiowane z Windows PC (2026-01-07 05:34)


