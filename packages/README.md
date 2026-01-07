# 📦 Python Package

This directory contains information about the Python package distribution of OMNIS2 Pi Analysis.

## 📥 Installation

### From GitHub Packages
```bash
pip install omnis2-pi-analysis --extra-index-url https://github.com/Baver1022/omnis2-pi-analysis/packages
```

### From PyPI (when published)
```bash
pip install omnis2-pi-analysis
```

### From Source
```bash
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
pip install .
```

## 📋 Package Information

See `PACKAGE_INFO.md` for detailed package information.

## 🔧 Build Package

To build the package locally:

```bash
pip install build wheel
python -m build
```

The built packages will be in the `dist/` directory.

## 📚 Documentation

- **Package Info**: `PACKAGE_INFO.md`
- **Main Documentation**: `../README.md`
- **Program Documentation**: `../Program/README.md`

