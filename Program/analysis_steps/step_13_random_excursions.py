#!/usr/bin/env python3
"""
KROK 13: Random Excursions Test (NIST)
- Test wędrówki losowej (random walk) dla sekwencji binarnej
- Sprawdza czy suma kumulatywna (excursion) ma właściwy rozkład
"""
import numpy as np
from scipy import stats
from collections import Counter
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step13RandomExcursions(AnalysisStep):
    """Random Excursions Test (NIST)"""
    
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
        
        # Znajdź cykle (excursions) - miejsca gdzie S wraca do 0
        print("   🔄 Wykrywanie cykli (excursions)...")
        cycles = []
        cycle_starts = []
        
        for i in range(len(S)):
            if S[i] == 0:
                if len(cycle_starts) > 0:
                    # Zakończ poprzedni cykl
                    cycles.append(S[cycle_starts[-1]:i+1])
                cycle_starts.append(i)
        
        # Ostatni cykl
        if len(cycle_starts) > 0:
            cycles.append(S[cycle_starts[-1]:])
        
        print(f"   ✅ Znaleziono {len(cycles)} cykli")
        
        if len(cycles) < 500:
            print(f"   ⚠️  Za mało cykli ({len(cycles)}) - test wymaga minimum 500")
            return {
                'test_name': 'Random Excursions Test (NIST)',
                'n': int(n),
                'num_cycles': len(cycles),
                'status': 'SKIP',
                'error': f'Insufficient cycles: {len(cycles)} < 500'
            }
        
        # Dla każdego cyklu, znajdź maksymalne odchylenie od 0
        # i stany które odwiedził (x = -4, -3, -2, -1, 1, 2, 3, 4)
        states = [-4, -3, -2, -1, 1, 2, 3, 4]
        state_visits = {x: [] for x in states}
        
        print("   🔄 Analizowanie odwiedzin stanów w cyklach...")
        for cycle in cycles:
            for x in states:
                if x in cycle:
                    # Policz ile razy odwiedzono stan x w tym cyklu
                    visits = np.sum(cycle == x)
                    state_visits[x].append(visits)
        
        # Dla każdego stanu x, oblicz statystyki
        print("   🧮 Obliczanie statystyk dla każdego stanu...")
        results_by_state = {}
        p_values = []
        
        for x in states:
            if len(state_visits[x]) == 0:
                continue
            
            visits = np.array(state_visits[x])
            num_cycles_with_state = len(visits)
            
            # Oczekiwana liczba odwiedzin stanu x w cyklu
            # Dla random walk: E[visits] = 1 / (2|x|) dla |x| >= 1
            if abs(x) >= 1:
                expected_visits = 1.0 / (2 * abs(x))
            else:
                expected_visits = 0.5
            
            # Chi-square test
            # Kategorie: 0 odwiedzin, 1 odwiedzin, 2+ odwiedzin
            observed = [
                np.sum(visits == 0),
                np.sum(visits == 1),
                np.sum(visits >= 2)
            ]
            
            # Oczekiwane (rozkład geometryczny)
            p_0 = 1 - expected_visits
            p_1 = expected_visits * (1 - expected_visits)
            p_2plus = expected_visits ** 2
            
            expected = [
                num_cycles_with_state * p_0,
                num_cycles_with_state * p_1,
                num_cycles_with_state * p_2plus
            ]
            
            # Unikaj dzielenia przez 0
            expected = np.maximum(expected, 0.1)
            
            chi2 = np.sum((np.array(observed) - np.array(expected)) ** 2 / np.array(expected))
            df = 2
            p_value = 1 - stats.chi2.cdf(chi2, df=df)
            p_values.append(p_value)
            
            results_by_state[x] = {
                'num_cycles': num_cycles_with_state,
                'mean_visits': float(np.mean(visits)),
                'expected_visits': expected_visits,
                'chi2': float(chi2),
                'p_value': float(p_value)
            }
            
            print(f"      - Stan {x:2d}: {num_cycles_with_state} cykli, p-value: {p_value:.6f}")
        
        # Finalne p-value (minimum z wszystkich stanów)
        if len(p_values) > 0:
            final_p_value = min(p_values)
        else:
            final_p_value = 0.5
        
        print(f"   📊 Finalne P-value: {final_p_value:.6f}")
        
        status = 'PASS' if final_p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
        results = {
            'test_name': 'Random Excursions Test (NIST)',
            'n': int(n),
            'num_cycles': len(cycles),
            'states_analyzed': list(results_by_state.keys()),
            'results_by_state': results_by_state,
            'p_value': float(final_p_value),
            'status': status,
            'interpretation': f"Random Excursions test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {final_p_value:.6f}"
        }
        
        return results

