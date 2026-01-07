# 🔧 INSTALACJA CUPY NA WINDOWS - INSTRUKCJA

## ⚠️ PROBLEM

**Błąd:** `Microsoft Visual C++ 14.0 or greater is required`

CuPy wymaga kompilacji C++ na Windows, co wymaga Visual Studio Build Tools.

---

## ✅ ROZWIĄZANIA

### **OPCJA 1: Zainstaluj Microsoft C++ Build Tools** ⭐⭐⭐⭐⭐

**Najlepsze rozwiązanie:**

1. **Pobierz i zainstaluj:**
   - Link: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Wybierz: "Build Tools for Visual Studio"
   - Podczas instalacji wybierz: "Desktop development with C++"

2. **Po instalacji, zainstaluj CuPy:**
   ```bash
   py -m pip install cupy-cuda12x
   ```

**Czas:** ~30-60 minut (pobieranie + instalacja)

---

### **OPCJA 2: Użyj pre-built wheels** ⭐⭐⭐⭐

**Jeśli dostępne:**

```bash
# Spróbuj pre-built wheels:
py -m pip install --only-binary :all: cupy

# Lub konkretna wersja:
py -m pip install --only-binary :all: cupy==13.6.0
```

**Status:** ⚠️ Może nie być dostępne dla Windows + Python 3.14

---

### **OPCJA 3: Użyj Conda/Miniconda** ⭐⭐⭐⭐⭐

**Najłatwiejsze - pre-built binaries:**

1. **Zainstaluj Miniconda:**
   - Link: https://docs.conda.io/en/latest/miniconda.html
   - Pobierz: Windows 64-bit installer

2. **Zainstaluj CuPy przez conda:**
   ```bash
   conda install -c conda-forge cupy
   ```

**Korzyści:**
- ✅ Pre-built binaries (bez kompilacji)
- ✅ Automatyczna detekcja CUDA
- ✅ Łatwa instalacja

**Czas:** ~15-30 minut

---

### **OPCJA 4: Użyj WSL2 (Windows Subsystem for Linux)** ⭐⭐⭐

**Jeśli masz WSL2:**

```bash
# W WSL2:
pip install cupy-cuda12x
```

**Korzyści:**
- ✅ Łatwiejsza instalacja (Linux)
- ✅ Pełny dostęp do GPU
- ✅ Kompatybilność z Linux tools

---

## 🎯 REKOMENDACJA

### **OPCJA 1: Microsoft C++ Build Tools** (jeśli chcesz natywny Windows)

**Kroki:**
1. Pobierz: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Zainstaluj "Desktop development with C++"
3. Zainstaluj CuPy: `py -m pip install cupy-cuda12x`

**Czas:** ~1 godzina

---

### **OPCJA 2: Conda** (najszybsze)

**Kroki:**
1. Pobierz Miniconda: https://docs.conda.io/en/latest/miniconda.html
2. Zainstaluj
3. Zainstaluj CuPy: `conda install -c conda-forge cupy`

**Czas:** ~30 minut

---

## 📋 SZYBKA INSTALACJA (CONDA)

### **Na Windows PC (przez SSH):**

```bash
# 1. Pobierz Miniconda (jeśli nie masz):
# https://docs.conda.io/en/latest/miniconda.html

# 2. Zainstaluj Miniconda (GUI lub przez PowerShell)

# 3. Otwórz Anaconda Prompt i zainstaluj CuPy:
conda install -c conda-forge cupy

# 4. Sprawdź:
python -c "import cupy as cp; print('CuPy:', cp.__version__)"
python -c "import cupy as cp; print('GPU:', cp.cuda.Device(0).compute_capability)"
```

---

## ⚠️ ALTERNATYWA: BEZ CUPY (NA RAZIE)

**Możesz użyć obecnego kodu (CPU) i dodać CuPy później:**

1. **Uruchom analizę na CPU** (działa, ale wolniejsze)
2. **Zainstaluj CuPy później** (gdy będziesz miał Build Tools)
3. **Przepisz kod na CuPy** (łatwa zmiana `np` → `cp`)

**Kod działa bez CuPy** - po prostu będzie wolniejszy (3-10h zamiast 20-60min).

---

## ✅ NASTĘPNE KROKI

1. **Wybierz opcję:**
   - Conda (najszybsze) ⭐
   - Build Tools (natywny Windows)
   - WSL2 (jeśli masz)

2. **Zainstaluj CuPy**

3. **Sprawdź:**
   ```bash
   python -c "import cupy as cp; print('CuPy:', cp.__version__)"
   ```

4. **Przygotuj kod GPU** (mogę przygotować wersję z CuPy)

---

**Status:** ⚠️ Wymaga instalacji Build Tools lub Conda

**Rekomendacja:** Użyj Conda (najszybsze i najłatwiejsze)! 🚀

