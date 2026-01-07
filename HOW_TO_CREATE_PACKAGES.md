# 📦 Jak opublikować Package na GitHub Packages (ręcznie)

## Krok 1: Przygotuj środowisko

```bash
cd /home/baver/GitHub/omnis2-pi-analysis
git checkout OMNIS2
```

## Krok 2: Zainstaluj narzędzia do budowania

```bash
pip install build wheel twine
```

## Krok 3: Utwórz pliki konfiguracyjne pakietu

### Utwórz `setup.py` w głównym katalogu:

```python
from setuptools import setup, find_packages

setup(
    name="omnis2-pi-analysis",
    version="1.0.0",
    author="baver",
    description="Comprehensive statistical analysis of Pi digits using 27 statistical tests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Baver1022/omnis2-pi-analysis",
    packages=find_packages(where="Program"),
    package_dir={"": "Program"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "torch>=1.9.0",
    ],
)
```

### Utwórz `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "omnis2-pi-analysis"
version = "1.0.0"
description = "Comprehensive statistical analysis of Pi digits using 27 statistical tests"
requires-python = ">=3.8"
dependencies = [
    "numpy>=1.21.0",
    "scipy>=1.7.0",
    "matplotlib>=3.4.0",
    "torch>=1.9.0",
]
```

## Krok 4: Zbuduj pakiet

```bash
python -m build
```

To utworzy katalog `dist/` z plikami:
- `omnis2_pi_analysis-1.0.0.tar.gz`
- `omnis2_pi_analysis-1.0.0-py3-none-any.whl`

## Krok 5: Utwórz token GitHub

1. Przejdź do: https://github.com/settings/tokens
2. Kliknij **"Generate new token"** → **"Generate new token (classic)"**
3. Nadaj nazwę: `github-packages-token`
4. Wybierz uprawnienia:
   - ✅ `write:packages` - Upload packages
   - ✅ `read:packages` - Download packages
5. Kliknij **"Generate token"**
6. **Skopiuj token** (będzie widoczny tylko raz!)

## Krok 6: Skonfiguruj twine

Utwórz plik `~/.pypirc`:

```ini
[distutils]
index-servers = github

[github]
repository = https://github.com/Baver1022/omnis2-pi-analysis
username = Baver1022
password = YOUR_GITHUB_TOKEN_HERE
```

Lub użyj zmiennej środowiskowej:

```bash
export TWINE_USERNAME=Baver1022
export TWINE_PASSWORD=YOUR_GITHUB_TOKEN_HERE
```

## Krok 7: Opublikuj pakiet

```bash
python -m twine upload --repository github dist/*
```

## Krok 8: Sprawdź na GitHub

1. Przejdź do: https://github.com/Baver1022/omnis2-pi-analysis/packages
2. Powinien być widoczny pakiet `omnis2-pi-analysis`

## Instalacja pakietu

Po publikacji można zainstalować:

```bash
pip install omnis2-pi-analysis --extra-index-url https://github.com/Baver1022/omnis2-pi-analysis/packages
```

---

**Uwaga**: Token GitHub jest wrażliwy - nie commituj go do Git!

