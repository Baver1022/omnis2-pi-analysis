# Changelog

Wszystkie znaczące zmiany w projekcie OMNIS2 będą dokumentowane w tym pliku.

Format oparty na [Keep a Changelog](https://keepachangelog.com/pl/1.0.0/),
a projekt używa [Semantic Versioning](https://semver.org/lang/pl/).

## [1.0.0] - 2026-01-07

### Dodane
- ✅ 27 testów statystycznych (17 NIST + 10 SmallCrush)
- ✅ Analiza 10 miliardów cyfr liczby Pi
- ✅ Generatory raportów naukowych w LaTeX (PL i EN)
- ✅ 55 plików JSON z wynikami analizy
- ✅ Dokumentacja matematyczna (PDF z wzorami)
- ✅ Wizualizacje wyników (wykresy p-values, entropii, czasów wykonania)
- ✅ Akceleracja GPU (CuPy dla NVIDIA RTX)
- ✅ Streaming processing dla dużych plików
- ✅ Checkpointing - automatyczne zapisywanie wyników
- ✅ Remote monitoring

### Wyniki Analizy
- ✅ ~70% testów PASS - podstawowe testy potwierdzają lokalną losowość
- ⚠️ Krytyczne FAIL w testach Random Excursions (13, 14) i niektórych SmallCrush
- 📊 Entropia: H ≈ 3.32 (blisko maksimum dla systemu dziesiętnego)
- 📈 Kompresja: R ≈ 0.47 (wysoka nieprzewidywalność)

### Dokumentacja
- README.md z pełną dokumentacją projektu
- WZORY_MATEMATYCZNE_27_TESTOW.pdf - wzory matematyczne wszystkich testów
- Raporty naukowe (70+ stron każdy) w języku polskim i angielskim

### Techniczne
- Python 3.8+ compatibility
- Modularna architektura (27 modułów testów)
- Konfiguracja przez .gitignore i requirements.txt
- Względne ścieżki w skryptach (przenośność)

[1.0.0]: https://github.com/Baver1022/omnis2-pi-analysis/releases/tag/v1.0.0

