#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 20: SmallCrush - Gap Test
- Test odstępów (gap) między wystąpieniami określonej wartości
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
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step20Gap(AnalysisStep):
    """SmallCrush: Gap Test"""
    
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
        
        # Wybierz wartość do testowania (np. cyfra 5)
        target_value = 5
        m = 10  # Zakres wartości
        
        print(f"   📐 Testowanie odstępów dla wartości: {target_value}")
        
        # Znajdź wszystkie pozycje gdzie występuje target_value
        print("   [PROC] Wyszukiwanie pozycji...")
        positions = np.where(digits == target_value)[0]
        
        if len(positions) < 100:
            return {
                'test_name': 'Gap Test (SmallCrush)',
                'n': int(n),
                'status': 'SKIP',
                'error': f'Insufficient occurrences: {len(positions)}'
            }
        
        # Oblicz odstępy (gaps)
        print("   [PROC] Obliczanie odstępów...")
        gaps = np.diff(positions) - 1  # -1 bo gap to odległość minus 1
        
        print(f"   [OK] Obliczono {len(gaps)} odstępów")
        
        # Test rozkładu gaps (powinien być geometryczny)
        print("   [CALC] Test rozkładu geometrycznego...")
        
        # Podziel gaps na kategorie
        max_gap = min(100, np.max(gaps))
        bins = np.arange(0, max_gap + 2)
        observed, _ = np.histogram(gaps, bins=bins)
        
        # Oczekiwany rozkład geometryczny: P(gap=k) = (1-p)^k * p
        p = 1.0 / m  # Prawdopodobieństwo wystąpienia target_value
        expected_probs = [(1-p)**k * p for k in range(len(bins)-1)]
        expected = np.array(expected_probs) * len(gaps)
        expected = np.maximum(expected, 0.1)
        
        # Chi-square
        chi2 = np.sum((observed[:len(expected)] - expected) ** 2 / expected)
        df = len(expected) - 1
        p_value = 1 - stats.chi2.cdf(chi2, df=df)
        
        print(f"   [STATS] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        return {
            'test_name': 'Gap Test (SmallCrush)',
            'n': int(n),
            'target_value': target_value,
            'num_occurrences': len(positions),
            'num_gaps': len(gaps),
            'mean_gap': float(np.mean(gaps)),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status
        }

