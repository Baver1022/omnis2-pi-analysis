#!/usr/bin/env python3
from __future__ import annotations
"""KROK 25: SmallCrush - MatrixRank Test"""
import numpy as np

# GPU acceleration
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    cp = np
    GPU_AVAILABLE = False
from scipy import stats
from numpy.linalg import matrix_rank
from .base_step import AnalysisStep
from typing import Dict, Optional

class Step25MatrixRank(AnalysisStep):
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        max_sample_size = 1_000_000  # Mniejsze bo macierze są kosztowne
        if n > max_sample_size:
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
        
        # Konwersja na binarne
        binary = (digits % 2).astype(int)
        
        # Twórz macierze 32x32
        matrix_size = 32
        num_matrices = min(100, len(binary) // (matrix_size**2))
        
        ranks = []
        for i in range(num_matrices):
            start = i * (matrix_size**2)
            matrix = binary[start:start+matrix_size**2].reshape(matrix_size, matrix_size)
            rank = matrix_rank(matrix)
            ranks.append(rank)
        
        if len(ranks) < 10:
            return {'test_name': 'MatrixRank Test', 'status': 'SKIP', 'error': 'Insufficient matrices'}
        
        # Oczekiwany rozkład rang (dla losowych macierzy binarnych)
        # Uproszczony test
        observed, bins = np.histogram(ranks, bins=min(33, max(ranks)-min(ranks)+1))
        # Oczekiwane: większość macierzy powinna mieć pełną rangę
        expected_full_rank = num_matrices * 0.9  # ~90% pełnej rangi
        expected = np.full(len(observed), num_matrices / len(observed))
        expected[-1] = expected_full_rank  # Ostatni bin = pełna ranga
        
        chi2 = np.sum((observed - expected)**2 / np.maximum(expected, 0.1))
        p_value = 1 - stats.chi2.cdf(chi2, df=len(observed)-1)
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        return {'test_name': 'MatrixRank Test', 'n': int(n), 'p_value': float(p_value), 'status': status}

