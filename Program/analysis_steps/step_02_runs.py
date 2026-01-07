#!/usr/bin/env python3
"""
KROK 2: Runs Test (NIST)
- Test liczby przejść (runs) w sekwencji binarnej
"""

import numpy as np
from scipy import stats
from math import sqrt
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step02Runs(AnalysisStep):
    """Test runs (przejść)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        # Konwersja na binarną (parzyste=0, nieparzyste=1)
        print("   🔄 Konwersja na binarną sekwencję...")
        binary = (digits % 2).astype(int)
        
        # Policz runs
        print("   🔄 Liczenie runs (przejść)...")
        runs = 0
        last_bit = None
        for bit in binary:
            if last_bit is not None and bit != last_bit:
                runs += 1
            last_bit = bit
        print(f"   ✅ Znaleziono {runs:,} runs")
        
        # Statystyki
        ones = int(np.sum(binary))
        zeros = n - ones
        
        if ones == 0 or zeros == 0:
            return {
                'test_name': 'Runs Test (NIST)',
                'n': int(n),
                'status': 'SKIP',
                'reason': 'All digits are same parity'
            }
        
        # Test statystyczny
        print("   🧮 Obliczanie statystyk testowych...")
        expected_runs = 2.0 * ones * zeros / n
        print(f"      - Oczekiwane runs: {expected_runs:.2f}")
        variance = (2.0 * ones * zeros * (2.0 * ones * zeros - n)) / (float(n)**2 * (n - 1))
        
        if variance <= 0:
            print("   ⚠️  Nieprawidłowa wariancja - pomijam")
            return {
                'test_name': 'Runs Test (NIST)',
                'n': int(n),
                'status': 'SKIP',
                'reason': 'Invalid variance'
            }
        
        z_score = (runs - expected_runs) / sqrt(variance)
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        print(f"   📊 Z-score: {z_score:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
        results = {
            'test_name': 'Runs Test (NIST)',
            'n': int(n),
            'runs': int(runs),
            'expected_runs': float(expected_runs),
            'ones': int(ones),
            'zeros': int(zeros),
            'z_score': float(z_score),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Runs test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

