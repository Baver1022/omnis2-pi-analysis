# 🔬 OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Pi

<div align="center">

[🇬🇧 English Version](README.md) • [📖 Dokumentacja](#-dokumentacja) • [🚀 Szybki Start](#-szybki-start) • [📊 Wyniki](#-wyniki-analizy) • [📄 Raporty](#-raporty-naukowe)

</div>

## 🌟 Co Mnie Fascynuje

Co mnie napędza w tym projekcie? **Tajemnica losowości** ukryta w nieskończonej sekwencji cyfr Pi. Czy Pi jest naprawdę losowe, czy zawiera ukryte wzorce? Czy mogę mu ufać w zastosowaniach kryptograficznych? Te pytania skłoniły mnie do przeprowadzenia jednej z najbardziej kompleksowych analiz statystycznych cyfr Pi, jakie kiedykolwiek wykonano.

Przeanalizowałem **10 miliardów cyfr** przy użyciu **27 rygorystycznych testów statystycznych** - podróż, która ujawniła zarówno oczekiwaną losowość, jak i zaskakujące anomalie. To dopiero początek - **moim następnym celem jest przeanalizowanie 1 biliona (1T) cyfr po przecinku**, przesuwając granice statystyki obliczeniowej i eksplorując najgłębsze tajemnice tej stałej matematycznej.

## 📊 O Projekcie

**OMNIS2** to kompleksowy projekt analizy statystycznej **10 miliardów cyfr Pi** przy użyciu **27 testów statystycznych** (17 testów NIST + 10 testów SmallCrush) z przyspieszeniem GPU.

Projekt zawiera:
- ✅ **27 testów statystycznych** (kod źródłowy Python)
- ✅ **55 plików JSON** z wynikami analizy 10B cyfr Pi
- ✅ **Raporty naukowe** (PDF) - po 70+ stron każdy
- ✅ **Wzory matematyczne** - kompletna dokumentacja
- ✅ **Przyspieszenie GPU** (CuPy dla NVIDIA RTX)
- ✅ **Przetwarzanie strumieniowe** - przetwarzanie 10B cyfr partiami

## 📈 Wyniki Analizy

Moja analiza 10 miliardów cyfr Pi ujawniła:

- ✅ **~70% testów PASS** - podstawowe testy potwierdzają lokalną losowość
- ⚠️ **Krytyczne FAIL** w testach Random Excursions (13, 14) i niektórych testach SmallCrush
- 📊 **Entropia**: H ≈ 3.32 (blisko maksimum dla systemu dziesiętnego)
- 📈 **Kompresja**: R ≈ 0.47 (wysoka nieprzewidywalność)

## 🌿 Główny Projekt - Gałąź OMNIS2

**Wszystkie pliki projektu znajdują się w gałęzi [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

### Struktura projektu w gałęzi OMNIS2:

```
OMNIS2/
├── Program/                      # Główny program
│   ├── analysis_orchestrator.py  # Główny orchestrator analizy
│   ├── analysis_steps/           # 27 modułów testów statystycznych
│   └── requirements.txt          # Zależności Python
├── Raporty/                      # Raporty naukowe (PDF)
│   ├── RAPORT_Z_ANALIZY_PI.pdf
│   └── RAPORT_Z_ANALIZY_PI_EN.pdf
├── Dane z analizy/               # Wyniki badań
│   └── *.json                    # 55 plików JSON z wynikami
└── README.md                     # Pełna dokumentacja
```

**[👉 Przejdź do gałęzi OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

## 🚀 Szybki Start

### Opcja 1: Instalacja z GitHub Packages (Zalecane)

```bash
# Zainstaluj pakiet
pip install omnis2-pi-analysis

# Uruchom analizę
python3 -m omnis2_pi_analysis.analysis_orchestrator --pi-file pi_10billion.txt
```

### Opcja 2: Pobierz pełny projekt:

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2

# Zainstaluj zależności
cd Program
pip install -r requirements.txt

# Uruchom analizę
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## 📚 Dokumentacja

### 📄 Raporty Naukowe

Oba raporty zawierają moją kompleksową analizę 10 miliardów cyfr Pi przy użyciu 27 testów statystycznych, w tym:

- 📖 **Wprowadzenie teoretyczne** - podstawy matematyczne i metodologia testów
- 🔬 **Szczegółowy opis** wszystkich 27 testów statystycznych (17 NIST + 10 SmallCrush)
- 📐 **Wzory matematyczne** - kompletne wzory i procedury testowe
- 📊 **Wyniki i interpretacje** - analiza statystyczna i testy istotności
- 📈 **Wykresy i tabele** - wizualizacje wyników testów
- 🔍 **Analiza porównawcza** - porównanie z poprzednimi badaniami
- 💡 **Wnioski** - implikacje dla kryptografii i teorii liczb
- 📚 **Bibliografia** - kompletne referencje i cytowania

<div align="center">

| | 🇵🇱 Polski | 🇬🇧 Angielski |
|:---:|:---:|:---:|
| **📄 Raport** | [RAPORT_Z_ANALIZY_PI.pdf](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [RAPORT_Z_ANALIZY_PI_EN.pdf](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |
| **📊 Strony** | 40+ | 40+ |
| **📥 Pobierz** | [📥 PDF](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [📥 PDF](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |

</div>

### 📖 Inne Materiały

- **📖 Pełna dokumentacja:** [Gałąź OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **📊 Wyniki badań:** 55 plików JSON w `OMNIS2/Dane z analizy/`

## 📦 Instalacja Pakietu

Projekt jest dostępny jako pakiet Python na **GitHub Packages**:

```bash
pip install omnis2-pi-analysis
```

**Szczegóły Pakietu:**
- 📦 **Nazwa:** `omnis2-pi-analysis`
- 📌 **Wersja:** `1.0.0`
- 🔗 **GitHub Packages:** [Zobacz Pakiet](https://github.com/Baver1022/omnis2-pi-analysis/packages)
- 📚 **Dokumentacja:** Zobacz [Gałąź OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)

## ⚡ Benchmarki Wydajności

Wyniki wydajności z mojej analizy:

- **Przetwarzanie 10 Miliardów Cyfr:**
  - Tylko CPU: ~5 godzin (szacunkowo)
  - Z przyspieszeniem GPU (NVIDIA RTX 4060 Ti 16GB): ~1-1.5 godziny
  - Przyśpieszenie: ~3-5x szybciej z GPU

- **Czasy Wykonania Testów (na miliard cyfr, z GPU):**
  - Testy częstotliwości: ~9-10 minut
  - Test runs: ~20 minut
  - Test częstotliwości blokowej: ~5 minut
  - Analiza entropii: ~29 minut
  - Spectral FFT (GPU): ~15 sekund (bardzo szybko!)
  - Test kompresji: ~18 minut
  - Przewidywanie LSTM: ~natychmiastowe (model wstępnie wytrenowany)

- **Użycie Pamięci:**
  - Szczytowa pamięć: ~1.3-2 GB (dla 1B cyfr)
  - Rozmiar partii strumieniowej: 100M cyfr (zoptymalizowane)
  - Pamięć GPU: ~2-4 GB (operacje CuPy)
  - Całkowite dla 10B: ~20-30 GB miejsca na dysku wymagane

## 🔗 Linki

- 🌿 **Gałąź OMNIS2:** [https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- 📦 **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- 📦 **Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)

## 👤 Autor

Projekt analizy statystycznej Pi - część baver

## 📄 Licencja

Zobacz plik LICENSE w gałęzi [OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2).

---

<div align="center">

**💡 Wszystkie pliki projektu, kod źródłowy, raporty i wyniki badań znajdują się w gałęzi [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

Stworzone z ❤️ dla matematyki i nauki

</div>
