#!/usr/bin/env python3
from __future__ import annotations
"""KROK 27: SmallCrush - RandomWalk1 Test"""
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

class Step27RandomWalk1(AnalysisStep):
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
        
        # Konwersja na binarne i random walk (używamy int8/int32 zamiast int64!)
        binary = (digits % 2).astype(np.int8)  # int8 zamiast int!
        X = (2 * binary - 1).astype(np.int8)  # int8 dla -1/+1
        S = np.cumsum(X.astype(np.int32))  # int32 dla cumulative sum
        
        # Test: maksymalne odchylenie od 0
        max_deviation = np.max(np.abs(S))
        
        # Oczekiwane maksymalne odchylenie dla random walk
        # E[max|S|] ≈ sqrt(2*n/π) dla dużych n
        expected_max = np.sqrt(2 * n / np.pi)
        
        # Test statystyczny
        z_score = (max_deviation - expected_max) / (np.std(S) / np.sqrt(n))
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'RandomWalk1 Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

