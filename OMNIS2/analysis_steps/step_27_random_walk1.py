#!/usr/bin/env python3
"""KROK 27: SmallCrush - RandomWalk1 Test"""
import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step27RandomWalk1(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Konwersja na binarne i random walk
        binary = (digits % 2).astype(int)
        X = 2 * binary - 1  # -1 lub +1
        S = np.cumsum(X)  # Cumulative sum
        
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

