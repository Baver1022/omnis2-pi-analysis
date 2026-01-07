#!/usr/bin/env python3
"""KROK 21: SmallCrush - SimplePoker Test"""
import numpy as np
from scipy import stats
from collections import Counter
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step21SimplePoker(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Podziel na bloki po 5 cyfr
        block_size = 5
        num_blocks = n // block_size
        blocks = [digits[i*block_size:(i+1)*block_size] for i in range(num_blocks)]
        
        # Dla każdego bloku, policz unikalne wartości
        unique_counts = [len(set(block)) for block in blocks]
        counter = Counter(unique_counts)
        
        # Oczekiwany rozkład (5 różnych wartości w bloku 5)
        # Uproszczony: dla losowej sekwencji, większość bloków ma 5 różnych wartości
        from scipy.special import comb
        expected = {
            1: num_blocks * (10/10**5),
            2: num_blocks * (comb(5,2) * 10 * 9 / 10**5),
            3: num_blocks * (comb(5,3) * 10 * 9 * 8 / 10**5),
            4: num_blocks * (comb(5,4) * 10 * 9 * 8 * 7 / 10**5),
            5: num_blocks * (10 * 9 * 8 * 7 * 6 / 10**5)
        }
        
        # Uproszczony test
        chi2 = sum((counter.get(k,0) - expected.get(k,0))**2 / max(expected.get(k,0.1), 0.1) 
                   for k in range(1,6))
        p_value = 1 - stats.chi2.cdf(chi2, df=4)
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'SimplePoker Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

