#!/usr/bin/env python3
from __future__ import annotations
"""KROK 23: SmallCrush - MaxOft Test"""
import numpy as np

# GPU acceleration
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    cp = np
    GPU_AVAILABLE = False
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step23MaxOft(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Test: maksimum z t próbek
        t = 5
        num_trials = min(10000, n // t)
        maxima = []
        
        for _ in range(num_trials):
            start = np.random.randint(0, n - t)
            max_val = np.max(digits[start:start+t])
            maxima.append(max_val)
        
        # Oczekiwany rozkład maksimum
        # P(max <= k) = (k/9)^t dla cyfr 0-9
        observed, bins = np.histogram(maxima, bins=10, range=(0, 10))
        expected_probs = [(i/9)**t - ((i-1)/9)**t for i in range(1, 11)]
        expected = np.array(expected_probs) * num_trials
        
        chi2 = np.sum((observed - expected)**2 / np.maximum(expected, 0.1))
        p_value = 1 - stats.chi2.cdf(chi2, df=9)
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'MaxOft Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

