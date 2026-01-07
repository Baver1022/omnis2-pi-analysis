#!/usr/bin/env python3
"""KROK 22: SmallCrush - CouponCollector Test"""
import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step22CouponCollector(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Test: ile cyfr potrzeba żeby zebrać wszystkie 0-9
        m = 10
        num_trials = min(1000, n // 100)
        lengths = []
        
        for _ in range(num_trials):
            start = np.random.randint(0, n - 200)
            seen = set()
            for i in range(start, min(start+200, n)):
                seen.add(digits[i])
                if len(seen) == m:
                    lengths.append(i - start + 1)
                    break
        
        if len(lengths) < 10:
            return {'test_name': 'CouponCollector Test', 'status': 'SKIP', 'error': 'Insufficient data'}
        
        # Oczekiwana długość: m * H_m (harmonic number)
        H_m = sum(1.0/k for k in range(1, m+1))
        expected = m * H_m
        
        # Test
        mean_length = np.mean(lengths)
        z_score = (mean_length - expected) / (np.std(lengths) / np.sqrt(len(lengths)))
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'CouponCollector Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

