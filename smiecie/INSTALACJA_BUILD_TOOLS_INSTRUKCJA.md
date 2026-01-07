# 🔧 INSTALACJA MICROSOFT C++ BUILD TOOLS - INSTRUKCJA

## ✅ STATUS

- ✅ **Winget dostępny** (v1.12.350)
- ✅ **SSH działa** (test/1234)
- ⚠️ **Build Tools nie zainstalowane** (wymagane dla CuPy)

---

## 🚀 OPCJA 1: AUTOMATYCZNA INSTALACJA (WINGET)

### **Krok 1: Otwórz PowerShell jako Administrator**

**Na Windows PC (192.168.0.54):**
1. Naciśnij `Win + X`
2. Wybierz: **"Windows PowerShell (Admin)"** lub **"Terminal (Admin)"**
3. Potwierdź UAC (User Account Control)

---

### **Krok 2: Zainstaluj Build Tools**

**W PowerShell (jako Admin):**
```powershell
winget install Microsoft.VisualStudio.2022.BuildTools `
    --silent `
    --accept-package-agreements `
    --accept-source-agreements `
    --override "--quiet --wait --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
```

**Czas:** 30-60 minut (pobieranie + instalacja ~3-4GB)

---

### **Krok 3: Sprawdź instalację**

```powershell
# Sprawdź czy kompilator jest dostępny:
where cl

# Powinno pokazać: C:\Program Files\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\...
```

---

### **Krok 4: Zainstaluj CuPy**

```powershell
# Po zakończeniu instalacji Build Tools:
py -m pip install cupy-cuda12x

# Sprawdź:
py -c "import cupy as cp; print('CuPy:', cp.__version__)"
py -c "import cupy as cp; print('GPU:', cp.cuda.Device(0).compute_capability)"
```

---

## 🖱️ OPCJA 2: RĘCZNA INSTALACJA (GUI)

### **Krok 1: Pobierz Build Tools**

1. Otwórz przeglądarkę
2. Przejdź do: https://visualstudio.microsoft.com/visual-cpp-build-tools/
3. Pobierz: **"Build Tools for Visual Studio 2022"

---

### **Krok 2: Zainstaluj**

1. Uruchom installer (`vs_buildtools.exe`)
2. Wybierz: **"Desktop development with C++"**
3. Zaznacz: **"MSVC v143 - VS 2022 C++ x64/x86 build tools"**
4. Zaznacz: **"Windows 10/11 SDK"**
5. Kliknij: **"Install"**

**Czas:** 30-60 minut

---

### **Krok 3: Zainstaluj CuPy**

```powershell
py -m pip install cupy-cuda12x
```

---

## 📋 OPCJA 3: PRZEZ SKRYPT POWERSHELL

### **Krok 1: Skopiuj skrypt na Windows PC**

**Z Linuxa:**
```bash
# Przez SMB (jeśli działa):
smbclient //192.168.0.54/Users/test -U test%1234
put install_build_tools.ps1

# Lub ręcznie skopiuj plik:
# /home/baver/hexstrike-ai/OMNIS2/install_build_tools.ps1
```

---

### **Krok 2: Uruchom skrypt**

**Na Windows PC (PowerShell jako Admin):**
```powershell
powershell -ExecutionPolicy Bypass -File install_build_tools.ps1
```

**Skrypt automatycznie:**
1. Zainstaluje Build Tools
2. Zainstaluje CuPy
3. Sprawdzi instalację

---

## ⚡ SZYBKA INSTALACJA (Z LINUXA PRZEZ SSH)

**Jeśli masz uprawnienia administratora:**

```bash
# Z Linuxa:
sshpass -p '1234' ssh test@192.168.0.54 \
  "powershell -Command \"Start-Process powershell -Verb RunAs -ArgumentList '-Command', 'winget install Microsoft.VisualStudio.2022.BuildTools --silent --accept-package-agreements --accept-source-agreements --override \\\"--quiet --wait --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended\\\"' -Wait\""
```

**Uwaga:** Może wymagać interakcji (UAC prompt).

---

## 🔍 SPRAWDZENIE INSTALACJI

### **Po instalacji Build Tools:**

```powershell
# Sprawdź kompilator:
where cl

# Sprawdź wersję:
cl

# Powinno pokazać: Microsoft (R) C/C++ Optimizing Compiler...
```

---

### **Po instalacji CuPy:**

```powershell
# Sprawdź CuPy:
py -c "import cupy as cp; print('CuPy:', cp.__version__)"

# Sprawdź GPU:
py -c "import cupy as cp; print('GPU:', cp.cuda.Device(0).compute_capability)"

# Test FFT:
py -c "import cupy as cp; import numpy as np; data = cp.array(np.random.rand(1000)); result = cp.fft.fft(data); print('FFT OK:', len(result))"
```

---

## ⚠️ PROBLEMY I ROZWIĄZANIA

### **Problem 1: "Winget requires admin"**

**Rozwiązanie:**
- Uruchom PowerShell jako Administrator
- Lub użyj ręcznej instalacji (GUI)

---

### **Problem 2: "Build Tools installation failed"**

**Rozwiązanie:**
- Sprawdź czy masz wystarczająco miejsca na dysku (~5GB)
- Sprawdź logi: `%TEMP%\dd_*.log`
- Spróbuj ręcznej instalacji (GUI)

---

### **Problem 3: "CuPy installation failed after Build Tools"**

**Rozwiązanie:**
- Zrestartuj system (może być wymagane)
- Sprawdź czy kompilator jest w PATH:
  ```powershell
  $env:PATH -split ';' | Select-String "Visual Studio"
  ```
- Spróbuj użyć Conda zamiast pip

---

## ✅ NASTĘPNE KROKI PO INSTALACJI

1. **Sprawdź instalację:**
   ```powershell
   py -c "import cupy as cp; print('CuPy:', cp.__version__)"
   ```

2. **Przygotuj kod GPU** (mogę przygotować wersję z CuPy)

3. **Uruchom analizę na GPU:**
   ```powershell
   py expmath_extended_analysis_gpu.py --max-digits 10000000000
   ```

---

## 📊 PODSUMOWANIE

| Krok | Czas | Status |
|------|------|--------|
| **1. Instalacja Build Tools** | 30-60 min | ⏳ Do zrobienia |
| **2. Instalacja CuPy** | 5-10 min | ⏳ Po kroku 1 |
| **3. Sprawdzenie** | 1 min | ⏳ Po kroku 2 |
| **RAZEM** | **~1 godzina** | ⏳ |

---

## 🎯 REKOMENDACJA

**Użyj OPCJI 1 (Winget) - najszybsze:**
1. Otwórz PowerShell jako Admin
2. Uruchom komendę winget
3. Czekaj 30-60 minut
4. Zainstaluj CuPy

**Gotowe!** 🚀

