# OMNIS2 - Analiza Statystyczna Liczby Pi

## O Projekcie

OMNIS2 to kompleksowy projekt analizy statystycznej 10 miliardów cyfr liczby Pi przy użyciu 27 testów statystycznych (17 testów NIST + 10 testów SmallCrush) z akceleracją GPU.

## Główny Branch

**Wszystkie pliki projektu znajdują się w branchu [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

Przejdź do brancha OMNIS2, aby zobaczyć:
- ✅ 27 testów statystycznych
- ✅ Kod źródłowy (Python)
- ✅ Wyniki analizy (55 plików JSON)
- ✅ Dokumentację i wzory matematyczne
- ✅ Instrukcje użycia

## Szybki Start

```bash
# Przełącz się na branch OMNIS2
git checkout OMNIS2

# Zainstaluj zależności
pip install -r requirements.txt

# Uruchom analizę
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## Struktura Projektu

```
omnis2-pi-analysis/
├── analysis_orchestrator.py    # Główny orchestrator
├── analysis_steps/             # 27 modułów testów
├── dane_z_windows/             # Wyniki analizy (55 JSON)
├── packages/                   # Releases i Packages
└── README.md                   # Dokumentacja
```

## Wyniki

Analiza 10 miliardów cyfr Pi wykazała:
- ✅ ~70% testów PASS
- ⚠️ Krytyczne FAIL w testach Random Excursions
- 📊 Entropia: H ≈ 3.32
- 📈 Kompresja: R ≈ 0.47

## Dokumentacja

Pełna dokumentacja dostępna w branchu [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2):
- Szczegółowy README.md
- Wzory matematyczne (PDF)
- Opis wyników badań
- Instrukcje instalacji i użycia

## Licencja

Zobacz plik [LICENSE](LICENSE) w głównym katalogu projektu.

## Autor

Projekt analizy statystycznej liczby Pi - część baver

## Linki

- **Branch OMNIS2:** [https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- **Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)
