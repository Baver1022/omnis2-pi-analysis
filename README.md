# OMNIS2 - Kompleksowa Analiza Statystyczna 10 Miliardów Cyfr π

## 📋 Opis Projektu

Projekt OMNIS2 to zaawansowana analiza statystyczna 10 miliardów cyfr liczby π, przeprowadzona przy użyciu 27 testów statystycznych z pakietów NIST Statistical Test Suite oraz TestU01 SmallCrush. Celem projektu było zbadanie właściwości losowych cyfr π na niespotykanej dotąd skali i ocena ich przydatności w zastosowaniach kryptograficznych.

## 🎯 Cele Badawcze

1. **Weryfikacja losowości**: Sprawdzenie, czy cyfry π wykazują właściwości losowe na dużej skali (10 miliardów cyfr)
2. **Analiza statystyczna**: Przeprowadzenie kompleksowej baterii 27 testów statystycznych
3. **Ocena kryptograficzna**: Określenie przydatności cyfr π jako źródła entropii w kryptografii
4. **Dokumentacja naukowa**: Stworzenie szczegółowych raportów naukowych z pełną dokumentacją metodologiczną

## 📁 Struktura Projektu

```
OMNIS2/
├── Program/                    # Kompletny program analizy
│   ├── analysis_orchestrator.py    # Główny orchestrator analizy
│   └── analysis_steps/             # 27 modułów testów statystycznych
│       ├── step_01_frequency.py
│       ├── step_02_runs.py
│       ├── step_03_block_frequency.py
│       ├── step_04_entropy.py
│       ├── step_05_spectral_fft.py
│       ├── step_06_compression.py
│       ├── step_07_entropy_bounds.py
│       ├── step_08_ml_lstm.py
│       ├── step_09_cumulative_sums.py
│       ├── step_10_approximate_entropy.py
│       ├── step_11_serial.py
│       ├── step_12_linear_complexity.py
│       ├── step_13_random_excursions.py
│       ├── step_14_random_excursions_variant.py
│       ├── step_15_universal_statistical.py
│       ├── step_16_non_overlapping_template.py
│       ├── step_17_overlapping_template.py
│       ├── step_18_birthday_spacings.py
│       ├── step_19_collision.py
│       ├── step_20_gap.py
│       ├── step_21_simple_poker.py
│       ├── step_22_coupon_collector.py
│       ├── step_23_maxoft.py
│       ├── step_24_weight_distrib.py
│       ├── step_25_matrix_rank.py
│       ├── step_26_hamming_indep.py
│       └── step_27_random_walk1.py
│
├── Raporty/                    # Raporty naukowe
│   ├── RAPORT_Z_ANALIZY_PI.pdf           # Raport w języku polskim (40+ stron)
│   ├── RAPORT_Z_ANALIZY_PI_EN.pdf        # Raport w języku angielskim
│   └── WZORY_MATEMATYCZNE_27_TESTOW.pdf  # Dokumentacja wzorów matematycznych
│
├── Dane z analizy/             # Wyniki badań (54 pliki JSON)
│   ├── 01_results.json         # Wyniki testu Frequency
│   ├── 01_status.json         # Status wykonania testu
│   ├── 02_results.json        # Wyniki testu Runs
│   ├── 02_status.json
│   └── ...                     # (wszystkie 27 testów)
│
└── README.md                   # Ten plik
```

## 🔬 Metodologia Badawcza

### Etap 1: Przygotowanie Danych
- **Źródło danych**: Plik `pi_10billion.txt` zawierający 10 miliardów cyfr π
- **Format**: Cyfry dziesiętne (0-9) zapisane sekwencyjnie
- **Weryfikacja**: Sprawdzenie poprawności danych przed analizą

### Etap 2: Implementacja Testów Statystycznych

#### Testy NIST Statistical Test Suite (17 testów):
1. **Frequency Test** - Test częstotliwości bitów
2. **Runs Test** - Test serii
3. **Block Frequency Test** - Test częstotliwości bloków
4. **Entropy Analysis** - Analiza entropii Shannona
5. **Spectral FFT Test** - Analiza widmowa FFT (z wykorzystaniem GPU)
6. **Compression Test** - Test kompresji
7. **Entropy Bounds** - Granice entropii
8. **ML LSTM Anomaly Detection** - Wykrywanie anomalii za pomocą LSTM
9. **Cumulative Sums Test** - Test sum skumulowanych
10. **Approximate Entropy Test** - Test przybliżonej entropii
11. **Serial Test** - Test szeregowy
12. **Linear Complexity Test** - Test złożoności liniowej
13. **Random Excursions Test** - Test przypadkowych wycieczek
14. **Random Excursions Variant Test** - Wariant testu wycieczek
15. **Universal Statistical Test** - Test uniwersalny statystyczny
16. **Non-overlapping Template Matching** - Test dopasowania szablonów bez nakładania
17. **Overlapping Template Matching** - Test dopasowania szablonów z nakładaniem

