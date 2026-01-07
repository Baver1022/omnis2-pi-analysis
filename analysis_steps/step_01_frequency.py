#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 1: Frequency Test (NIST)
- Test częstotliwości cyfr 0-9
- Chi-square test
"""

import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional

# GPU acceleration with CPU fallback
try:
    import cupy as cp
    try:
        # Test if GPU operations work
        test = cp.array([1])
        _ = cp.sum(test)
        GPU_AVAILABLE = True
    except:
        cp = np
        GPU_AVAILABLE = False
except ImportError:
    cp = np
    GPU_AVAILABLE = False


class Step01Frequency(AnalysisStep):
    """Test częstotliwości cyfr"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # Detect if GPU array
        xp = cp if GPU_AVAILABLE and isinstance(digits, cp.ndarray) else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr {'[GPU]' if is_gpu else '[CPU]'}...", flush=True)
        
        # Oblicz częstotliwości - GPU accelerated
        print("   [PROC] Liczenie częstotliwości cyfr 0-9...", flush=True)
        frequencies = xp.bincount(digits, minlength=10)
        
        # Transfer back to CPU for output
        if is_gpu:
            frequencies_cpu = cp.asnumpy(frequencies)
        else:
            frequencies_cpu = frequencies
        print(f"   [OK] Częstotliwości: {frequencies_cpu.tolist()}", flush=True)
        
        # Chi-square test - GPU accelerated
        print("   [CALC] Obliczanie testu chi-square...", flush=True)
        expected = n / 10.0
        print(f"      - Oczekiwana częstotliwość: {expected:.2f}", flush=True)
        chi2 = float(xp.sum((frequencies - expected) ** 2 / expected))
        p_value = 1 - stats.chi2.cdf(chi2, df=9)
        print(f"   [STATS] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}", flush=True)
        
        # Status
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Frequency Test (NIST)',
            'n': int(n),
            'frequencies': frequencies_cpu.tolist(),
            'expected': float(expected),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status,
            'gpu_accelerated': is_gpu,
            'interpretation': f"Frequency test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

