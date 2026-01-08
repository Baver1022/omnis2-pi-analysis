# 🔬 OMNIS2 - Dokumentacja Techniczna i Implementacja

<div align="center">

[🇬🇧 English Version](README.md) • [📖 Dokumentacja Programu](Program/README.md) • [🚀 Szybki Start](#-szybki-start) • [📊 Wyniki](#-szczegółowe-wyniki) • [📄 Raporty](#-raporty-naukowe)

**To jest gałąź OMNIS2 - zawiera cały kod źródłowy, wyniki analizy i dokumentację techniczną**

[← Powrót do Gałęzi Głównej](https://github.com/Baver1022/omnis2-pi-analysis)

</div>

## 📋 Przegląd

Ta gałąź zawiera kompletną implementację systemu analizy statystycznej OMNIS2 dla 10 miliardów cyfr Pi. Wszystki kod źródłowy, wyniki analizy, raporty naukowe i dokumentacja techniczna znajdują się tutaj.

## 📁 Struktura Projektu

```
OMNIS2/
├── Program/                      # Główny program analizy
│   ├── analysis_orchestrator.py # Orchestrator (zarządza wszystkimi 27 testami)
│   ├── analysis_steps/          # Implementacje poszczególnych testów
│   │   ├── step_01_frequency.py
│   │   ├── step_02_runs.py
│   │   ├── ...                   # (27 plików testów)
│   │   ├── base_step.py          # Klasa bazowa z checkpointing
│   │   └── gpu_template.py       # Szablon przyspieszenia GPU
│   ├── requirements.txt          # Zależności Python
│   └── README.md                 # Dokumentacja programu
│
├── Raporty/                      # Raporty naukowe (PDF)
│   ├── RAPORT_Z_ANALIZY_PI.pdf      # Raport polski (40+ stron)
│   └── RAPORT_Z_ANALIZY_PI_EN.pdf   # Raport angielski (40+ stron)
│
├── Dane z analizy/               # Wyniki analizy (JSON)
│   ├── 01_results.json           # Wyniki Frequency Test
│   ├── 01_status.json            # Status Frequency Test
│   ├── ...                       # (55 plików JSON łącznie)
│   └── analysis_summary.json    # Pełne podsumowanie analizy
│
├── README.md                     # Ten plik
└── README_PL.md                  # Wersja polska
```

## 🚀 Szybki Start

### Wymagania

- Python 3.8+
- NVIDIA GPU z obsługą CUDA (opcjonalne, dla przyspieszenia GPU)
- ~20-30 GB miejsca na dysku dla analizy 10B cyfr

### Instalacja

```bash
# Sklonuj repozytorium
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2

# Zainstaluj zależności
cd Program
pip install -r requirements.txt
```

### Uruchomienie Analizy

```bash
# Pełna analiza (wszystkie 27 testów)
python3 analysis_orchestrator.py \
    --pi-file /ścieżka/do/pi_10billion.txt \
    --output-dir ../Dane\ z\ analizy \
    --max-digits 10000000000

# Uruchom tylko wybrane testy
python3 analysis_orchestrator.py \
    --pi-file /ścieżka/do/pi_10billion.txt \
    --output-dir ../Dane\ z\ analizy \
    --steps 01 02 05  # Tylko Frequency, Runs i Spectral FFT

# Sprawdź status analizy
python3 analysis_orchestrator.py \
    --pi-file /ścieżka/do/pi_10billion.txt \
    --output-dir ../Dane\ z\ analizy \
    --status
```

## 🔬 27 Testów Statystycznych

### NIST Statistical Test Suite (17 testów)

| # | Nazwa Testu | Moduł | Opis |
|---|-------------|-------|------|
| 01 | Frequency Test | `step_01_frequency.py` | Test proporcji zer i jedynek |
| 02 | Runs Test | `step_02_runs.py` | Test całkowitej liczby runs |
| 03 | Block Frequency Test | `step_03_block_frequency.py` | Test proporcji w blokach M-bitowych |
| 04 | Entropy Analysis | `step_04_entropy.py` | Obliczanie entropii Shannona |
| 05 | Spectral FFT Test | `step_05_spectral_fft.py` | Analiza FFT z przyspieszeniem GPU |
| 06 | Compression Test | `step_06_compression.py` | Test kompresowalności |
| 07 | Entropy Bounds | `step_07_entropy_bounds.py` | Empiryczne granice entropii |
| 09 | Cumulative Sums Test | `step_09_cumulative_sums.py` | Test sum skumulowanych |
| 10 | Approximate Entropy | `step_10_approximate_entropy.py` | Częstotliwość nakładających się wzorców |
| 11 | Serial Test | `step_11_serial.py` | Częstotliwość wszystkich wzorców m-bitowych |
| 12 | Linear Complexity | `step_12_linear_complexity.py` | Test długości LFSR |
| 13 | Random Excursions | `step_13_random_excursions.py` | Liczba cykli w random walk |
| 14 | Random Excursions Variant | `step_14_random_excursions_variant.py` | Liczba wizyt stanów |
| 15 | Universal Statistical | `step_15_universal_statistical.py` | Test uniwersalny Maurera |
| 16 | Non-overlapping Template | `step_16_non_overlapping_template.py` | Dopasowanie szablonów |
| 17 | Overlapping Template | `step_17_overlapping_template.py` | Nakładające się dopasowanie szablonów |

### TestU01 SmallCrush (10 testów)

| # | Nazwa Testu | Moduł | Opis |
|---|-------------|-------|------|
| 18 | Birthday Spacings | `step_18_birthday_spacings.py` | Rozkład odstępów |
| 19 | Collision | `step_19_collision.py` | Kolizje w hash table |
| 20 | Gap | `step_20_gap.py` | Rozkład gapów |
| 21 | Simple Poker | `step_21_simple_poker.py` | Rozkład rąk pokerowych |
| 22 | Coupon Collector | `step_22_coupon_collector.py` | Test zbierania kuponów |
| 23 | MaxOft | `step_23_maxoft.py` | Rozkład wartości maksymalnych |
| 24 | Weight Distribution | `step_24_weight_distrib.py` | Rozkład wag |
| 25 | Matrix Rank | `step_25_matrix_rank.py` | Ranga macierzy losowej |
| 26 | Hamming Independence | `step_26_hamming_indep.py` | Odległość Hamminga |
| 27 | Random Walk1 | `step_27_random_walk1.py` | Pozycje random walk |

### Komponent Machine Learning

| # | Komponent | Moduł | Opis |
|---|-----------|-------|------|
| 08 | LSTM Anomaly Detection | `step_08_ml_lstm.py` | Przewidywanie wzorców siecią neuronową |

## 📊 Szczegółowe Wyniki

### Podsumowanie Analizy

Kompletna analiza 10 miliardów cyfr Pi wyprodukowała:

- **55 plików JSON** ze szczegółowymi wynikami dla każdego testu
- **Podsumowanie analizy** w `Dane z analizy/analysis_summary.json`
- **Wyniki poszczególnych testów** w `Dane z analizy/XX_results.json`
- **Status testów** w `Dane z analizy/XX_status.json`

### Kluczowe Metryki

- **Całkowita liczba testów:** 27
- **Testy zaliczone:** ~70% (19/27)
- **Testy niezaliczone:** ~30% (8/27)
- **Entropia (H):** ≈ 3.32 (99.7% maksimum 3.3219)
- **Współczynnik kompresji (R):** ≈ 0.47
- **Czas przetwarzania:** ~1-1.5 godziny (z przyspieszeniem GPU)

### Kluczowe Odkrycia

- ✅ **Testy częstotliwości:** Wszystkie zaliczone - równomierny rozkład cyfr
- ✅ **Testy runs:** Zaliczone - brak wzorców w sekwencjach
- ✅ **Entropia:** Blisko maksimum - wysoka losowość
- ⚠️ **Random Excursions (13, 14):** Niezaliczone - potencjalne korelacje długiego zasięgu
- ⚠️ **Niektóre testy SmallCrush:** Niezaliczone - wykryte nieoczekiwane wzorce

## 📄 Raporty Naukowe

Kompleksowe raporty naukowe z pełną metodologią, wzorami i interpretacjami:

<div align="center">

| | 🇵🇱 Polski | 🇬🇧 Angielski |
|:---:|:---:|:---:|
| **📄 Raport** | [RAPORT_Z_ANALIZY_PI.pdf](Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [RAPORT_Z_ANALIZY_PI_EN.pdf](Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |
| **📊 Strony** | 40+ | 40+ |
| **📥 Pobierz** | [📥 PDF](Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [📥 PDF](Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |

</div>

**Zawartość Raportów:**
- Kompletne tło teoretyczne
- Szczegółowy opis wszystkich 27 testów
- Wzory matematyczne i procedury
- Kompleksowe wyniki z interpretacjami
- Wizualizacje i tabele danych
- Analiza porównawcza
- Wnioski i przyszłe kierunki
- Kompletna bibliografia

## 🏗️ Architektura

### Projekt Modułowy

Każdy test jest zaimplementowany jako niezależny moduł dziedziczący z `AnalysisStep`:

```python
class Step01Frequency(AnalysisStep):
    def execute(self, pi_digits):
        # Implementacja testu
        return results
```

### Funkcje

- **Checkpointing:** Każdy krok może być wstrzymany i wznowiony
- **Niezależne wykonanie:** Uruchom tylko wybrane testy
- **Przyspieszenie GPU:** Automatyczne wykrywanie i użycie GPU
- **Przetwarzanie strumieniowe:** Efektywne obsługiwanie dużych zbiorów danych
- **Wyjście JSON:** Ustrukturyzowane wyniki do dalszej analizy

### Przyspieszenie GPU

Testy z obsługą GPU:
- `step_05_spectral_fft.py` - Operacje FFT na GPU
- Inne testy używają CPU z opcjonalnymi optymalizacjami GPU

## 📈 Wydajność

### Czasy Wykonania (10B cyfr, z przyspieszeniem GPU)

- **Testy częstotliwości:** ~9-10 min na 1B cyfr
- **Test runs:** ~20 min na 1B cyfr
- **Analiza entropii:** ~29 min na 1B cyfr
- **Spectral FFT (GPU):** ~15 sekund na 1B cyfr
- **Całkowite dla 10B:** ~1-1.5 godziny

### Użycie Zasobów

- **Szczytowa pamięć:** ~1.3-2 GB (dla 1B cyfr)
- **Pamięć GPU:** ~2-4 GB (operacje CuPy)
- **Miejsce na dysku:** ~20-30 GB dla pełnej analizy 10B
- **Rozmiar partii:** 100M cyfr (zoptymalizowane)

## 🔧 Konfiguracja

### Opcje Linii Poleceń

```bash
analysis_orchestrator.py [OPCJE]

Opcje:
  --pi-file ŚCIEŻKA      Ścieżka do pliku z cyframi Pi (wymagane)
  --output-dir ŚCIEŻKA    Katalog wyjściowy (domyślnie: ../Dane z analizy)
  --max-digits N          Maksymalna liczba cyfr do analizy
  --steps XX YY ZZ        Uruchom tylko określone kroki
  --status                Pokaż status analizy
  --verbose               Włącz szczegółowe wyjście
  --gpu                   Wymuś użycie GPU
```

### Format Wyjścia

Każdy test produkuje:
- `XX_results.json` - Wyniki testu z p-values, statystykami
- `XX_status.json` - Status wykonania, znaczniki czasu
- `analysis_summary.json` - Kompletne podsumowanie wszystkich testów

## 📚 Dokumentacja

- **Dokumentacja Programu:** [Program/README.md](Program/README.md)
- **Raporty Naukowe:** [Raporty/](Raporty/)
- **Wyniki Analizy:** [Dane z analizy/](Dane%20z%20analizy/)

## 🔗 Linki

- **Gałąź Główna:** [https://github.com/Baver1022/omnis2-pi-analysis](https://github.com/Baver1022/omnis2-pi-analysis)
- **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)

## 👤 Autor

Projekt analizy statystycznej Pi - część baver

## 📄 Licencja

Zobacz plik [LICENSE](LICENSE).

---

<div align="center">

**💡 Ta gałąź zawiera całą implementację techniczną, kod źródłowy i wyniki analizy**

**Dla przeglądu projektu i ogólnych informacji, zobacz [gałąź główną](https://github.com/Baver1022/omnis2-pi-analysis)**

Stworzone z ❤️ dla matematyki i nauki

</div>