#### Testy TestU01 SmallCrush (10 testów):
18. **BirthdaySpacings** - Test odstępów urodzinowych
19. **Collision** - Test kolizji
20. **Gap** - Test przerw
21. **SimplePoker** - Test prostego pokera
22. **CouponCollector** - Test zbieracza kuponów
23. **MaxOft** - Test maksimum
24. **WeightDistrib** - Test rozkładu wag
25. **MatrixRank** - Test rangi macierzy
26. **HammingIndep** - Test niezależności Hamminga
27. **RandomWalk1** - Test losowego spaceru

### Etap 3: Wykonanie Analizy
- **Orchestracja**: Program `analysis_orchestrator.py` zarządza sekwencyjnym wykonaniem wszystkich 27 testów
- **Przetwarzanie**: Każdy test jest wykonywany niezależnie z zapisem wyników do plików JSON
- **Monitorowanie**: Status każdego testu jest śledzony i zapisywany
- **Optymalizacja**: Wykorzystanie GPU (CUDA) dla testów wymagających intensywnych obliczeń (FFT)

### Etap 4: Analiza Wyników
- **Interpretacja p-values**: Analiza wartości p dla każdego testu
- **Wykrywanie wzorców**: Identyfikacja subtelnych struktur w cyfrach π
- **Porównanie z losowością**: Ocena, czy wyniki są zgodne z oczekiwaniami dla prawdziwie losowej sekwencji
- **Analiza porównawcza**: Porównanie z innymi badaniami (kwantowe RNG, inne stałe matematyczne)

### Etap 5: Generowanie Raportów
- **Raport naukowy (PL)**: 40+ stron szczegółowej analizy z wykresami, tabelami i interpretacjami
- **Raport naukowy (EN)**: Pełna wersja angielska dla międzynarodowej społeczności naukowej
- **Dokumentacja wzorów**: Szczegółowy opis matematyczny wszystkich 27 testów

## 📊 Kluczowe Wyniki

### Testy Przechodzące (PASS)
Większość podstawowych testów statystycznych przeszła pomyślnie, potwierdzając lokalną losowość cyfr π:
- Frequency Test: ✅ PASS
- Runs Test: ✅ PASS
- Block Frequency: ✅ PASS
- Entropy Analysis: H ≈ 3.32 (blisko maksimum)
- Universal Statistical: p = 0.80
- Overlapping Template: p = 0.77

### Testy Wykazujące Struktury (FAIL)
Niektóre zaawansowane testy wykryły subtelne struktury na skali 10 miliardów cyfr:
- **Random Excursions**: p = 0.0 (wykryto odchylenia w rozkładzie stanów)
- **Random Excursions Variant**: p = 0.0 (obserwowane wartości różnią się od oczekiwanych)
- **Non-overlapping Template**: p = 2e-11 (za mało dopasowań szablonów)
- **BirthdaySpacings**: p = 0.0 (χ² = 91M)
- **SimplePoker**: p = 0.0
- **MaxOft**: p = 0.0
- **RandomWalk1**: p = 0.0

### Wnioski Naukowe
1. **Lokalna losowość**: Cyfry π wykazują doskonałe właściwości losowe na małych i średnich skalach
2. **Struktury globalne**: Na skali 10 miliardów cyfr wykryto subtelne struktury, które nie występują w prawdziwie losowych sekwencjach
3. **Zastosowania kryptograficzne**: π może być użyte jako dobry PRNG z odpowiednim seedem, ale nie jako CSPRNG solo
4. **Granice losowości**: Wyniki potwierdzają teoretyczne granice losowości dla deterministycznych stałych matematycznych

## 🛠️ Wymagania Techniczne

### Oprogramowanie
- Python 3.8+
- NumPy
- SciPy
- Matplotlib
- PyTorch (dla testów ML)
- CUDA Toolkit (opcjonalnie, dla przyspieszenia GPU)

### Sprzęt
- **Pamięć RAM**: Minimum 32 GB (dla pełnej analizy 10B cyfr)
- **Dysk**: ~10 GB wolnego miejsca
- **GPU**: Opcjonalnie NVIDIA CUDA-compatible (dla testów FFT)

## 🚀 Użycie

### Instalacja Zależności
```bash
pip install numpy scipy matplotlib torch
```

### Uruchomienie Analizy
```bash
cd Program
python3 analysis_orchestrator.py
```

### Struktura Wyników
Każdy test generuje dwa pliki JSON:
- `XX_results.json` - Szczegółowe wyniki testu (p-values, statystyki, interpretacje)
- `XX_status.json` - Status wykonania (sukces/błąd, czas wykonania)

