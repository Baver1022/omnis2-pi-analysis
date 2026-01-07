#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 19: SmallCrush - Collision Test
- Test kolizji (collision) - sprawdza ile wartości się powtarza
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
from collections import Counter
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step19Collision(AnalysisStep):
    """SmallCrush: Collision Test"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        max_sample_size = 10_000_000
        if n > max_sample_size:
            print(f"   [PROC] Losowanie próbki {max_sample_size:,} z {n:,}...")
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            n = len(digits)
            print(f"   [OK] Próbka wybrana")
        
        # Parametry: m = zakres wartości, t = liczba próbek
        m = 10  # Cyfry 0-9
        t = min(10000, n // 10)  # Liczba próbek
        
        print(f"   📐 Parametry: m={m}, t={t}")
        
        # Wybierz losowe próbki
        print("   [PROC] Losowanie próbek...")
        np.random.seed(43)
        sample_indices = np.random.choice(n, t, replace=False)
        samples = digits[sample_indices]
        
        # Policz kolizje (powtórzenia)
        print("   [PROC] Liczenie kolizji...")
        counter = Counter(samples)
        collisions = sum(count - 1 for count in counter.values() if count > 1)
        num_unique = len(counter)
        
        print(f"   [OK] Unikalnych wartości: {num_unique}, Kolizji: {collisions}")
        
        # Oczekiwana liczba kolizji dla losowej sekwencji
        # E[collisions] ≈ t - m + m * (1 - 1/m)^t
        expected_collisions = t - m + m * ((1 - 1/m) ** t)
        
        # Chi-square test
        chi2 = (collisions - expected_collisions) ** 2 / max(expected_collisions, 0.1)
        p_value = 1 - stats.chi2.cdf(chi2, df=1)
        
        print(f"   [STATS] Oczekiwane kolizje: {expected_collisions:.2f}")
        print(f"   [STATS] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        return {
            'test_name': 'Collision Test (SmallCrush)',
            'n': int(n),
            'm': m,
            't': t,
            'collisions': collisions,
            'expected_collisions': float(expected_collisions),
            'num_unique': num_unique,
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status
        }

