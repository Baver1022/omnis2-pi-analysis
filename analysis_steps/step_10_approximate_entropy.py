#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 10: Approximate Entropy Test (NIST)
- Test przybliżonej entropii
- Porównanie entropii dla m i m+1
"""

import numpy as np

# GPU acceleration
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    cp = np
    GPU_AVAILABLE = False
from collections import Counter
from math import log2
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional


def approximate_entropy(sequence, m, n):
    """Oblicz przybliżoną entropię dla wzorca długości m"""
    if len(sequence) < m + 1:
        return 0.0
    
    # Utwórz wzorce długości m i m+1
    patterns_m = []
    patterns_m1 = []
    
    for i in range(len(sequence) - m):
        pattern_m = tuple(sequence[i:i+m])
        patterns_m.append(pattern_m)
        
        if i < len(sequence) - m - 1:
            pattern_m1 = tuple(sequence[i:i+m+1])
            patterns_m1.append(pattern_m1)
    
    # Policz częstotliwości
    counter_m = Counter(patterns_m)
    counter_m1 = Counter(patterns_m1)
    
    # Oblicz entropię
    phi_m = 0.0
    for pattern, count in counter_m.items():
        if count > 0:
            phi_m += (count / len(patterns_m)) * log2(count / len(patterns_m))
    
    phi_m1 = 0.0
    for pattern, count in counter_m1.items():
        if count > 0:
            phi_m1 += (count / len(patterns_m1)) * log2(count / len(patterns_m1))
    
    # Approximate entropy
    apen = phi_m - phi_m1
    
    return apen


class Step10ApproximateEntropy(AnalysisStep):
    """Approximate Entropy Test (NIST)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 10_000_000  # 10M cyfr max
        
        if n > max_sample_size:
            print(f"   [PROC] Losowanie próbki {max_sample_size:,} cyfr z {n:,}...")
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            sample_digits = digits[sample_indices]
            print(f"   [OK] Próbka wybrana")
        else:
            sample_digits = digits
        
        # Konwersja na binarną
        print("   [PROC] Konwersja na binarną sekwencję...")
        binary = (sample_digits % 2).astype(int)
        
        # Parametry
        m = 2  # Długość wzorca
        print(f"   📐 Długość wzorca: {m}")
        
        # Oblicz approximate entropy
        print("   [CALC] Obliczanie approximate entropy...")
        print("      - Tworzenie wzorców długości m...")
        apen = approximate_entropy(binary, m, len(binary))
        print(f"   [OK] Approximate entropy: {apen:.6f}")
        
        # Test statystyczny (uproszczony)
        # Dla losowej sekwencji, apen powinno być ~0
        expected_apen = 0.0
        print(f"   📐 Oczekiwana entropia: {expected_apen:.6f}")
        
        # Chi-square test (uproszczony)
        print("   [CALC] Obliczanie testu chi-square...")
        chi2 = (apen - expected_apen) ** 2 / 0.1  # Empiryczna wariancja
        p_value = 1 - stats.chi2.cdf(chi2, df=1)
        print(f"   [STATS] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Approximate Entropy Test (NIST)',
            'n': int(n),
            'sample_size': len(sample_digits),
            'm': m,
            'approximate_entropy': float(apen),
            'expected_apen': float(expected_apen),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Approximate entropy test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

