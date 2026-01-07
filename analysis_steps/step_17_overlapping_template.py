#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 17: Overlapping Template Matching Test (NIST)
- Test częstotliwości występowania wzorców (templates) w sekwencji
- Wzorce MOGĄ się nakładać (overlapping)
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
from typing import Dict, Optional, List


def find_overlapping_matches(sequence: np.ndarray, template: List[int]) -> List[int]:
    """Znajdź wszystkie wystąpienia wzorca (z nakładaniem)"""
    matches = []
    template_len = len(template)
    
    for i in range(len(sequence) - template_len + 1):
        if np.array_equal(sequence[i:i+template_len], template):
            matches.append(i)
    
    return matches


class Step17OverlappingTemplate(AnalysisStep):
    """Overlapping Template Matching Test (NIST)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        # Konwersja na binarną sekwencję
        print("   [PROC] Konwersja na binarną sekwencję...")
        binary = (digits % 2).astype(int)
        print(f"   [OK] Utworzono {len(binary):,} bitów")
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 10_000_000  # 10M
        
        if len(binary) > max_sample_size:
            print(f"   [PROC] Losowanie próbki {max_sample_size:,} z {len(binary):,}...")
            sample_indices = np.random.choice(len(binary), max_sample_size, replace=False)
            binary = binary[sample_indices]
            print(f"   [OK] Próbka wybrana")
        
        # Wzorzec: m bitów (zwykle m=9)
        m = 9  # Długość wzorca
        num_templates = 5  # Liczba wzorców do testowania
        
        print(f"   📐 Parametry: m={m}, liczba wzorców={num_templates}")
        
        # Generuj wzorce (używamy deterministycznych dla powtarzalności)
        np.random.seed(43)  # Różne seed niż non-overlapping
        templates = []
        for i in range(num_templates):
            template = np.random.randint(0, 2, size=m).tolist()
            templates.append(template)
            print(f"      - Wzorzec {i+1}: {template}")
        
        # Dla każdego wzorca, znajdź wystąpienia
        print("   [PROC] Wyszukiwanie wzorców (overlapping)...")
        results_by_template = {}
        all_p_values = []
        
        for template_idx, template in enumerate(templates):
            matches = find_overlapping_matches(binary, template)
            num_matches = len(matches)
            
            print(f"      - Wzorzec {template_idx+1}: znaleziono {num_matches} wystąpień")
            
            # Oczekiwana liczba wystąpień dla losowej sekwencji
            # Prawdopodobieństwo wystąpienia wzorca: 1/2^m
            # Dla overlapping: oczekiwana ≈ (n - m + 1) / 2^m
            expected = (len(binary) - m + 1) / (2**m)
            
            # Chi-square test
            # Obserwowane vs oczekiwane
            chi2 = (num_matches - expected) ** 2 / max(expected, 0.1)
            p_value = 1 - stats.chi2.cdf(chi2, df=1)
            all_p_values.append(p_value)
            
            results_by_template[template_idx] = {
                'template': template,
                'num_matches': num_matches,
                'expected': float(expected),
                'chi2': float(chi2),
                'p_value': float(p_value)
            }
            
            print(f"         Oczekiwane: {expected:.2f}, Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        # Finalne p-value (minimum z wszystkich wzorców)
        if len(all_p_values) > 0:
            final_p_value = min(all_p_values)
        else:
            final_p_value = 0.5
        
        print(f"   [STATS] Finalne P-value: {final_p_value:.6f}")
        
        status = 'PASS' if final_p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Overlapping Template Matching Test (NIST)',
            'n': int(n),
            'm': m,
            'num_templates': num_templates,
            'results_by_template': results_by_template,
            'p_value': float(final_p_value),
            'status': status,
            'interpretation': f"Overlapping Template test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {final_p_value:.6f}"
        }
        
        return results

