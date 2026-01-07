# Installation Guide - OMNIS2 Pi Analysis

## 📦 Installation Methods

### Method 1: From GitHub Releases (Recommended)

1. **Download the latest release**:
   - Go to [Releases](https://github.com/Baver1022/omnis2-pi-analysis/releases)
   - Download `omnis2-pi-analysis-v1.0.0.zip` or `omnis2-pi-analysis-v1.0.0.tar.gz`

2. **Extract the archive**:
   ```bash
   unzip omnis2-pi-analysis-v1.0.0.zip
   cd omnis2-pi-analysis-v1.0.0
   ```

3. **Install dependencies**:
   ```bash
   cd Program
   pip install -r requirements.txt
   ```

4. **Run the analysis**:
   ```bash
   python3 analysis_orchestrator.py --pi-file pi_10billion.txt
   ```

### Method 2: From Git Repository

```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
cd Program
pip install -r requirements.txt
python3 analysis_orchestrator.py --pi-file pi_10billion.txt
```

### Method 3: Python Package (pip)

```bash
pip install omnis2-pi-analysis
```

After installation, use:
```bash
omnis2-analyze --pi-file pi_10billion.txt
```

## 🔧 Requirements

### System Requirements
- **OS**: Linux, macOS, or Windows
- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (16GB+ recommended for 10B digits)
- **Disk Space**: ~20GB for 10 billion digits file

### Python Dependencies
- `numpy>=1.21.0`
- `scipy>=1.7.0`
- `matplotlib>=3.4.0`
- `torch>=1.9.0`

### Optional (GPU Acceleration)
- NVIDIA CUDA-compatible GPU
- CUDA Toolkit 11.0+
- PyTorch with CUDA support

## 📋 Quick Start

1. **Install dependencies**:
   ```bash
   pip install numpy scipy matplotlib torch
   ```

2. **Prepare Pi digits file**:
   - Download or generate `pi_10billion.txt`
   - Place it in the working directory

3. **Run analysis**:
   ```bash
   cd Program
   python3 analysis_orchestrator.py --pi-file pi_10billion.txt
   ```

4. **View results**:
   - Results are saved in `../Dane z analizy/Analiza_10B/`
   - Each test generates a JSON file with detailed results

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

## 📚 Additional Resources

- **Documentation**: See `README.md` and `Program/README.md`
- **Scientific Reports**: See `Raporty/` directory
- **GitHub Repository**: https://github.com/Baver1022/omnis2-pi-analysis
- **Issues**: https://github.com/Baver1022/omnis2-pi-analysis/issues

