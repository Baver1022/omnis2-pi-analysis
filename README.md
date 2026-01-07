# 📊 OMNIS2 - Analiza Statystyczna Liczby Pi

## 🎯 O Projekcie

**OMNIS2** to kompleksowy projekt analizy statystycznej **10 miliardów cyfr liczby Pi** przy użyciu **27 testów statystycznych** (17 testów NIST + 10 testów SmallCrush) z akceleracją GPU.

## 📄 Raporty z Analizy

### 📑 Dostępne Raporty

W katalogu `analiza_wynikow_output/` znajdują się szczegółowe raporty z analizy:

| Raport | Opis | Format |
|--------|------|--------|
| 📊 **RAPORT_Z_ANALIZY_PI.pdf** | Raport naukowy w języku polskim (70+ stron) | PDF |
| 📊 **RAPORT_Z_ANALIZY_PI_EN.pdf** | Raport naukowy w języku angielskim (70+ stron) | PDF |
| 📝 **RAPORT_Z_ANALIZY_PI.tex** | Źródło LaTeX raportu PL | LaTeX |
| 📝 **RAPORT_Z_ANALIZY_PI_EN.tex** | Źródło LaTeX raportu EN | LaTeX |

### 🔍 Co zawierają raporty:

- ✅ Wprowadzenie teoretyczne
- ✅ Opis 27 testów statystycznych z wzorami matematycznymi
- ✅ Szczegółowe wyniki i interpretacje
- ✅ Wizualizacje (wykresy p-values, entropii, czasów wykonania)
- ✅ Analizę porównawczą z innymi badaniami
- ✅ Sekcję zastosowań kryptograficznych
- ✅ Wnioski i granice losowości

## 🔬 Główny Projekt

**Wszystkie pliki projektu, kod źródłowy i wyniki badań znajdują się w branchu [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

### Co znajdziesz w branchu OMNIS2:

- ✅ **27 testów statystycznych** (kod źródłowy Python)
- ✅ **55 plików JSON** z wynikami analizy 10B cyfr Pi
- ✅ **Główny orchestrator** analizy (`analysis_orchestrator.py`)
- ✅ **Dokumentacja** (README, wzory matematyczne PDF)
- ✅ **Instrukcje instalacji i użycia**
- ✅ **Struktura packages** dla Releases i Packages

## 📈 Wyniki Analizy

Analiza 10 miliardów cyfr Pi wykazała:

- ✅ **~70% testów PASS** - podstawowe testy potwierdzają lokalną losowość
- ⚠️ **Krytyczne FAIL** w testach Random Excursions (13, 14) i niektórych SmallCrush
- 📊 **Entropia**: H ≈ 3.32 (blisko maksimum dla systemu dziesiętnego)
- 📈 **Kompresja**: R ≈ 0.47 (wysoka nieprzewidywalność)

## 🚀 Szybki Start

### Pobierz raporty (ten branch - main):

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
# Raporty są w katalogu analiza_wynikow_output/
ls analiza_wynikow_output/*.pdf
```

### Pobierz pełny projekt (branch OMNIS2):

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2

# Zainstaluj zależności
pip install -r requirements.txt

# Uruchom analizę
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## 📚 Dokumentacja

- **📄 Raporty PDF:** W katalogu `analiza_wynikow_output/` (ten branch)
- **📖 Pełna dokumentacja:** [Branch OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **📐 Wzory matematyczne:** `WZORY_MATEMATYCZNE_27_TESTOW.pdf` (w OMNIS2)
- **📊 Wyniki badań:** 55 plików JSON w `dane_z_windows/Analiza_10B/` (w OMNIS2)

## 🔗 Linki

- **🌿 Branch OMNIS2:** [https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **📦 Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- **📚 Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)

## 👤 Autor

Projekt analizy statystycznej liczby Pi - część baver

## 📄 Licencja

Zobacz plik LICENSE w branchu [OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2).

---

**💡 Wskazówka:** Aby zobaczyć kod źródłowy, wyniki badań i pełną dokumentację, przełącz się na branch [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2).
