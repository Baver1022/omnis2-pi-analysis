# 🚀 CUPY - WYJAŚNIENIE

## 📖 CO TO JEST CUPY?

**CuPy** to biblioteka Python, która jest **kompatybilną z NumPy** implementacją operacji na GPU (NVIDIA CUDA).

### **Prosta definicja:**
> **CuPy = NumPy dla GPU**

---

## 🎯 DLACZEGO CUPY?

### **Problem z NumPy:**
- NumPy wykonuje obliczenia na **CPU** (procesor)
- CPU ma **kilka/kilkanaście rdzeni** (np. 12 cores)
- **Wolne** dla dużych obliczeń (FFT, macierze)

### **Rozwiązanie - CuPy:**
- CuPy wykonuje obliczenia na **GPU** (karta graficzna)
- GPU ma **tysiące rdzeni** (RTX 4060 Ti = 4,352 CUDA cores)
- **10-100x szybciej** dla równoległych operacji!

---

## 📊 PORÓWNANIE: NUMPY vs CUPY

### **Przykład 1: FFT (Fast Fourier Transform)**

**NumPy (CPU):**
```python
import numpy as np

# Duża tablica
data = np.random.rand(10_000_000)

# FFT na CPU
result = np.fft.fft(data)
# Czas: ~2-5 sekund
```

**CuPy (GPU):**
```python
import cupy as cp

# Ta sama tablica, ale na GPU
data_gpu = cp.array(data)  # Kopiuj na GPU

# FFT na GPU
result_gpu = cp.fft.fft(data_gpu)
# Czas: ~0.2-0.5 sekund (10x szybciej!)
```

**Przyspieszenie:** **10x szybciej!** ⚡

---

### **Przykład 2: Operacje na macierzach**

**NumPy (CPU):**
```python
import numpy as np

# Duża macierz
A = np.random.rand(10_000, 10_000)
B = np.random.rand(10_000, 10_000)

# Mnożenie macierzy na CPU
C = np.dot(A, B)
# Czas: ~10-20 sekund
```

**CuPy (GPU):**
```python
import cupy as cp

# Macierze na GPU
A_gpu = cp.array(A)
B_gpu = cp.array(B)

# Mnożenie macierzy na GPU
C_gpu = cp.dot(A_gpu, B_gpu)
# Czas: ~1-2 sekundy (10x szybciej!)
```

**Przyspieszenie:** **10x szybciej!** ⚡

---

## 🔄 JAK DZIAŁA CUPY?

### **1. Kompatybilność z NumPy:**
```python
# NumPy:
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.sin(x)

# CuPy (identyczna składnia!):
import cupy as cp
x_gpu = cp.array([1, 2, 3, 4, 5])
y_gpu = cp.sin(x_gpu)
```

**Różnica:** Tylko `np` → `cp`!

---

### **2. Transfer danych CPU ↔ GPU:**

```python
import numpy as np
import cupy as cp

# Dane na CPU (RAM)
data_cpu = np.array([1, 2, 3, 4, 5])

# Kopiuj na GPU (VRAM)
data_gpu = cp.asarray(data_cpu)  # CPU → GPU

# Obliczenia na GPU
result_gpu = cp.fft.fft(data_gpu)

# Kopiuj z powrotem na CPU
result_cpu = cp.asnumpy(result_gpu)  # GPU → CPU
```

**Uwaga:** Transfer CPU ↔ GPU kosztuje czas! Wykonuj jak najwięcej na GPU.

---

## 🎯 DLA TWOJEJ ANALIZY π

### **Co przyspieszy CuPy:**

#### **1. Spectral FFT Analysis** ⭐⭐⭐⭐⭐
**Największa korzyść!**

**Obecnie (NumPy/CPU):**
```python
from scipy.fft import fft
pairs = np.array([...])  # 1M par cyfr
fft_result = fft(pairs)  # ~1-2 sekundy
```

**Z CuPy (GPU):**
```python
import cupy as cp
pairs_gpu = cp.asarray(pairs)  # Na GPU
fft_result_gpu = cp.fft.fft(pairs_gpu)  # ~0.1-0.2 sekundy
fft_result = cp.asnumpy(fft_result_gpu)  # Z powrotem
```

**Przyspieszenie:** **10x** (1-2s → 0.1-0.2s)

**Dla 10B cyfr:**
- CPU: 3-10 godzin
- GPU: 20-60 minut
- **Oszczędność: 3-11 godzin!** ⚡

---

#### **2. Operacje na macierzach** ⭐⭐⭐⭐
**Entropia, częstotliwości, statystyki**

```python
# NumPy (CPU):
freq = np.bincount(digits)  # Wolne dla dużych danych

# CuPy (GPU):
digits_gpu = cp.asarray(digits)
freq_gpu = cp.bincount(digits_gpu)  # 5-10x szybciej
```

