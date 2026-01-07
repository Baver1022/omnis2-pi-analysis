#!/usr/bin/env python3
"""
KROK 16: Non-overlapping Template Matching Test (NIST)
- Test częstotliwości występowania wzorców (templates) w sekwencji
- Wzorce NIE mogą się nakładać (non-overlapping)
"""
import numpy as np
from scipy import stats
from collections import Counter
from .base_step import AnalysisStep
from typing import Dict, Optional, List


def find_non_overlapping_matches(sequence: np.ndarray, template: List[int]) -> List[int]:
    """Znajdź wszystkie nieprzekrywające się wystąpienia wzorca"""
    matches = []
    i = 0
    template_len = len(template)
    
    while i <= len(sequence) - template_len:
        if np.array_equal(sequence[i:i+template_len], template):
            matches.append(i)
            i += template_len  # Przeskocz o długość wzorca (non-overlapping)
        else:
            i += 1
    
    return matches


class Step16NonOverlappingTemplate(AnalysisStep):
    """Non-overlapping Template Matching Test (NIST)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        # Konwersja na binarną sekwencję
        print("   🔄 Konwersja na binarną sekwencję...")
        binary = (digits % 2).astype(int)
        print(f"   ✅ Utworzono {len(binary):,} bitów")
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 10_000_000  # 10M
        
        if len(binary) > max_sample_size:
            print(f"   🔄 Losowanie próbki {max_sample_size:,} z {len(binary):,}...")
            sample_indices = np.random.choice(len(binary), max_sample_size, replace=False)
            binary = binary[sample_indices]
            print(f"   ✅ Próbka wybrana")
        
        # Wybierz wzorce do testowania (m = 9 lub 10 bitów)
        # Używamy kilku losowych wzorców
        m = 9  # Długość wzorca
        num_templates = 5  # Liczba wzorców do testowania
        
        print(f"   📐 Parametry: m={m}, liczba wzorców={num_templates}")
        
        # Generuj wzorce (używamy deterministycznych dla powtarzalności)
        np.random.seed(42)  # Dla powtarzalności
        templates = []
        for i in range(num_templates):
            template = np.random.randint(0, 2, size=m).tolist()
            templates.append(template)
            print(f"      - Wzorzec {i+1}: {template}")
        
        # Dla każdego wzorca, znajdź wystąpienia
        print("   🔄 Wyszukiwanie wzorców (non-overlapping)...")
        results_by_template = {}
        all_p_values = []
        
        for template_idx, template in enumerate(templates):
            matches = find_non_overlapping_matches(binary, template)
            num_matches = len(matches)
            
            print(f"      - Wzorzec {template_idx+1}: znaleziono {num_matches} wystąpień")
            
            # Oczekiwana liczba wystąpień dla losowej sekwencji
            # Prawdopodobieństwo wystąpienia wzorca: 1/2^m
            # Dla non-overlapping: oczekiwana ≈ n / (2^m + m - 1)
            expected = len(binary) / (2**m + m - 1)
            
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
        
        print(f"   📊 Finalne P-value: {final_p_value:.6f}")
        
        status = 'PASS' if final_p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
        results = {
            'test_name': 'Non-overlapping Template Matching Test (NIST)',
            'n': int(n),
            'm': m,
            'num_templates': num_templates,
            'results_by_template': results_by_template,
            'p_value': float(final_p_value),
            'status': status,
            'interpretation': f"Non-overlapping Template test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {final_p_value:.6f}"
        }
        
        return results

