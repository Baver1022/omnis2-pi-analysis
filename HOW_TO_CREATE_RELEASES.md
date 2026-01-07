# 📦 Jak utworzyć Release na GitHubie (ręcznie)

## Krok 1: Utwórz tag (jeśli jeszcze nie istnieje)

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Krok 2: Przejdź do GitHub Releases

1. Otwórz repozytorium: https://github.com/Baver1022/omnis2-pi-analysis
2. Kliknij **"Releases"** (z boku, obok "Packages")
3. Kliknij **"Create a new release"**

## Krok 3: Wypełnij formularz

- **Choose a tag**: Wybierz `v1.0.0` (lub utwórz nowy)
- **Release title**: `OMNIS2 Pi Analysis v1.0.0`
- **Describe this release**: Skopiuj poniższy tekst:

```markdown
# OMNIS2 Pi Analysis v1.0.0

## 🎉 Initial Release

First stable release of OMNIS2 Pi Analysis - comprehensive statistical analysis tool for Pi digits.

## ✨ Features

- **27 Statistical Tests**: Complete implementation of NIST Statistical Test Suite (17 tests) and TestU01 SmallCrush (10 tests)
- **Large-Scale Analysis**: Processes up to 10 billion digits efficiently
- **GPU Acceleration**: Optional CUDA support for FFT-based tests
- **Comprehensive Reporting**: Generates detailed JSON results with interpretations
- **Modular Architecture**: Each test implemented as a separate step for easy maintenance

## 📊 Analysis Results Included

- Analysis of 10 billion Pi digits
- 55 JSON files with detailed test results
- Scientific reports (PDF) - 70+ pages each (Polish and English)
- Mathematical formulas documentation

## 📦 Installation

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
cd Program
pip install -r requirements.txt
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## 📚 Documentation

- **Main README**: See repository README.md
- **Program Documentation**: See Program/README.md
- **Scientific Reports**: See Raporty/ directory

## 📄 License

MIT License - see LICENSE file for details
```

- **Attach binaries** (opcjonalnie): Możesz załączyć archiwa ZIP/TAR.GZ z kodem źródłowym

## Krok 4: Opublikuj

Kliknij **"Publish release"**

---

**Gotowe!** Release będzie widoczny w sekcji "Releases" z boku repozytorium.

