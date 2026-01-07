# Python Package Information - omnis2-pi-analysis

## 📦 Package Details

**Package Name**: `omnis2-pi-analysis`  
**Version**: 1.0.0  
**Author**: baver  
**License**: MIT  
**Python Version**: >=3.8

## 📋 Description

Comprehensive statistical analysis tool for Pi digits using 27 statistical tests from NIST Statistical Test Suite and TestU01 SmallCrush. Processes up to 10 billion digits with optional GPU acceleration.

## 🔧 Installation

### From PyPI (when published)
```bash
pip install omnis2-pi-analysis
```

### From GitHub
```bash
pip install git+https://github.com/Baver1022/omnis2-pi-analysis.git@OMNIS2
```

### From Local Source
```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
pip install .
```

## 📦 Package Structure

```
omnis2-pi-analysis/
├── analysis_orchestrator.py    # Main orchestrator
├── analysis_steps/             # 27 statistical test modules
│   ├── step_01_frequency.py
│   ├── step_02_runs.py
│   └── ... (25 more steps)
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

## 🚀 Usage

After installation:

```bash
# Using command-line entry point
omnis2-analyze --pi-file pi_10billion.txt

# Or directly with Python
python3 -m analysis_orchestrator --pi-file pi_10billion.txt
```

## 📊 Features

- **27 Statistical Tests**: NIST STS (17) + TestU01 SmallCrush (10)
- **GPU Acceleration**: Optional CUDA support
- **Large-Scale Processing**: Handles up to 10B digits
- **Comprehensive Output**: JSON results with detailed interpretations

## 📚 Dependencies

- `numpy>=1.21.0`
- `scipy>=1.7.0`
- `matplotlib>=3.4.0`
- `torch>=1.9.0`

## 🔗 Links

- **GitHub**: https://github.com/Baver1022/omnis2-pi-analysis
- **Documentation**: https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2
- **Issues**: https://github.com/Baver1022/omnis2-pi-analysis/issues

## 📄 License

MIT License - see LICENSE file for details

