# 🔬 OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Liczby Pi

## 📊 O Projekcie

**OMNIS2** to kompleksowy projekt analizy statystycznej **10 miliardów cyfr liczby Pi** przy użyciu **27 testów statystycznych** (17 testów NIST + 10 testów SmallCrush) z akceleracją GPU.

Projekt zawiera:
- ✅ **27 testów statystycznych** (kod źródłowy Python)
- ✅ **55 plików JSON** z wynikami analizy 10B cyfr Pi
- ✅ **Raporty naukowe** (PDF) - 70+ stron każdy
- ✅ **Wzory matematyczne** - kompletna dokumentacja
- ✅ **Akceleracja GPU** (CuPy dla NVIDIA RTX)
- ✅ **Streaming processing** - przetwarzanie 10B cyfr batch-by-batch

## 📈 Wyniki Analizy

Analiza 10 miliardów cyfr Pi wykazała:

- ✅ **~70% testów PASS** - podstawowe testy potwierdzają lokalną losowość
- ⚠️ **Krytyczne FAIL** w testach Random Excursions (13, 14) i niektórych SmallCrush
- 📊 **Entropia**: H ≈ 3.32 (blisko maksimum dla systemu dziesiętnego)
- 📈 **Kompresja**: R ≈ 0.47 (wysoka nieprzewidywalność)

## 🌿 Główny Projekt - Branch OMNIS2

**Wszystkie pliki projektu znajdują się w branchu [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

### Struktura projektu w branchu OMNIS2:

```
OMNIS2/
├── analysis_orchestrator.py      # Główny orchestrator analizy
├── analysis_steps/               # 27 modułów testów statystycznych
├── Raporty/                      # Raporty naukowe (PDF)
│   ├── RAPORT_NAUKOWY_PI.pdf
│   ├── RAPORT_NAUKOWY_PI_EN.pdf
│   └── WZORY_MATEMATYCZNE_27_TESTOW.pdf
├── dane_z_windows/               # Wyniki badań
│   └── Analiza_10B/             # 55 plików JSON z wynikami
└── README.md                     # Pełna dokumentacja
```

**[👉 Przejdź do brancha OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

## 🚀 Szybki Start

### Pobierz pełny projekt:

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

- **📖 Pełna dokumentacja:** [Branch OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **📄 Raporty naukowe:** W katalogu `Raporty/` (w OMNIS2)
- **📐 Wzory matematyczne:** `WZORY_MATEMATYCZNE_27_TESTOW.pdf` (w OMNIS2)
- **📊 Wyniki badań:** 55 plików JSON w `dane_z_windows/Analiza_10B/` (w OMNIS2)

## 🔗 Linki

- 🌿 **Branch OMNIS2:** [https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- 📦 **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- 📦 **Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)

## 👤 Autor

Projekt analizy statystycznej liczby Pi - część baver

## 📄 Licencja

Zobacz plik LICENSE w branchu [OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2).

---

<div align="center">

**💡 Wszystkie pliki projektu, kod źródłowy, raporty i wyniki badań znajdują się w branchu [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

</div>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        