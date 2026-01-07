# OMNIS2 - Comprehensive Statistical Analysis of 10 Billion Digits of π

## 📋 Project Description

OMNIS2 is an advanced statistical analysis of 10 billion digits of π, conducted using 27 statistical tests from the NIST Statistical Test Suite and TestU01 SmallCrush packages. The project's goal was to investigate the random properties of π digits on an unprecedented scale and assess their usefulness in cryptographic applications.

## 🎯 Research Objectives

1. **Randomness Verification**: Check whether π digits exhibit random properties on a large scale (10 billion digits)
2. **Statistical Analysis**: Conduct a comprehensive battery of 27 statistical tests
3. **Cryptographic Assessment**: Determine the usefulness of π digits as a source of entropy in cryptography
4. **Scientific Documentation**: Create detailed scientific reports with full methodological documentation

## 📁 Project Structure

```
OMNIS2/
├── Program/                    # Complete analysis program
│   ├── analysis_orchestrator.py    # Main analysis orchestrator
│   └── analysis_steps/             # 27 statistical test modules
│       ├── step_01_frequency.py
│       ├── step_02_runs.py
│       ├── step_03_block_frequency.py
│       ├── step_04_entropy.py
│       ├── step_05_spectral_fft.py
│       ├── step_06_compression.py
│       ├── step_07_entropy_bounds.py
│       ├── step_08_ml_lstm.py
│       ├── step_09_cumulative_sums.py
│       ├── step_10_approximate_entropy.py
│       ├── step_11_serial.py
│       ├── step_12_linear_complexity.py
│       ├── step_13_random_excursions.py
│       ├── step_14_random_excursions_variant.py
│       ├── step_15_universal_statistical.py
│       ├── step_16_non_overlapping_template.py
│       ├── step_17_overlapping_template.py
│       ├── step_18_birthday_spacings.py
│       ├── step_19_collision.py
│       ├── step_20_gap.py
│       ├── step_21_simple_poker.py
│       ├── step_22_coupon_collector.py
│       ├── step_23_maxoft.py
│       ├── step_24_weight_distrib.py
│       ├── step_25_matrix_rank.py
│       ├── step_26_hamming_indep.py
│       └── step_27_random_walk1.py
│
├── Raporty/                    # Scientific reports
│   ├── RAPORT_Z_ANALIZY_PI.pdf           # Report in Polish (40+ pages)
│   └── RAPORT_Z_ANALIZY_PI_EN.pdf        # Report in English
│
├── Dane z analizy/             # Research results (54 JSON files)
│   ├── 01_results.json         # Frequency test results
│   ├── 01_status.json         # Test execution status
│   ├── 02_results.json        # Runs test results
│   ├── 02_status.json
│   └── ...                     # (all 27 tests)
│
└── README.md                   # This file
```

## 🔬 Research Methodology

### Stage 1: Data Preparation
- **Data source**: File `pi_10billion.txt` containing 10 billion digits of π
- **Format**: Decimal digits (0-9) written sequentially
- **Verification**: Check data correctness before analysis

### Stage 2: Statistical Test Implementation

#### NIST Statistical Test Suite (17 tests):
1. **Frequency Test** - Bit frequency test
2. **Runs Test** - Runs test
3. **Block Frequency Test** - Block frequency test
4. **Entropy Analysis** - Shannon entropy analysis
5. **Spectral FFT Test** - Spectral FFT analysis (using GPU)
6. **Compression Test** - Compression test
7. **Entropy Bounds** - Entropy bounds
8. **ML LSTM Anomaly Detection** - Anomaly detection using LSTM
9. **Cumulative Sums Test** - Cumulative sums test
10. **Approximate Entropy Test** - Approximate entropy test
11. **Serial Test** - Serial test
12. **Linear Complexity Test** - Linear complexity test
13. **Random Excursions Test** - Random excursions test
14. **Random Excursions Variant Test** - Random excursions variant test
15. **Universal Statistical Test** - Universal statistical test
16. **Non-overlapping Template Matching** - Non-overlapping template matching test
17. **Overlapping Template Matching** - Overlapping template matching test

#### TestU01 SmallCrush (10 tests):
18. **BirthdaySpacings** - Birthday spacings test
19. **Collision** - Collision test
20. **Gap** - Gap test
21. **SimplePoker** - Simple poker test
22. **CouponCollector** - Coupon collector test
23. **MaxOft** - Maximum test
24. **WeightDistrib** - Weight distribution test
25. **MatrixRank** - Matrix rank test
26. **HammingIndep** - Hamming independence test
27. **RandomWalk1** - Random walk test

