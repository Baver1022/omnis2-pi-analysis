#!/usr/bin/env python3
"""KROK 24: SmallCrush - WeightDistrib Test"""
import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step24WeightDistrib(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Test: suma wag w blokach
        block_size = 10
        num_blocks = n // block_size
        weights = [np.sum(digits[i*block_size:(i+1)*block_size]) for i in range(num_blocks)]
        
        # Oczekiwana suma: block_size * 4.5 (średnia 0-9)
        expected_sum = block_size * 4.5
        observed_mean = np.mean(weights)
        
        # Z-test
        z_score = (observed_mean - expected_sum) / (np.std(weights) / np.sqrt(num_blocks))
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'WeightDistrib Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

