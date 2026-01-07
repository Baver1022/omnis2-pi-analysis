#!/usr/bin/env python3
"""
KROK 14: Random Excursions Variant Test (NIST)
- Wariant testu Random Excursions
- Sprawdza częstotliwość odwiedzin każdego stanu w random walk
"""
import numpy as np
from scipy import stats
from collections import Counter
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step14RandomExcursionsVariant(AnalysisStep):
    """Random Excursions Variant Test (NIST)"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        print(f"   📊 Analizuję {n:,} cyfr...")
        
        # Konwersja na binarną sekwencję
        print("   🔄 Konwersja na binarną sekwencję...")
        binary = (digits % 2).astype(int)
        # Konwersja 0->-1, 1->+1 dla random walk
        X = 2 * binary - 1
        print(f"   ✅ Utworzono {len(X):,} wartości ±1")
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 10_000_000  # 10M
        
        if len(X) > max_sample_size:
            print(f"   🔄 Losowanie próbki {max_sample_size:,} z {len(X):,}...")
            sample_indices = np.random.choice(len(X), max_sample_size, replace=False)
            X = X[sample_indices]
            print(f"   ✅ Próbka wybrana")
        
        # Oblicz cumulative sum (random walk)
        print("   🔄 Obliczanie cumulative sum (random walk)...")
        S = np.cumsum(X)
        S = np.concatenate([[0], S])  # Start from 0
        
        # Stany do analizy: -9, -8, ..., -1, 1, 2, ..., 9
        states = list(range(-9, 0)) + list(range(1, 10))
        
        # Policz ile razy każdy stan został odwiedzony
        print("   🔄 Liczenie odwiedzin stanów...")
        state_counts = Counter()
        
        for s in S:
            if s in states:
                state_counts[s] += 1
        
        print(f"   ✅ Policzono odwiedziny dla {len(state_counts)} stanów")
        
        # Dla każdego stanu x, oblicz statystyki
        print("   🧮 Obliczanie statystyk dla każdego stanu...")
        results_by_state = {}
        p_values = []
        
        n_total = len(S) - 1  # Liczba kroków (bez początkowego 0)
        
        for x in states:
            observed = state_counts.get(x, 0)
            
            # Oczekiwana liczba odwiedzin stanu x
            # Dla random walk: jeśli |x| <= 5, to oczekiwana = n / (2|x|)
            # Dla |x| > 5, użyj przybliżenia
            if abs(x) >= 1:
                # Prawdopodobieństwo odwiedzenia stanu x w jednym kroku
                # Dla symetrycznego random walk: P(x) ≈ 1/(2|x|) dla dużych n
                expected = n_total / (2 * abs(x))
            else:
                expected = n_total / 2
            
            # Chi-square test (obserwowane vs oczekiwane)
            # Używamy prostego testu: (obs - exp)^2 / exp
            if expected > 0:
                chi2 = (observed - expected) ** 2 / expected
                # Dla pojedynczego stopnia swobody
                p_value = 1 - stats.chi2.cdf(chi2, df=1)
            else:
                chi2 = 0
                p_value = 0.5
            
            p_values.append(p_value)
            
            results_by_state[x] = {
                'observed': int(observed),
                'expected': float(expected),
                'chi2': float(chi2),
                'p_value': float(p_value)
            }
            
            print(f"      - Stan {x:2d}: odwiedzin={observed:6d}, oczekiwane={expected:8.1f}, p-value={p_value:.6f}")
        
        # Finalne p-value (minimum z wszystkich stanów)
        if len(p_values) > 0:
            final_p_value = min(p_values)
        else:
            final_p_value = 0.5
        
        print(f"   📊 Finalne P-value: {final_p_value:.6f}")
        
        status = 'PASS' if final_p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
        results = {
            'test_name': 'Random Excursions Variant Test (NIST)',
            'n': int(n),
            'n_total_steps': n_total,
            'states_analyzed': states,
            'results_by_state': results_by_state,
            'p_value': float(final_p_value),
            'status': status,
            'interpretation': f"Random Excursions Variant test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {final_p_value:.6f}"
        }
        
        return results