## 📚 Dokumentacja

<<<<<<< Updated upstream
### 📄 Raporty Naukowe

<div align="center">

| 📊 Raport | 🌐 Język | 📥 Pobierz | 📄 Opis |
|:---------:|:--------:|:---------:|:-------:|
| **RAPORT_Z_ANALIZY_PI.pdf** | 🇵🇱 Polski | [📥 Pobierz PDF](OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI.pdf) | Kompleksowy raport naukowy (40+ stron) z pełną analizą statystyczną |
| **RAPORT_Z_ANALIZY_PI_EN.pdf** | 🇬🇧 English | [📥 Download PDF](OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) | Full scientific report (40+ pages) with complete statistical analysis |
| **WZORY_MATEMATYCZNE_27_TESTOW.pdf** | 📐 Formuły | [📥 Pobierz PDF](OMNIS2/Raporty/WZORY_MATEMATYCZNE_27_TESTOW.pdf) | Dokumentacja matematyczna wszystkich 27 testów statystycznych |

</div>

#### 📋 Zawartość Raportów Naukowych

**RAPORT_Z_ANALIZY_PI.pdf** (Polski) zawiera:
- 📖 Wprowadzenie teoretyczne
- 🔬 Szczegółowy opis wszystkich 27 testów statystycznych
- 📐 Wzory matematyczne dla każdego testu
- 📊 Wyniki i interpretacje statystyczne
- 📈 Wykresy i tabele wyników
- 🔍 Analizę porównawczą z innymi badaniami
- 💡 Wnioski i zastosowania kryptograficzne
- 📚 Bibliografia i referencje

**RAPORT_Z_ANALIZY_PI_EN.pdf** (English) zawiera:
- 📖 Theoretical introduction
- 🔬 Detailed description of all 27 statistical tests
- 📐 Mathematical formulas for each test
- 📊 Results and statistical interpretations
- 📈 Charts and result tables
- 🔍 Comparative analysis with other studies
- 💡 Conclusions and cryptographic applications
- 📚 Bibliography and references

### 📖 Inne Materiały

- **📖 Pełna dokumentacja:** [Branch OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **📊 Wyniki badań:** 54 pliki JSON w `OMNIS2/Dane z analizy/`
=======
### Raporty Naukowe
- **RAPORT_Z_ANALIZY_PI.pdf**: Kompleksowy raport naukowy w języku polskim zawierający:
  - Wprowadzenie teoretyczne
  - Szczegółowy opis wszystkich 27 testów
  - Wzory matematyczne
  - Wyniki i interpretacje
  - Wykresy i tabele
  - Analizę porównawczą
  - Wnioski i zastosowania kryptograficzne
>>>>>>> Stashed changes

- **RAPORT_Z_ANALIZY_PI_EN.pdf**: Pełna wersja angielska

- **WZORY_MATEMATYCZNE_27_TESTOW.pdf**: Dokumentacja matematyczna wszystkich testów

### Pliki Wynikowe
Wszystkie wyniki są dostępne w katalogu `Dane z analizy/` w formacie JSON, umożliwiając:
- Dalszą analizę
- Reprodukcję wyników
- Integrację z innymi narzędziami

## 🔬 Metodologia Interpretacji Wyników

### P-values
- **p > 0.01**: Wynik zgodny z hipotezą losowości
- **0.001 < p ≤ 0.01**: Słabe odchylenie od losowości
- **p ≤ 0.001**: Silne odchylenie od losowości

### Ważna Uwaga
Wyniki FAIL nie oznaczają "błędów" - są to **obserwacje naukowe** wskazujące na subtelne struktury w cyfrach π. Dla deterministycznej stałej matematycznej takie struktury są oczekiwane i stanowią ważny wkład w zrozumienie natury π.

## 📈 Statystyki Projektu

- **Liczba testów**: 27
- **Rozmiar danych**: 10 miliardów cyfr
- **Czas analizy**: ~kilka dni (w zależności od sprzętu)
- **Pliki wynikowe**: 54 pliki JSON
- **Rozmiar raportów**: 40+ stron każdy
- **Linie kodu**: ~5000+ linii Python

## 👤 Autor

**baver**

## 📄 Licencja

Projekt jest dostępny do celów naukowych i edukacyjnych.

## 🙏 Podziękowania

- NIST za opracowanie Statistical Test Suite
- TestU01 za zaawansowane testy losowości
- Społeczność naukowa za inspirację i wsparcie

## 📞 Kontakt

W razie pytań dotyczących metodologii lub wyników, proszę o kontakt przez GitHub Issues.

---

**Uwaga**: Projekt reprezentuje jedno z największych i najbardziej kompleksowych badań statystycznych cyfr π przeprowadzonych do tej pory. Wszystkie wyniki są w pełni udokumentowane i możliwe do reprodukcji.
