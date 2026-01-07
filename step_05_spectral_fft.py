#!/usr/bin/env python3
"""
KROK 5: Spectral FFT Analysis (GPU)
- Analiza spektralna par cyfr
- Wykrywanie spectral gaps
"""

import numpy as np
from math import log2
from .base_step import AnalysisStep
from typing import Dict, Optional

# GPU
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False
    from scipy.fft import fft, fftfreq


class Step05SpectralFFT(AnalysisStep):
    """Analiza spektralna FFT"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        window_size = min(1_000_000, n)  # Maksymalne okno
        print(f"   📐 Okno analizy: {window_size:,} cyfr")
        
        # Analiza par cyfr
        print("   🔄 Tworzenie par cyfr...")
        pairs = digits[:-1] * 10 + digits[1:]
        pairs_window = pairs[:window_size]
        print(f"   ✅ Utworzono {len(pairs_window):,} par")
        
        # FFT
        if GPU_AVAILABLE and len(pairs_window) > 10000:
            print("   ⚡ Używam GPU do FFT...")
            pairs_gpu = cp.asarray(pairs_window, dtype=cp.float32)
            fft_result = cp.fft.fft(pairs_gpu)
            power_spectrum = cp.abs(fft_result) ** 2
            power_spectrum = cp.asnumpy(power_spectrum)
            print("   ✅ FFT zakończone (GPU)")
        else:
            print("   🔄 Obliczanie FFT (CPU)...")
            fft_result = np.fft.fft(pairs_window.astype(np.float32))
            power_spectrum = np.abs(fft_result) ** 2
            print("   ✅ FFT zakończone (CPU)")
        
        # Entropia spektralna
        print("   🧮 Obliczanie entropii spektralnej...")
        power_normalized = power_spectrum / np.sum(power_spectrum)
        spectral_entropy = -np.sum(power_normalized * np.log2(power_normalized + 1e-10))
        print(f"   ✅ Entropia spektralna: {spectral_entropy:.6f}")
        
        # Wykrywanie gaps (niskie wartości w spektrum)
        print("   🔍 Wykrywanie spectral gaps...")
        threshold = np.percentile(power_spectrum, 5)
        gaps = np.where(power_spectrum < threshold)[0]
        print(f"   ✅ Znaleziono {len(gaps):,} gaps")
        
        results = {
            'test_name': 'Spectral FFT Analysis',
            'n': int(n),
            'window_size': int(window_size),
            'gpu_used': GPU_AVAILABLE,
            'spectral_entropy': float(spectral_entropy),
            'max_spectral_entropy': float(log2(window_size)),
            'num_gaps': len(gaps),
            'gaps_positions': gaps[:100].tolist() if len(gaps) > 0 else [],  # Pierwsze 100
            'interpretation': f"Spectral entropy: {spectral_entropy:.6f}, detected {len(gaps)} gaps"
        }
        
        return results

