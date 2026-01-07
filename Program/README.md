# OMNIS2 Pi Analysis Program

## 📋 Overview

This program performs comprehensive statistical analysis of Pi digits using 27 statistical tests from NIST Statistical Test Suite and TestU01 SmallCrush. It analyzes up to 10 billion digits of Pi to evaluate their statistical properties and randomness characteristics.

## 🎯 Features

- **27 Statistical Tests**: Complete NIST STS (17 tests) and TestU01 SmallCrush (10 tests)
- **Large-Scale Analysis**: Processes up to 10 billion digits efficiently
- **GPU Acceleration**: Optional CUDA support for FFT-based tests
- **Comprehensive Reporting**: Generates detailed JSON results with interpretations
- **Modular Architecture**: Each test implemented as a separate step for easy maintenance

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip package manager
- (Optional) NVIDIA CUDA-compatible GPU for FFT tests

### Install Dependencies

```bash
cd Program
pip install -r requirements.txt
```

### Required Packages

- `numpy>=1.21.0` - Numerical computations
- `scipy>=1.7.0` - Statistical functions
- `matplotlib>=3.4.0` - Data visualization
- `torch>=1.9.0` - GPU acceleration (optional)

## 🚀 Usage

### Basic Usage

```bash
cd Program
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

### Command Line Options

```bash
python3 analysis_orchestrator.py [OPTIONS]

Options:
  --pi-file PATH     Path to Pi digits file (required)
  --output-dir PATH  Output directory for results (default: ../Dane z analizy/Analiza_10B)
  --steps-dir PATH   Directory containing analysis steps (default: analysis_steps)
  --verbose          Enable verbose output
  --gpu              Enable GPU acceleration (if available)
```

### Example

```bash
# Analyze 10 billion digits
python3 analysis_orchestrator.py --pi-file /path/to/pi_10billion.txt

# With custom output directory
python3 analysis_orchestrator.py \
  --pi-file pi_10billion.txt \
  --output-dir ../results/custom_analysis
```

## 📊 Statistical Tests

### NIST Statistical Test Suite (17 tests)

1. **Frequency Test** - Tests the proportion of zeros and ones
2. **Block Frequency Test** - Tests the proportion of ones within M-bit blocks
3. **Runs Test** - Tests the total number of runs in the sequence
4. **Longest Run Test** - Tests the longest run of ones within M-bit blocks
5. **Binary Matrix Rank Test** - Tests for linear dependence among fixed length substrings
6. **Discrete Fourier Transform Test** - Tests for periodic features
7. **Non-overlapping Template Matching Test** - Tests the number of occurrences of pre-specified target strings
8. **Overlapping Template Matching Test** - Tests the number of occurrences of pre-specified target strings
9. **Maurer's Universal Statistical Test** - Tests the number of bits between matching patterns
10. **Linear Complexity Test** - Tests the length of a linear feedback shift register
11. **Serial Test** - Tests the frequency of all possible overlapping m-bit patterns
12. **Approximate Entropy Test** - Tests the frequency of all possible overlapping m-bit patterns
13. **Cumulative Sums Test** - Tests the cumulative sums of the partial sequences
14. **Random Excursions Test** - Tests the number of cycles having exactly K visits in a cumulative sum random walk
15. **Random Excursions Variant Test** - Tests the total number of times that a particular state is visited
16. **Compression Test** - Tests the compressibility of the sequence
17. **Entropy Analysis** - Tests the Shannon entropy of the sequence

### TestU01 SmallCrush (10 tests)

18. **BirthdaySpacings** - Tests the distribution of spacings between birthdays
19. **Collision** - Tests the number of collisions in a hash table
20. **Gap** - Tests the distribution of gaps between occurrences
21. **SimplePoker** - Tests the distribution of poker hands
22. **CouponCollector** - Tests the number of coupons needed to collect all types
23. **MaxOft** - Tests the distribution of maximum values
24. **WeightDistrib** - Tests the distribution of weights
25. **MatrixRank** - Tests the rank of random matrices
26. **HammingIndep** - Tests the Hamming distance between blocks
27. **RandomWalk1** - Tests the distribution of random walk positions

## 📁 Project Structure

```
Program/
├── analysis_orchestrator.py  # Main orchestrator script
├── analysis_steps/           # Individual test implementations
│   ├── 01_frequency_test.py
│   ├── 02_runs_test.py
│   ├── ...
│   └── 27_random_walk1.py
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 📈 Output Format

The program generates JSON files for each test with the following structure:

```json
{
  "test_id": "01",
  "test_name": "Frequency Test",
  "status": "completed",
  "p_value": 0.5234,
  "result": "PASS",
  "interpretation": "The sequence passes the frequency test...",
  "statistics": {
    "chi_square": 0.4123,
    "degrees_of_freedom": 1
  }
}
```

Results are saved in: `../Dane z analizy/Analiza_10B/`

## 🔧 Advanced Configuration

### GPU Acceleration

For FFT-based tests, GPU acceleration can significantly speed up computation:

```bash
python3 analysis_orchestrator.py --pi-file pi_10billion.txt --gpu
```

**Note**: Requires CUDA-compatible NVIDIA GPU and PyTorch with CUDA support.

### Custom Analysis Steps

You can add custom analysis steps by creating new Python files in `analysis_steps/` following the naming convention: `XX_test_name.py`

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'numpy'`
- **Solution**: Install dependencies: `pip install -r requirements.txt`

**Issue**: `FileNotFoundError: pi_10billion.txt`
- **Solution**: Provide correct path to Pi digits file using `--pi-file` option

**Issue**: Out of memory errors
- **Solution**: Process smaller chunks or use a machine with more RAM

**Issue**: GPU not detected
- **Solution**: Install PyTorch with CUDA support or run without `--gpu` flag

## 📚 Documentation

- **Main Project README**: `../README.md`
- **Scientific Reports**: `../Raporty/`
- **Analysis Results**: `../Dane z analizy/`

## 👤 Author

**baver** - Statistical Analysis of Pi Digits

## 📄 License

See `../LICENSE` for license information.

## 🔗 Links

- **GitHub Repository**: https://github.com/Baver1022/omnis2-pi-analysis
- **OMNIS2 Branch**: https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2

