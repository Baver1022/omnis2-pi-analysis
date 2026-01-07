#!/usr/bin/env python3
"""
KROK 1: Frequency Test (NIST)
- Test częstotliwości cyfr 0-9
- Chi-square test
"""

import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step01Frequency(AnalysisStep):
    """Test częstotliwości cyfr"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        # Oblicz częstotliwości
        print("   🔄 Liczenie częstotliwości cyfr 0-9...")
        frequencies = np.bincount(digits, minlength=10)
        print(f"   ✅ Częstotliwości: {frequencies.tolist()}")
        
        # Chi-square test
        print("   🧮 Obliczanie testu chi-square...")
        expected = n / 10.0
        print(f"      - Oczekiwana częstotliwość: {expected:.2f}")
        chi2 = np.sum((frequencies - expected) ** 2 / expected)
        p_value = 1 - stats.chi2.cdf(chi2, df=9)
        print(f"   📊 Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        # Status
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
        results = {
            'test_name': 'Frequency Test (NIST)',
            'n': int(n),
            'frequencies': frequencies.tolist(),
            'expected': float(expected),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Frequency test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

