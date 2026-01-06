@ -0,0 +1,79 @@
# OMNIS2 - Statistical Analysis of 10 Billion Digits of Pi

## 🔬 Project Description

Comprehensive statistical analysis of 10 billion digits of Pi using 27 statistical tests (17 NIST tests + 10 SmallCrush tests) with GPU acceleration.

**Note:** This is an initial/preliminary phase of the project.

## ✨ Features

- ✅ **27 statistical tests** (NIST + SmallCrush)
- ✅ **GPU acceleration** (CuPy for NVIDIA RTX)
- ✅ **Streaming processing** - processing 10B digits batch-by-batch
- ✅ **Checkpointing** - automatic result saving
- ✅ **Remote monitoring** - monitoring from Linux to Windows
- ✅ **Mathematical formulas documentation** (PDF)

## 📁 Project Structure

**[OMNIS2](https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2)**/

## 📊 Statistical Tests

### NIST Statistical Test Suite (17 tests):
1. Frequency Test
2. Runs Test
3. Block Frequency Test
4. Entropy Test
5. Spectral FFT Test
6. Compression Test
7. Empirical Entropy Bounds
8. ML LSTM Test
9. Cumulative Sums Test
10. Approximate Entropy Test
11. Serial Test
12. Linear Complexity Test
13. Random Excursions Test
14. Random Excursions Variant Test
15. Universal Statistical Test
16. Non-overlapping Template Matching Test
17. Overlapping Template Matching Test

### SmallCrush Test Suite (10 tests):
18. Birthday Spacings Test
19. Collision Test
20. Gap Test
21. Simple Poker Test
22. Coupon Collector Test
23. MaxOft Test
24. Weight Distribution Test
25. Matrix Rank Test
26. Hamming Independence Test
27. Random Walk 1 Test

## 📚 Documentation

- **Mathematical formulas:** `OMNIS2/MATHEMATICAL_FORMULAS_27_TESTS.pdf`

## 🔧 Requirements

- Python 3.8+
- NumPy, SciPy
- CuPy (for GPU acceleration)
- NVIDIA GPU with CUDA (optional, works on CPU too)

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 👤 Author

Statistical analysis project of Pi number - part of baver

## 🚧 Status

**Initial/Preliminary Phase** - Project is in early development stage.
