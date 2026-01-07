#!/usr/bin/env python3
"""
KROK 15: Universal Statistical Test (NIST)
- Test Maurera (Maurer's Universal Test)
- Mierzy ile bitów potrzeba do opisania sekwencji
- Sprawdza kompresywność sekwencji
"""
import numpy as np
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step15UniversalStatistical(AnalysisStep):
    """Universal Statistical Test (NIST) - Maurer's Test"""
    
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
        
        n = len(binary)
        
        # Parametry testu Maurera
        # L: długość bloku (zwykle 6-16)
        # Q: liczba początkowych bloków do inicjalizacji (zwykle 10*2^L)
        L = 6  # Długość bloku
        Q = 10 * (2 ** L)  # Bloki inicjalizacyjne
        
        if n < Q + 10:
            print(f"   ⚠️  Za mało danych (n={n}, wymagane >{Q+10})")
            return {
                'test_name': 'Universal Statistical Test (NIST)',
                'n': int(n),
                'status': 'SKIP',
                'error': f'Insufficient data: {n} < {Q+10}'
            }
        
        print(f"   📐 Parametry: L={L}, Q={Q}")
        
        # Podziel na bloki długości L
        num_blocks = n // L
        blocks = []
        print("   🔄 Dzielenie na bloki...")
        
        for i in range(num_blocks):
            block = binary[i*L:(i+1)*L]
            # Konwersja bloku na liczbę całkowitą
            block_value = int(''.join(map(str, block)), 2)
            blocks.append(block_value)
        
        print(f"   ✅ Utworzono {len(blocks)} bloków")
        
        # Faza inicjalizacji: Q pierwszych bloków
        print("   🔄 Faza inicjalizacji (Q bloków)...")
        init_blocks = blocks[:Q]
        
        # Słownik: ostatnia pozycja każdego wzorca
        last_position = {}
        for i, block_val in enumerate(init_blocks):
            last_position[block_val] = i
        
        # Faza testowa: pozostałe bloki
        print("   🔄 Faza testowa (obliczanie odległości)...")
        K = num_blocks - Q  # Liczba bloków testowych
        
        if K < 10:
            print(f"   ⚠️  Za mało bloków testowych (K={K})")
            return {
                'test_name': 'Universal Statistical Test (NIST)',
                'n': int(n),
                'status': 'SKIP',
                'error': f'Insufficient test blocks: K={K}'
            }
        
        distances = []
        for i in range(Q, num_blocks):
            block_val = blocks[i]
            if block_val in last_position:
                distance = i - last_position[block_val]
                distances.append(distance)
            else:
                # Jeśli wzorzec nie wystąpił wcześniej, użyj dużej odległości
                distances.append(i + 1)
            last_position[block_val] = i
        
        print(f"   ✅ Obliczono {len(distances)} odległości")
        
        # Oblicz statystykę testową: fn = (1/K) * sum(log2(distance))
        print("   🧮 Obliczanie statystyki testowej...")
        log_distances = [np.log2(max(d, 1)) for d in distances]
        fn = np.mean(log_distances)
        
        # Oczekiwana wartość fn dla losowej sekwencji
        # Dla L=6: expected ≈ 5.2177052
        expected_fn = {
            6: 5.2177052,
            7: 6.1962507,
            8: 7.1836656,
            9: 8.1764248,
            10: 9.1723243
        }.get(L, 5.2177052)
        
        # Wariancja fn dla losowej sekwencji
        # Dla L=6: variance ≈ 2.954
        variance_fn = {
            6: 2.954,
            7: 3.125,
            8: 3.238,
            9: 3.311,
            10: 3.356
        }.get(L, 2.954)
        
        # Z-score
        z_score = (fn - expected_fn) / np.sqrt(variance_fn / K)
        
        # P-value (dwustronny test)
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        
        print(f"   📊 fn = {fn:.6f} (oczekiwane: {expected_fn:.6f})")
        print(f"   📊 Z-score: {z_score:.6f}")
        print(f"   📊 P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   ✅ Status: {status}")
        
        results = {
            'test_name': 'Universal Statistical Test (NIST)',
            'n': int(n),
            'L': L,
            'Q': Q,
            'K': K,
            'fn': float(fn),
            'expected_fn': expected_fn,
            'variance_fn': variance_fn,
            'z_score': float(z_score),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Universal Statistical test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

