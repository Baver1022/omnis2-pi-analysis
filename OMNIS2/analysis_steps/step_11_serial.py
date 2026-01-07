#!/usr/bin/env python3
"""
KROK 11: Serial Test (NIST)
- Test korelacji między parami i trójkami cyfr
- Chi-square test dla wzorców
"""

import numpy as np
from collections import Counter
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step11Serial(AnalysisStep):
    """Serial Test (NIST)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 10_000_000  # 10M cyfr max
        
        if n > max_sample_size:
            print(f"   🔄 Losowanie próbki {max_sample_size:,} cyfr z {n:,}...")
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            sample_digits = digits[sample_indices]
            print(f"   ✅ Próbka wybrana")
        else:
            sample_digits = digits
        
        # Analiza par (m=2)
        print("   🔄 Tworzenie par cyfr...")
        pairs = []
        for i in range(len(sample_digits) - 1):
            pairs.append((sample_digits[i], sample_digits[i+1]))
        print(f"   ✅ Utworzono {len(pairs):,} par")
        
        # Analiza trójek (m=3)
        print("   🔄 Tworzenie trójek cyfr...")
        triplets = []
        for i in range(len(sample_digits) - 2):
            triplets.append((sample_digits[i], sample_digits[i+1], sample_digits[i+2]))
        print(f"   ✅ Utworzono {len(triplets):,} trójek")
        
        # Chi-square test dla par
        print("   🧮 Analiza par - chi-square test...")
        pair_counter = Counter(pairs)
        expected_pairs = len(pairs) / 100  # 100 możliwych par (0-9 x 0-9)
        print(f"      - Oczekiwana częstotliwość: {expected_pairs:.2f}")
        chi2_pairs = sum((count - expected_pairs) ** 2 / expected_pairs 
                        for count in pair_counter.values())
        p_value_pairs = 1 - stats.chi2.cdf(chi2_pairs, df=99)
        print(f"   ✅ Chi-square par: {chi2_pairs:.4f}, P-value: {p_value_pairs:.6f}")
        
        # Chi-square test dla trójek (jeśli wystarczająco danych)
        p_value_triplets = 0.5
        if len(triplets) > 1000:
            print("   🧮 Analiza trójek - chi-square test...")
            triplet_counter = Counter(triplets)
            expected_triplets = len(triplets) / 1000  # 1000 możliwych trójek
            print(f"      - Oczekiwana częstotliwość: {expected_triplets:.2f}")
            chi2_triplets = sum((count - expected_triplets) ** 2 / expected_triplets 
                               for count in triplet_counter.values())
            p_value_triplets = 1 - stats.chi2.cdf(chi2_triplets, df=999)
            print(f"   ✅ Chi-square trójek: {chi2_triplets:.4f}, P-value: {p_value_triplets:.6f}")
        else:
            print("   ⏭️  Za mało trójek do analizy")
        
        # P-value (minimum z obu)
        p_value = min(p_value_pairs, p_value_triplets)
        print(f"   📊 Finalne P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
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

