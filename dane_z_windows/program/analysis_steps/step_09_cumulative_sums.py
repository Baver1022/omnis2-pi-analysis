#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 9: Cumulative Sums Test (NIST)
- Test skumulowanych sum w sekwencji binarnej
- Forward i backward mode
"""

import numpy as np

# GPU acceleration
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    cp = np
    GPU_AVAILABLE = False
from scipy import stats
from math import sqrt
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step09CumulativeSums(AnalysisStep):
    """Cumulative Sums Test (NIST)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        # Konwersja na binarną (parzyste=0, nieparzyste=1)
        print("   [PROC] Konwersja na binarną sekwencję...")
        binary = (digits % 2).astype(int)
        # Konwersja: 0 -> -1, 1 -> +1
        sequence = 2 * binary - 1
        
        # Forward cumulative sums
        print("    Obliczanie cumulative sums (forward)...")
        cumsum_forward = np.cumsum(sequence)
        max_forward = np.max(np.abs(cumsum_forward))
        print(f"   [OK] Max forward: {max_forward:.2f}")
        
        # Backward cumulative sums
        print("    Obliczanie cumulative sums (backward)...")
        cumsum_backward = np.cumsum(sequence[::-1])
        max_backward = np.max(np.abs(cumsum_backward))
        print(f"   [OK] Max backward: {max_backward:.2f}")
        
        # Test statystyczny (uproszczony)
        # Dla dużych n, max powinien być ~sqrt(n)
        expected_max = sqrt(n) * 0.95  # Empiryczna wartość
        print(f"   📐 Oczekiwany max: {expected_max:.2f}")
        
        # P-value (uproszczony - pełna implementacja wymaga dokładnych tablic)
        print("   [CALC] Obliczanie statystyk testowych...")
        z_forward = max_forward / sqrt(n) if n > 0 else 0
        z_backward = max_backward / sqrt(n) if n > 0 else 0
        print(f"   [STATS] Z-score forward: {z_forward:.4f}, backward: {z_backward:.4f}")
        
        # Przybliżony p-value (dla dużych n)
        p_value_forward = 1 - stats.norm.cdf(z_forward)
        p_value_backward = 1 - stats.norm.cdf(z_backward)
        p_value = min(p_value_forward, p_value_backward)
        print(f"    P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Cumulative Sums Test (NIST)',
            'n': int(n),
            'max_forward': float(max_forward),
            'max_backward': float(max_backward),
            'expected_max': float(expected_max),
            'z_forward': float(z_forward),
            'z_backward': float(z_backward),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Cumulative sums test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

