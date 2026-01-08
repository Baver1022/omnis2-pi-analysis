# 🔬 OMNIS2 - Technical Documentation & Implementation

<div align="center">

[🇵🇱 Polski](README_PL.md) • [📖 Program Documentation](Program/README.md) • [🚀 Quick Start](#-quick-start) • [📊 Results](#-detailed-results) • [📄 Reports](#-scientific-reports)

**This is the OMNIS2 branch - contains all source code, analysis results, and technical documentation**

[← Back to Main Branch](https://github.com/Baver1022/omnis2-pi-analysis)

</div>

## 📋 Overview

This branch contains the complete implementation of the OMNIS2 statistical analysis system for 10 billion Pi digits. All source code, analysis results, scientific reports, and technical documentation are located here.

## 📁 Project Structure

```
OMNIS2/
├── Program/                      # Main analysis program
│   ├── analysis_orchestrator.py # Orchestrator (manages all 27 tests)
│   ├── analysis_steps/          # Individual test implementations
│   │   ├── step_01_frequency.py
│   │   ├── step_02_runs.py
│   │   ├── step_03_block_frequency.py
│   │   ├── step_04_entropy.py
│   │   ├── step_05_spectral_fft.py    # GPU-accelerated
│   │   ├── step_06_compression.py
│   │   ├── step_07_entropy_bounds.py
│   │   ├── step_08_ml_lstm.py        # LSTM neural network
│   │   ├── step_09_cumulative_sums.py
│   │   ├── step_10_approximate_entropy.py
│   │   ├── step_11_serial.py
│   │   ├── step_12_linear_complexity.py
│   │   ├── step_13_random_excursions.py
│   │   ├── step_14_random_excursions_variant.py
│   │   ├── step_15_universal_statistical.py
│   │   ├── step_16_non_overlapping_template.py
│   │   ├── step_17_overlapping_template.py
│   │   ├── step_18_birthday_spacings.py    # SmallCrush
│   │   ├── step_19_collision.py             # SmallCrush
│   │   ├── step_20_gap.py                   # SmallCrush
│   │   ├── step_21_simple_poker.py          # SmallCrush
│   │   ├── step_22_coupon_collector.py      # SmallCrush
│   │   ├── step_23_maxoft.py                # SmallCrush
│   │   ├── step_24_weight_distrib.py        # SmallCrush
│   │   ├── step_25_matrix_rank.py           # SmallCrush
│   │   ├── step_26_hamming_indep.py         # SmallCrush
│   │   ├── step_27_random_walk1.py          # SmallCrush
│   │   ├── base_step.py                     # Base class with checkpointing
│   │   └── gpu_template.py                  # GPU acceleration template
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # Program documentation
│
├── Raporty/                      # Scientific reports (PDF)
│   ├── RAPORT_Z_ANALIZY_PI.pdf      # Polish report (40+ pages)
│   └── RAPORT_Z_ANALIZY_PI_EN.pdf   # English report (40+ pages)
│
├── Dane z analizy/               # Analysis results (JSON)
│   ├── 01_results.json           # Frequency Test results
│   ├── 01_status.json            # Frequency Test status
│   ├── 02_results.json           # Runs Test results
│   ├── ...                       # (55 JSON files total)
│   ├── 27_results.json           # Random Walk1 results
│   └── analysis_summary.json     # Complete analysis summary
│
├── README.md                     # This file
└── README_PL.md                  # Polish version
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- NVIDIA GPU with CUDA support (optional, for GPU acceleration)
- ~20-30 GB disk space for 10B digits analysis

### Installation

```bash
# Clone repository
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2

# Install dependencies
cd Program
pip install -r requirements.txt
```

### Running Analysis

```bash
# Full analysis (all 27 tests)
python3 analysis_orchestrator.py \
    --pi-file /path/to/pi_10billion.txt \
    --output-dir ../Dane\ z\ analizy \
    --max-digits 10000000000

# Run specific tests only
python3 analysis_orchestrator.py \
    --pi-file /path/to/pi_10billion.txt \
    --output-dir ../Dane\ z\ analizy \
    --steps 01 02 05  # Only Frequency, Runs, and Spectral FFT

# Check analysis status
python3 analysis_orchestrator.py \
    --pi-file /path/to/pi_10billion.txt \
    --output-dir ../Dane\ z\ analizy \
    --status
```

## 🔬 The 27 Statistical Tests

### NIST Statistical Test Suite (17 tests)

| # | Test Name | Module | Description |
|---|-----------|--------|-------------|
| 01 | Frequency Test | `step_01_frequency.py` | Tests the proportion of zeros and ones |
| 02 | Runs Test | `step_02_runs.py` | Tests the total number of runs |
| 03 | Block Frequency Test | `step_03_block_frequency.py` | Tests proportion within M-bit blocks |
| 04 | Entropy Analysis | `step_04_entropy.py` | Shannon entropy calculation |
| 05 | Spectral FFT Test | `step_05_spectral_fft.py` | GPU-accelerated FFT analysis |
| 06 | Compression Test | `step_06_compression.py` | Tests compressibility |
| 07 | Entropy Bounds | `step_07_entropy_bounds.py` | Empirical entropy bounds |
| 09 | Cumulative Sums Test | `step_09_cumulative_sums.py` | Tests cumulative sums |
| 10 | Approximate Entropy | `step_10_approximate_entropy.py` | Frequency of overlapping patterns |
| 11 | Serial Test | `step_11_serial.py` | Frequency of all m-bit patterns |
| 12 | Linear Complexity | `step_12_linear_complexity.py` | LFSR length test |
| 13 | Random Excursions | `step_13_random_excursions.py` | Number of cycles in random walk |
| 14 | Random Excursions Variant | `step_14_random_excursions_variant.py` | State visit counts |
| 15 | Universal Statistical | `step_15_universal_statistical.py` | Maurer's universal test |
| 16 | Non-overlapping Template | `step_16_non_overlapping_template.py` | Template matching |
| 17 | Overlapping Template | `step_17_overlapping_template.py` | Overlapping template matching |

### TestU01 SmallCrush (10 tests)

| # | Test Name | Module | Description |
|---|-----------|--------|-------------|
| 18 | Birthday Spacings | `step_18_birthday_spacings.py` | Distribution of spacings |
| 19 | Collision | `step_19_collision.py` | Hash table collisions |
| 20 | Gap | `step_20_gap.py` | Gap distribution |
| 21 | Simple Poker | `step_21_simple_poker.py` | Poker hand distribution |
| 22 | Coupon Collector | `step_22_coupon_collector.py` | Coupon collection test |
| 23 | MaxOft | `step_23_maxoft.py` | Maximum value distribution |
| 24 | Weight Distribution | `step_24_weight_distrib.py` | Weight distribution |
| 25 | Matrix Rank | `step_25_matrix_rank.py` | Random matrix rank |
| 26 | Hamming Independence | `step_26_hamming_indep.py` | Hamming distance |
| 27 | Random Walk1 | `step_27_random_walk1.py` | Random walk positions |

### Machine Learning Component

| # | Component | Module | Description |
|---|-----------|--------|-------------|
| 08 | LSTM Anomaly Detection | `step_08_ml_lstm.py` | Neural network pattern prediction |

## 📊 Detailed Results

### Analysis Summary

The complete analysis of 10 billion Pi digits produced:

- **55 JSON files** with detailed results for each test
- **Analysis summary** in `Dane z analizy/analysis_summary.json`
- **Individual test results** in `Dane z analizy/XX_results.json`
- **Test status** in `Dane z analizy/XX_status.json`

### Key Metrics

- **Total tests:** 27
- **Tests passed:** ~70% (19/27)
- **Tests failed:** ~30% (8/27)
- **Entropy (H):** ≈ 3.32 (99.7% of maximum 3.3219)
- **Compression ratio (R):** ≈ 0.47
- **Processing time:** ~1-1.5 hours (GPU-accelerated)

### Critical Findings

- ✅ **Frequency tests:** All passed - uniform digit distribution
- ✅ **Runs tests:** Passed - no patterns in sequences
- ✅ **Entropy:** Near maximum - high randomness
- ⚠️ **Random Excursions (13, 14):** Failed - potential long-range correlations
- ⚠️ **Some SmallCrush tests:** Failed - unexpected patterns detected

## 📄 Scientific Reports

Comprehensive scientific reports with complete methodology, formulas, and interpretations:

<div align="center">

| | 🇵🇱 Polish | 🇬🇧 English |
|:---:|:---:|:---:|
| **📄 Report** | [RAPORT_Z_ANALIZY_PI.pdf](Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [RAPORT_Z_ANALIZY_PI_EN.pdf](Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |
| **📊 Pages** | 40+ | 40+ |
| **📥 Download** | [📥 PDF](Raporty/RAPORT_Z_ANALIZY_PI.pdf) | [📥 PDF](Raporty/RAPORT_Z_ANALIZY_PI_EN.pdf) |

</div>

**Report Contents:**
- Complete theoretical background
- Detailed description of all 27 tests
- Mathematical formulas and procedures
- Comprehensive results with interpretations
- Visualizations and data tables
- Comparative analysis
- Conclusions and future directions
- Complete bibliography

## 🏗️ Architecture

### Modular Design

Each test is implemented as an independent module inheriting from `AnalysisStep`:

```python
class Step01Frequency(AnalysisStep):
    def execute(self, pi_digits):
        # Test implementation
        return results
```

### Features

- **Checkpointing:** Each step can be paused and resumed
- **Independent execution:** Run only selected tests
- **GPU acceleration:** Automatic GPU detection and usage
- **Streaming processing:** Handles large datasets efficiently
- **JSON output:** Structured results for further analysis

### GPU Acceleration

Tests with GPU support:
- `step_05_spectral_fft.py` - FFT operations on GPU
- Other tests use CPU with optional GPU optimizations

## 📈 Performance

### Execution Times (10B digits, GPU-accelerated)

- **Frequency tests:** ~9-10 min per 1B digits
- **Runs test:** ~20 min per 1B digits
- **Entropy analysis:** ~29 min per 1B digits
- **Spectral FFT (GPU):** ~15 seconds per 1B digits
- **Total for 10B:** ~1-1.5 hours

### Resource Usage

- **Peak memory:** ~1.3-2 GB (for 1B digits)
- **GPU memory:** ~2-4 GB (CuPy operations)
- **Disk space:** ~20-30 GB for full 10B analysis
- **Batch size:** 100M digits (optimized)

## 🔧 Configuration

### Command Line Options

```bash
analysis_orchestrator.py [OPTIONS]

Options:
  --pi-file PATH      Path to Pi digits file (required)
  --output-dir PATH   Output directory (default: ../Dane z analizy)
  --max-digits N      Maximum digits to analyze
  --steps XX YY ZZ    Run only specified steps
  --status            Show analysis status
  --verbose           Enable verbose output
  --gpu               Force GPU usage
```

### Output Format

Each test produces:
- `XX_results.json` - Test results with p-values, statistics
- `XX_status.json` - Execution status, timestamps
- `analysis_summary.json` - Complete summary of all tests

## 📚 Documentation

- **Program Documentation:** [Program/README.md](Program/README.md)
- **Scientific Reports:** [Raporty/](Raporty/)
- **Analysis Results:** [Dane z analizy/](Dane%20z%20analizy/)

## 🔗 Links

- **Main Branch:** [https://github.com/Baver1022/omnis2-pi-analysis](https://github.com/Baver1022/omnis2-pi-analysis)
- **Releases:** [https://github.com/Baver1022/omnis2-pi-analysis/releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)

## 👤 Author

Pi statistical analysis project - part of baver

## 📄 License

See [LICENSE](LICENSE) file.

---

<div align="center">

**💡 This branch contains all technical implementation, source code, and analysis results**

**For project overview and general information, see the [main branch](https://github.com/Baver1022/omnis2-pi-analysis)**

Made with ❤️ for mathematics and science

</div>
