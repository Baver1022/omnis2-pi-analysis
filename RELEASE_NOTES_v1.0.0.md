# OMNIS2 Pi Analysis v1.0.0

## 🎉 Initial Release

Pierwsza stabilna wersja OMNIS2 Pi Analysis - narzędzie do kompleksowej analizy statystycznej cyfr Pi.

## ✨ Features

- **27 Testów Statystycznych**: Pełna implementacja NIST Statistical Test Suite (17 testów) i TestU01 SmallCrush (10 testów)
- **Analiza na Dużą Skalę**: Przetwarza do 10 miliardów cyfr efektywnie
- **Przyspieszenie GPU**: Opcjonalne wsparcie CUDA dla testów opartych na FFT
- **Szczegółowe Raportowanie**: Generuje szczegółowe wyniki JSON z interpretacjami
- **Modułowa Architektura**: Każdy test zaimplementowany jako osobny krok dla łatwej konserwacji

## 📊 Wyniki Analizy Zawarte

- Analiza 10 miliardów cyfr Pi
- 55 plików JSON ze szczegółowymi wynikami testów
- Raporty naukowe (PDF) - 70+ stron każdy (polski i angielski)
- Dokumentacja wzorów matematycznych

## 📦 Instalacja

### Z plików Release:
```bash
# Pobierz pliki .whl lub .tar.gz z Release
pip install omnis2_pi_analysis-1.0.0-py3-none-any.whl
```

### Z kodu źródłowego:
```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
cd Program
pip install -r requirements.txt
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## 📚 Dokumentacja

- **Główny README**: Zobacz README.md w repozytorium
- **Dokumentacja Programu**: Zobacz Program/README.md
- **Raporty Naukowe**: Zobacz Raporty/ katalog

## 📄 Licencja

MIT License - zobacz plik LICENSE dla szczegółów

## 👤 Autor

baver
