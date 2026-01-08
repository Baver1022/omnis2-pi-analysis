# 🔬 OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Pi

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![GPU](https://img.shields.io/badge/GPU-CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![GitHub](https://img.shields.io/github/stars/Baver1022/omnis2-pi-analysis?style=for-the-badge&logo=github)
![GitHub forks](https://img.shields.io/github/forks/Baver1022/omnis2-pi-analysis?style=for-the-badge&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/Baver1022/omnis2-pi-analysis?style=flat-square&logo=git)
![Code Size](https://img.shields.io/github/languages/code-size/Baver1022/omnis2-pi-analysis?style=flat-square)

**🔬 Kompleksowa analiza statystyczna 10 miliardów cyfr Pi przy użyciu 27 rygorystycznych testów**

[🇬🇧 English Version](README.md) • [📖 Dokumentacja](#-dokumentacja) • [🚀 Szybki Start](#-szybki-start) • [📊 Wyniki](#-wyniki-analizy) • [📄 Raporty](#-raporty-naukowe)

</div>

## 🌟 Co Mnie Fascynuje

Co mnie napędza w tym projekcie? **Tajemnica losowości** ukryta w nieskończonej sekwencji cyfr Pi. Czy Pi jest naprawdę losowe, czy zawiera ukryte wzorce? Czy mogę mu ufać w zastosowaniach kryptograficznych? Te pytania skłoniły mnie do przeprowadzenia jednej z najbardziej kompleksowych analiz statystycznych cyfr Pi, jakie kiedykolwiek wykonano.

Przeanalizowałem **10 miliardów cyfr** przy użyciu **27 rygorystycznych testów statystycznych** - podróż, która ujawniła zarówno oczekiwaną losowość, jak i zaskakujące anomalie. To dopiero początek - **moim następnym celem jest przeanalizowanie 1 biliona (1T) cyfr po przecinku**, przesuwając granice statystyki obliczeniowej i eksplorując najgłębsze tajemnice tej stałej matematycznej.

## 📊 O Projekcie

**OMNIS2** to kompleksowy projekt analizy statystycznej **10 miliardów cyfr Pi** przy użyciu **27 testów statystycznych** (17 testów NIST + 10 testów SmallCrush) z przyspieszeniem GPU.

> **Słowa kluczowe:** Analiza cyfr Pi, testy losowości statystycznej, testy NIST, SmallCrush, obliczenia GPU, kryptografia, teoria liczb, stałe matematyczne, data science, Python, CuPy, analiza statystyczna, walidacja losowości, badania Pi, matematyka obliczeniowa, **AI, machine learning, deep learning, sieci neuronowe, rozpoznawanie wzorców, analiza danych, sztuczna inteligencja**

Projekt zawiera:
- ✅ **27 testów statystycznych** (kod źródłowy Python)
- ✅ **55 plików JSON** z wynikami analizy 10B cyfr Pi
- ✅ **Raporty naukowe** (PDF) - po 70+ stron każdy
- ✅ **Wzory matematyczne** - kompletna dokumentacja
- ✅ **Przyspieszenie GPU** (CuPy dla NVIDIA RTX)
- ✅ **Przetwarzanie strumieniowe** - przetwarzanie 10B cyfr partiami
- ✅ **Komponenty AI/ML** - sieci neuronowe LSTM do przewidywania wzorców i analizy

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

## 🔗 Linki

- 🌿 **Gałąź OMNIS2:** [https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- 📦 **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- 📦 **Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)

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

## 🗺️ Plan Działania

### ✅ Ukończone
- ✅ Analiza 10 miliardów cyfr Pi
- ✅ Implementacja 27 testów statystycznych
- ✅ Przyspieszenie GPU z CuPy
- ✅ Raporty naukowe (Polski & Angielski)
- ✅ Sieci neuronowe LSTM do przewidywania wzorców

### 🚀 W Trakcie
- 🔄 Optymalizacja algorytmów testowych
- 🔄 Ulepszone narzędzia wizualizacji
- 🔄 Rozwój API do analizy zdalnej

### 📅 Planowane
- 📋 **Analiza 1 Biliona (1T) cyfr** - Mój następny główny kamień milowy
- 📋 Dashboard analizy w czasie rzeczywistym
- 📋 Ulepszenia modeli machine learning
- 📋 Wsparcie dla obliczeń rozproszonych
- 📋 Interfejs webowy do interaktywnej analizy

## ❓ FAQ

### P: Dlaczego analizować cyfry Pi?
**O:** Rozkład cyfr Pi to fundamentalne pytanie w teorii liczb i kryptografii. Zrozumienie jego właściwości losowości ma implikacje dla zastosowań kryptograficznych i badań matematycznych.

### P: Jak długo trwała analiza 10B?
**O:** Analiza 10 miliardów cyfr zajęła około **1-1.5 godziny** przy użyciu przyspieszenia GPU na sprzęcie NVIDIA RTX 4060 Ti 16GB. Bez GPU zajęłoby to około 5 godzin.

### P: Czy mogę użyć tego do własnych badań?
**O:** Tak! Ten projekt jest open source na licencji MIT. Możesz swobodnie używać, modyfikować i współtworzyć.

### P: Jaki jest następny krok?
**O:** Moim celem jest przeanalizowanie **1 biliona cyfr** po przecinku, co zapewni jeszcze głębsze wglądy we właściwości statystyczne Pi.

### P: Jak mogę współtworzyć?
**O:** Zobacz moje [Wytyczne Współtworzenia](CONTRIBUTING.md) lub otwórz issue, aby przedyskutować swoje pomysły!

## 📖 Cytowanie

Jeśli używasz tego projektu w swoich badaniach, proszę zacytuj:

```bibtex
@software{omnis2_pi_analysis,
  author = {baver},
  title = {OMNIS2: Statistical Analysis of 10 Billion Digits of Pi},
  year = {2026},
  url = {https://github.com/Baver1022/omnis2-pi-analysis},
  version = {1.0.0}
}
```

## 🤝 Współtworzenie

Wkład jest mile widziany! Możesz przesłać Pull Request. W przypadku większych zmian, proszę najpierw otwórz issue, aby przedyskutować, co chciałbyś zmienić.

1. Sforkuj repozytorium
2. Utwórz gałąź funkcji (`git checkout -b feature/AmazingFeature`)
3. Zatwierdź swoje zmiany (`git commit -m 'Add some AmazingFeature'`)
4. Wypchnij do gałęzi (`git push origin feature/AmazingFeature`)
5. Otwórz Pull Request

Zobacz [CONTRIBUTING.md](CONTRIBUTING.md) dla szczegółowych wytycznych.

## 💬 Wsparcie

- 📧 **Issues:** [GitHub Issues](https://github.com/Baver1022/omnis2-pi-analysis/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/Baver1022/omnis2-pi-analysis/discussions)
- 📖 **Dokumentacja:** Zobacz [Gałąź OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)

## 👤 Autor

Projekt analizy statystycznej Pi - część baver

## 📄 Licencja

Zobacz plik LICENSE w gałęzi [OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2).

---

## 🌟 Oznacz Gwiazdką To Repozytorium

Jeśli uważasz ten projekt za interesujący lub użyteczny, rozważ nadanie mu ⭐ gwiazdki! Pomaga to innym odkryć projekt i wspiera dalszy rozwój.

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Baver1022/omnis2-pi-analysis&type=Date)](https://star-history.com/#Baver1022/omnis2-pi-analysis&Date)

</div>

## 📈 Statystyki Projektu

<div align="center">

![GitHub watchers](https://img.shields.io/github/watchers/Baver1022/omnis2-pi-analysis?style=social)
![GitHub stars](https://img.shields.io/github/stars/Baver1022/omnis2-pi-analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/Baver1022/omnis2-pi-analysis?style=social)
![GitHub issues](https://img.shields.io/github/issues/Baver1022/omnis2-pi-analysis?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Baver1022/omnis2-pi-analysis?style=flat-square)

</div>

---

<div align="center">

**💡 Wszystkie pliki projektu, kod źródłowy, raporty i wyniki badań znajdują się w gałęzi [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

Stworzone z ❤️ dla matematyki i nauki

</div>

