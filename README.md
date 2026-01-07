# 🔬 OMNIS2 - Statistical Analysis of 10 Billion Digits of Pi

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![GPU](https://img.shields.io/badge/GPU-CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![GitHub](https://img.shields.io/github/stars/Baver1022/omnis2-pi-analysis?style=for-the-badge&logo=github)
![GitHub forks](https://img.shields.io/github/forks/Baver1022/omnis2-pi-analysis?style=for-the-badge&logo=github)

**🔬 Comprehensive statistical analysis of 10 billion Pi digits using 27 rigorous tests**

[📖 Documentation](#-documentation) • [🚀 Quick Start](#-quick-start) • [📊 Results](#-analysis-results) • [📄 Reports](#-scientific-reports)

</div>

## 🌟 What Fascinates Us

What drives us in this project? The **mystery of randomness** hidden in the infinite sequence of Pi digits. Is Pi truly random, or does it contain hidden patterns? Can we trust it for cryptographic applications? These questions led us to conduct one of the most comprehensive statistical analyses of Pi digits ever performed.

We analyzed **10 billion digits** using **27 rigorous statistical tests** - a journey that revealed both expected randomness and surprising anomalies. This is just the beginning - **our next goal is to analyze 1 trillion (1T) digits after the decimal point**, pushing the boundaries of computational statistics and exploring the deepest secrets of this mathematical constant.

## 📊 About the Project

**OMNIS2** is a comprehensive project for statistical analysis of **10 billion digits of Pi** using **27 statistical tests** (17 NIST tests + 10 SmallCrush tests) with GPU acceleration.

> **Keywords:** Pi digits analysis, statistical randomness testing, NIST tests, SmallCrush, GPU computing, cryptography, number theory, mathematical constants, data science, Python, CuPy, statistical analysis, randomness validation, Pi research, computational mathematics, **AI, machine learning, deep learning, neural networks, pattern recognition, data analysis, artificial intelligence**

The project includes:
- ✅ **27 statistical tests** (Python source code)
- ✅ **55 JSON files** with analysis results of 10B Pi digits
- ✅ **Scientific reports** (PDF) - 70+ pages each
- ✅ **Mathematical formulas** - complete documentation
- ✅ **GPU acceleration** (CuPy for NVIDIA RTX)
- ✅ **Streaming processing** - processing 10B digits batch-by-batch

## 📈 Analysis Results

Analysis of 10 billion Pi digits revealed:

- ✅ **~70% tests PASS** - basic tests confirm local randomness
- ⚠️ **Critical FAIL** in Random Excursions tests (13, 14) and some SmallCrush tests
- 📊 **Entropy**: H ≈ 3.32 (close to maximum for decimal system)
- 📈 **Compression**: R ≈ 0.47 (high unpredictability)

## 🌿 Main Project - OMNIS2 Branch

**All project files are located in the [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2) branch**

### Project structure in OMNIS2 branch:

```
OMNIS2/
├── Program/                      # Main program
│   ├── analysis_orchestrator.py  # Main analysis orchestrator
│   ├── analysis_steps/           # 27 statistical test modules
│   └── requirements.txt          # Python dependencies
├── Raporty/                      # Scientific reports (PDF)
│   ├── RAPORT_Z_ANALIZY_PI.pdf
│   └── RAPORT_Z_ANALIZY_PI_EN.pdf
├── Dane z analizy/               # Research results
│   └── *.json                    # 55 JSON files with results
└── README.md                     # Full documentation
```

**[👉 Go to OMNIS2 branch](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**

## 🚀 Quick Start

### Option 1: Install from GitHub Packages (Recommended)

```bash
# Install the package
pip install omnis2-pi-analysis

# Run analysis
python3 -m omnis2_pi_analysis.analysis_orchestrator --pi-file pi_10billion.txt
```

### Option 2: Download the full project:

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2

# Install dependencies
cd Program
pip install -r requirements.txt

# Run analysis
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## 📚 Documentation

### 📄 Scientific Reports

Both reports contain comprehensive analysis of 10 billion Pi digits using 27 statistical tests, including:

- 📖 **Theoretical introduction** - mathematical foundations and test methodology
- 🔬 **Detailed description** of all 27 statistical tests (17 NIST + 10 SmallCrush)
- 📐 **Mathematical formulas** - complete formulas and test procedures
- 📊 **Results and interpretations** - statistical analysis and significance testing
- 📈 **Charts and tables** - visualizations of test results
- 🔍 **Comparative analysis** - comparison with previous studies
- 💡 **Conclusions** - implications for cryptography and number theory
- 📚 **Bibliography** - complete references and citations

<div align="center">

| | 🇵🇱 Polish | 🇬🇧 English |
|:---:|:---:|:---:|
| **📄 Report** | [RAPORT_Z_ANALIZY_PI.pdf](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [RAPORT_Z_ANALIZY_PI_EN.pdf](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |
| **📊 Pages** | 40+ | 40+ |
| **📥 Download** | [📥 PDF](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [📥 PDF](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |

</div>

### 📖 Other Materials

- **📖 Full documentation:** [OMNIS2 Branch](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- **📊 Research results:** 55 JSON files in `OMNIS2/Dane z analizy/`

## 📦 Package Installation

The project is available as a Python package on **GitHub Packages**:

```bash
pip install omnis2-pi-analysis
```

**Package Details:**
- 📦 **Name:** `omnis2-pi-analysis`
- 📌 **Version:** `1.0.0`
- 🔗 **GitHub Packages:** [View Package](https://github.com/Baver1022/omnis2-pi-analysis/packages)
- 📚 **Documentation:** See [OMNIS2 Branch](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)

## 🔗 Links

- 🌿 **OMNIS2 Branch:** [https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)
- 📦 **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- 📦 **Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)

## 👤 Author

Pi statistical analysis project - part of baver

## 📄 License

See LICENSE file in the [OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2) branch.

---

## 🌟 Star This Repository

If you find this project interesting or useful, please consider giving it a ⭐ star! It helps others discover the project and supports continued development.

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Baver1022/omnis2-pi-analysis&type=Date)](https://star-history.com/#Baver1022/omnis2-pi-analysis&Date)

</div>

## 📈 Project Statistics

<div align="center">

![GitHub watchers](https://img.shields.io/github/watchers/Baver1022/omnis2-pi-analysis?style=social)
![GitHub stars](https://img.shields.io/github/stars/Baver1022/omnis2-pi-analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/Baver1022/omnis2-pi-analysis?style=social)
![GitHub issues](https://img.shields.io/github/issues/Baver1022/omnis2-pi-analysis?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Baver1022/omnis2-pi-analysis?style=flat-square)

</div>

---

<div align="center">

**💡 All project files, source code, reports, and research results are located in the [`OMNIS2`](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2) branch**

Made with ❤️ for mathematics and science

</div>