### Stage 3: Analysis Execution
- **Orchestration**: The `analysis_orchestrator.py` program manages sequential execution of all 27 tests
- **Processing**: Each test is executed independently with results saved to JSON files
- **Monitoring**: Status of each test is tracked and saved
- **Optimization**: GPU (CUDA) utilization for tests requiring intensive computations (FFT)

### Stage 4: Results Analysis
- **p-value interpretation**: Analysis of p-values for each test
- **Pattern detection**: Identification of subtle structures in π digits
- **Randomness comparison**: Assessment of whether results are consistent with expectations for a truly random sequence
- **Comparative analysis**: Comparison with other studies (quantum RNG, other mathematical constants)

### Stage 5: Report Generation
- **Scientific report (PL)**: 40+ pages of detailed analysis with charts, tables, and interpretations
- **Scientific report (EN)**: Full English version for the international scientific community
- **Formula documentation**: Detailed mathematical description of all 27 tests

## 📊 Key Results

### Passing Tests (PASS)
Most basic statistical tests passed successfully, confirming local randomness of π digits:
- Frequency Test: ✅ PASS
- Runs Test: ✅ PASS
- Block Frequency: ✅ PASS
- Entropy Analysis: H ≈ 3.32 (close to maximum)
- Universal Statistical: p = 0.80
- Overlapping Template: p = 0.77

### Tests Showing Structures (FAIL)
Some advanced tests detected subtle structures on the scale of 10 billion digits:
- **Random Excursions**: p = 0.0 (deviations detected in state distribution)
- **Random Excursions Variant**: p = 0.0 (observed values differ from expected)
- **Non-overlapping Template**: p = 2e-11 (too few template matches)
- **BirthdaySpacings**: p = 0.0 (χ² = 91M)
- **SimplePoker**: p = 0.0
- **MaxOft**: p = 0.0
- **RandomWalk1**: p = 0.0

### Scientific Conclusions
1. **Local randomness**: π digits exhibit excellent random properties on small and medium scales
2. **Global structures**: On the scale of 10 billion digits, subtle structures were detected that do not occur in truly random sequences
3. **Cryptographic applications**: π can be used as a good PRNG with an appropriate seed, but not as a CSPRNG alone
4. **Randomness limits**: Results confirm theoretical limits of randomness for deterministic mathematical constants

## 🛠️ Technical Requirements

### Software
- Python 3.8+
- NumPy
- SciPy
- Matplotlib
- PyTorch (for ML tests)
- CUDA Toolkit (optional, for GPU acceleration)

### Hardware
- **RAM**: Minimum 32 GB (for full 10B digit analysis)
- **Disk**: ~10 GB free space
- **GPU**: Optional NVIDIA CUDA-compatible (for FFT tests)

## 🚀 Usage

### Install Dependencies
```bash
cd Program
pip install -r requirements.txt
```

### Run Analysis
```bash
cd Program
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

For detailed program documentation, see [Program/README.md](Program/README.md).

### Results Structure
Each test generates two JSON files:
- `XX_results.json` - Detailed test results (p-values, statistics, interpretations)
- `XX_status.json` - Execution status (success/error, execution time)

## 📚 Documentation

### Scientific Reports
- **RAPORT_Z_ANALIZY_PI.pdf**: Comprehensive scientific report in Polish containing:
  - Theoretical introduction
  - Detailed description of all 27 tests
  - Mathematical formulas
  - Results and interpretations
  - Charts and tables
  - Comparative analysis
  - Conclusions and cryptographic applications

- **RAPORT_Z_ANALIZY_PI_EN.pdf**: Full English version

### Result Files
All results are available in the `Dane z analizy/` directory in JSON format, enabling:
- Further analysis
- Results reproduction
- Integration with other tools

## 🔬 Results Interpretation Methodology

### P-values
- **p > 0.01**: Result consistent with randomness hypothesis
- **0.001 < p ≤ 0.01**: Weak deviation from randomness
- **p ≤ 0.001**: Strong deviation from randomness

### Important Note
FAIL results do not mean "errors" - these are **scientific observations** indicating subtle structures in π digits. For a deterministic mathematical constant, such structures are expected and constitute an important contribution to understanding the nature of π.

## 📈 Project Statistics

- **Number of tests**: 27
- **Data size**: 10 billion digits
- **Analysis time**: ~several days (depending on hardware)
- **Result files**: 54 JSON files
- **Report size**: 40+ pages each
- **Lines of code**: ~5000+ Python lines

## 👤 Author

**baver**

## 📄 License

The project is available for scientific and educational purposes.

## 🙏 Acknowledgments

- NIST for developing the Statistical Test Suite
- TestU01 for advanced randomness tests
- Scientific community for inspiration and support

## 📞 Contact

For questions regarding methodology or results, please contact via GitHub Issues.

---

**Note**: The project represents one of the largest and most comprehensive statistical studies of π digits conducted to date. All results are fully documented and reproducible.
