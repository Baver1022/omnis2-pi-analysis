#!/usr/bin/env python3
"""KROK 26: SmallCrush - HammingIndep Test"""
import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step26HammingIndep(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Konwersja na binarne
        binary = (digits % 2).astype(int)
        
        # Test: Hamming weight (liczba jedynek) w blokach
        block_size = 32
        num_blocks = len(binary) // block_size
        hamming_weights = [np.sum(binary[i*block_size:(i+1)*block_size]) for i in range(num_blocks)]
        
        # Oczekiwana waga: block_size / 2
        expected_weight = block_size / 2
        observed_mean = np.mean(hamming_weights)
        
        # Chi-square test rozkładu wag
        observed, bins = np.histogram(hamming_weights, bins=block_size+1, range=(0, block_size+1))
        # Oczekiwany rozkład binarny
        from scipy.stats import binom
        expected = [binom.pmf(k, block_size, 0.5) * num_blocks for k in range(block_size+1)]
        expected = np.array(expected)
        
        chi2 = np.sum((observed - expected)**2 / np.maximum(expected, 0.1))
        p_value = 1 - stats.chi2.cdf(chi2, df=block_size)
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'HammingIndep Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

