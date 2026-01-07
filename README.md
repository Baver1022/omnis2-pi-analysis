# 🔬 OMNIS2 - Statistical Analysis of 10 Billion Digits of Pi

## 📊 About the Project

**OMNIS2** is a comprehensive project for statistical analysis of **10 billion digits of Pi** using **27 statistical tests** (17 NIST tests + 10 SmallCrush tests) with GPU acceleration.

The project includes:
- ✅ **27 statistical tests** (Python source code)
- ✅ **55 JSON files** with analysis results of 10B Pi digits
- ✅ **Scientific reports** (PDF) - 70+ pages each
- ✅ **GPU acceleration** (CuPy for NVIDIA RTX)
- ✅ **Streaming processing** - processing 10B digits batch-by-batch

## 📈 Analysis Results

Analysis of 10 billion Pi digits revealed:

- ✅ **~70% tests PASS** - basic tests confirm local randomness
- ⚠️ **Critical FAIL** in Random Excursions tests (13, 14) and some SmallCrush tests
- 📊 **Entropy**: H ≈ 3.32 (close to maximum for decimal system)
- 📈 **Compression**: R ≈ 0.47 (high unpredictability)

## 📁 Project Structure

```
OMNIS2/
├── Program/                      # Main program
│   ├── analysis_orchestrator.py  # Main analysis orchestrator
│   ├── analysis_steps/           # 27 statistical test modules
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # Program documentation
├── Raporty/                      # Scientific reports (PDF)
│   ├── RAPORT_Z_ANALIZY_PI.pdf
│   └── RAPORT_Z_ANALIZY_PI_EN.pdf
├── Dane z analizy/               # Research results
│   └── *.json                    # 55 JSON files with results
├── README.md                     # This file
└── LICENSE                       # MIT License
```

## 🚀 Quick Start

### Installation:

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2

# Install dependencies
cd Program
pip install -r requirements.txt
```

### Run Analysis:

```bash
# From Program/ directory
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

## 📚 Documentation

### 📄 Scientific Reports

<div align="center">

| 📊 Report | 🌐 Language | 📥 Download | 📄 Description |
|:---------:|:--------:|:---------:|:-------:|
| **RAPORT_Z_ANALIZY_PI.pdf** | 🇵🇱 Polish | [📥 Download PDF](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI.pdf) | Comprehensive scientific report (40+ pages) with complete statistical analysis |
| **RAPORT_Z_ANALIZY_PI_EN.pdf** | 🇬🇧 English | [📥 Download PDF](https://github.com/Baver1022/omnis2-pi-analysis/raw/OMNIS2/Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) | Full scientific report (40+ pages) with complete statistical analysis |

</div>

#### 📋 Scientific Reports Content

**RAPORT_Z_ANALIZY_PI.pdf** (Polish) contains:
- 📖 Theoretical introduction
- 🔬 Detailed description of all 27 statistical tests
- 📐 Mathematical formulas for each test
- 📊 Results and statistical interpretations
- 📈 Charts and result tables
- 🔍 Comparative analysis with other studies
- 💡 Conclusions and cryptographic applications
- 📚 Bibliography and references

**RAPORT_Z_ANALIZY_PI_EN.pdf** (English) contains:
- 📖 Theoretical introduction
- 🔬 Detailed description of all 27 statistical tests
- 📐 Mathematical formulas for each test
- 📊 Results and statistical interpretations
- 📈 Charts and result tables
- 🔍 Comparative analysis with other studies
- 💡 Conclusions and cryptographic applications
- 📚 Bibliography and references

### 📖 Research Results

- **📊 Analysis results:** 55 JSON files in `Dane z analizy/` directory
- **📄 Program documentation:** See `Program/README.md`

## 🔗 Links

- 🌿 **Main Branch:** [https://github.com/Baver1022/omnis2-pi-analysis](https://github.com/Baver1022/omnis2-pi-analysis)
- 📦 **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
- 📦 **Packages:** [https://github.com/Baver1022/omnis2-pi-analysis/packages](https://github.com/Baver1022/omnis2-pi-analysis/packages)

## 👤 Author

Pi statistical analysis project - part of baver

## 📄 License

MIT License - see LICENSE file for details
