# OMNIS2 Pi Analysis - Release Notes

## Version 1.0.0 (2026-01-07)

### 🎉 Initial Release

First stable release of OMNIS2 Pi Analysis - comprehensive statistical analysis tool for Pi digits.

### ✨ Features

- **27 Statistical Tests**: Complete implementation of NIST Statistical Test Suite (17 tests) and TestU01 SmallCrush (10 tests)
- **Large-Scale Analysis**: Processes up to 10 billion digits efficiently
- **GPU Acceleration**: Optional CUDA support for FFT-based tests
- **Comprehensive Reporting**: Generates detailed JSON results with interpretations
- **Modular Architecture**: Each test implemented as a separate step for easy maintenance

### 📊 Analysis Results Included

- Analysis of 10 billion Pi digits
- 55 JSON files with detailed test results
- Scientific reports (PDF) - 70+ pages each (Polish and English)
- Mathematical formulas documentation

### 📦 Package Contents

#### Source Code Release
- Complete Python source code
- 27 statistical test modules
- Analysis orchestrator
- Documentation (README.md)
- Requirements file

#### Scientific Reports
- `RAPORT_Z_ANALIZY_PI.pdf` - Polish scientific report (40+ pages)
- `RAPORT_Z_ANALIZY_PI_EN.pdf` - English scientific report (40+ pages)
- `WZORY_MATEMATYCZNE_27_TESTOW.pdf` - Mathematical formulas documentation

#### Research Results
- 55 JSON files with analysis results
- Complete statistical test outputs
- Analysis summaries

### 🔧 Installation

#### From Source
```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
cd Program
pip install -r requirements.txt
```

#### From Package (Python)
```bash
pip install omnis2-pi-analysis
```

### 📚 Documentation

- **Main README**: `README.md`
- **Program Documentation**: `Program/README.md`
- **Scientific Reports**: `Raporty/`

### 🐛 Known Issues

- GPU acceleration requires CUDA-compatible NVIDIA GPU
- Large file processing (10B digits) requires significant RAM

### 🙏 Acknowledgments

- NIST Statistical Test Suite
- TestU01 SmallCrush
- All contributors and researchers in the field

### 📄 License

MIT License - see LICENSE file for details

---

**Download**: [GitHub Releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
**Documentation**: [OMNIS2 Branch](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)