**Przyspieszenie:** **5-10x**

---

#### **3. Batch Processing** ⭐⭐⭐
**Przetwarzanie większych batchów**

**Obecnie (CPU):**
- Batch size: 1M-10M cyfr (limit RAM)
- Przetwarzanie sekwencyjne

**Z GPU:**
- Batch size: 100M-1B cyfr (16GB VRAM!)
- Przetwarzanie równoległe
- **100x większe okna!**

---

## 📊 PRZYKŁAD: SPECTRAL FFT DLA 10B CYFR

### **Obecnie (CPU):**
```python
# Przetwarzamy w małych oknach (1M cyfr)
window_size = 1_000_000
for i in range(0, len(digits), window_size):
    window = digits[i:i+window_size]
    pairs = [window[j]*10 + window[j+1] for j in range(len(window)-1)]
    fft_result = np.fft.fft(pairs)  # ~1-2 sekundy na okno
    # Analiza...

# Czas: 10,000 okien × 1-2s = 10,000-20,000 sekund = 3-6 godzin
```

### **Z CuPy (GPU):**
```python
# Przetwarzamy w dużych oknach (100M cyfr)
window_size = 100_000_000
for i in range(0, len(digits), window_size):
    window = digits[i:i+window_size]
    pairs = [window[j]*10 + window[j+1] for j in range(len(window)-1)]
    pairs_gpu = cp.asarray(pairs)  # Na GPU
    fft_result_gpu = cp.fft.fft(pairs_gpu)  # ~10-30 sekund na okno
    fft_result = cp.asnumpy(fft_result_gpu)  # Z powrotem
    # Analiza...

# Czas: 100 okien × 10-30s = 1,000-3,000 sekund = 20-60 minut
```

**Przyspieszenie:** **10x** (3-6h → 20-60min)  
**Większe okna:** **100x** (1M → 100M cyfr)

---

## 🔧 INSTALACJA CUPY

### **Na Windows PC (RTX 4060 Ti):**

```bash
# Sprawdź wersję CUDA:
nvidia-smi
# Wynik: CUDA Version: 13.1

# Zainstaluj CuPy dla CUDA 13.x:
py -m pip install cupy-cuda13x

# Sprawdź:
py -c "import cupy as cp; print('CuPy:', cp.__version__)"
py -c "import cupy as cp; print('GPU:', cp.cuda.Device(0).compute_capability)"
```

---

## ⚠️ UWAGI I OGRANICZENIA

### **1. Transfer CPU ↔ GPU:**
```python
# WOLNE (unikaj jeśli możesz):
data_cpu = np.array([...])
data_gpu = cp.asarray(data_cpu)  # Transfer CPU → GPU
result_gpu = cp.fft.fft(data_gpu)
result_cpu = cp.asnumpy(result_gpu)  # Transfer GPU → CPU

# SZYBSZE (wykonuj wszystko na GPU):
data_gpu = cp.array([...])  # Bezpośrednio na GPU
result_gpu = cp.fft.fft(data_gpu)
# Zostań na GPU jak najdłużej!
```

---

### **2. Limit VRAM:**
- RTX 4060 Ti: **16GB VRAM**
- Możesz przetwarzać **~100M-1B cyfr** na raz
- Większe dane = batch processing

---

### **3. Kompatybilność:**
- CuPy jest **kompatybilny z NumPy**
- Większość kodu NumPy działa z CuPy
- **Ale:** Nie wszystkie funkcje NumPy są dostępne w CuPy

---

## 📊 PODSUMOWANIE

| Aspekt | NumPy (CPU) | CuPy (GPU) |
|--------|-------------|------------|
| **Lokalizacja** | RAM (CPU) | VRAM (GPU) |
| **Rdzenie** | 12 cores | 4,352 CUDA cores |
| **FFT (1M)** | 1-2s | 0.1-0.2s (10x) |
| **FFT (10B)** | 3-10h | 20-60min (10x) |
| **Batch size** | 1M-10M | 100M-1B (100x) |
| **Koszt** | Darmowe | Darmowe |

---

## ✅ DLA TWOJEJ ANALIZY

**CuPy da Ci:**
1. ✅ **10x przyspieszenie** dla Spectral FFT
2. ✅ **100x większe okna** analizy (100M-1B zamiast 1M-10M)
3. ✅ **Oszczędność czasu:** 3-11 godzin na analizę 10B cyfr
4. ✅ **Możliwość Opcji C:** 1T cyfr staje się możliwe!

---

## 🚀 GOTOWE DO UŻYCIA!

**Masz:**
- ✅ RTX 4060 Ti 16GB
- ✅ CUDA Driver 13.1
- ✅ Python 3.14.2

**Zainstaluj CuPy:**
```bash
py -m pip install cupy-cuda13x
```

**I gotowe!** Możesz używać GPU do analizy! 🎯

