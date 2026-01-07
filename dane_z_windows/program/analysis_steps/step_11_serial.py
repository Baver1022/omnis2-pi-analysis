#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 11: Serial Test (NIST)
- Test korelacji między parami i trójkami cyfr
- Chi-square test dla wzorców
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
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step11Serial(AnalysisStep):
    """Serial Test (NIST)"""
    
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
        
        # Analiza par (m=2)
        print("   [PROC] Tworzenie par cyfr...")
        pairs = []
        for i in range(len(sample_digits) - 1):
            pairs.append((sample_digits[i], sample_digits[i+1]))
        print(f"   [OK] Utworzono {len(pairs):,} par")
        
        # Analiza trójek (m=3)
        print("   [PROC] Tworzenie trójek cyfr...")
        triplets = []
        for i in range(len(sample_digits) - 2):
            triplets.append((sample_digits[i], sample_digits[i+1], sample_digits[i+2]))
        print(f"   [OK] Utworzono {len(triplets):,} trójek")
        
        # Chi-square test dla par
        print("   [CALC] Analiza par - chi-square test...")
        pair_counter = Counter(pairs)
        expected_pairs = len(pairs) / 100  # 100 możliwych par (0-9 x 0-9)
        print(f"      - Oczekiwana częstotliwość: {expected_pairs:.2f}")
        chi2_pairs = sum((count - expected_pairs) ** 2 / expected_pairs 
                        for count in pair_counter.values())
        p_value_pairs = 1 - stats.chi2.cdf(chi2_pairs, df=99)
        print(f"   [OK] Chi-square par: {chi2_pairs:.4f}, P-value: {p_value_pairs:.6f}")
        
        # Chi-square test dla trójek (jeśli wystarczająco danych)
        p_value_triplets = 0.5
        if len(triplets) > 1000:
            print("   [CALC] Analiza trójek - chi-square test...")
            triplet_counter = Counter(triplets)
            expected_triplets = len(triplets) / 1000  # 1000 możliwych trójek
            print(f"      - Oczekiwana częstotliwość: {expected_triplets:.2f}")
            chi2_triplets = sum((count - expected_triplets) ** 2 / expected_triplets 
                               for count in triplet_counter.values())
            p_value_triplets = 1 - stats.chi2.cdf(chi2_triplets, df=999)
            print(f"   [OK] Chi-square trójek: {chi2_triplets:.4f}, P-value: {p_value_triplets:.6f}")
        else:
            print("   [SKIP]  Za mało trójek do analizy")
        
        # P-value (minimum z obu)
        p_value = min(p_value_pairs, p_value_triplets)
        print(f"   [STATS] Finalne P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Serial Test (NIST)',
            'n': int(n),
            'sample_size': len(sample_digits),
            'num_pairs': len(pairs),
            'num_triplets': len(triplets),
            'chi2_pairs': float(chi2_pairs),
            'p_value_pairs': float(p_value_pairs),
            'p_value_triplets': float(p_value_triplets),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Serial test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

