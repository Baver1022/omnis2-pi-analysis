#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 12: Linear Complexity Test (NIST)
- Test złożoności liniowej sekwencji binarnej
- Mierzy długość najkrótszego LFSR który generuje sekwencję
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
from .base_step import AnalysisStep
from typing import Dict, Optional


def berlekamp_massey(sequence):
    """
    Algorytm Berlekamp-Massey do obliczania złożoności liniowej
    Zwraca długość LFSR (Linear Feedback Shift Register)
    """
    n = len(sequence)
    if n == 0:
        return 0
    
    # Konwersja na listę int
    s = [int(b) for b in sequence]
    
    # Inicjalizacja
    C = [1]  # Connection polynomial
    B = [1]  # Previous connection polynomial
    L = 0    # Current length
    m = -1   # Previous discrepancy position
    b = 1    # Previous discrepancy value
    
    for n_iter in range(n):
        # Oblicz discrepancy
        d = s[n_iter]
        for i in range(1, min(L + 1, len(C))):
            if n_iter - i >= 0:
                d ^= C[i] & s[n_iter - i]
        
        if d == 1:
            # Discrepancy found - update polynomial
            T = C[:]
            # Shift and XOR
            shift = n_iter - m
            if shift > 0:
                # Rozszerz C jeśli potrzeba
                while len(C) < len(B) + shift:
                    C.append(0)
                # XOR z przesuniętym B
                for i in range(len(B)):
                    idx = i + shift
                    if idx < len(C):
                        C[idx] ^= B[i]
                    else:
                        C.append(B[i])
            
            if L <= n_iter // 2:
                L = n_iter + 1 - L
                m = n_iter
                B = T[:]
                b = 1
    
    return L


class Step12LinearComplexity(AnalysisStep):
    """Linear Complexity Test (NIST)"""
    
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
        max_sample_size = 1_000_000  # 1M bitów max (Berlekamp-Massey jest O(n²))
        
        if len(binary) > max_sample_size:
            print(f"   [PROC] Losowanie próbki {max_sample_size:,} bitów z {len(binary):,}...")
            sample_indices = np.random.choice(len(binary), max_sample_size, replace=False)
            sample_binary = binary[sample_indices]
            print(f"   [OK] Próbka wybrana")
        else:
            sample_binary = binary
        
        # Podziel na bloki (M = 500 bitów każdy)
        M = 500
        num_blocks = len(sample_binary) // M
        print(f"   📐 Dzielę na {num_blocks} bloków po {M} bitów...")
        
        complexities = []
        print("   [PROC] Obliczanie złożoności liniowej dla każdego bloku...")
        
        for i in range(num_blocks):
            block = sample_binary[i*M:(i+1)*M]
            complexity = berlekamp_massey(block)
            complexities.append(complexity)
            
            if (i + 1) % 100 == 0:
                print(f"      - Przetworzono {i+1}/{num_blocks} bloków...")
        
        print(f"   [OK] Obliczono złożoność dla {len(complexities)} bloków")
        
        # Oczekiwana złożoność: M/2 + (9 + (-1)^(M+1))/36
        expected_complexity = M / 2 + (9 + ((-1) ** (M + 1))) / 36
        
        # Statystyki
        mean_complexity = np.mean(complexities)
        std_complexity = np.std(complexities)
        
        print(f"   [STATS] Średnia złożoność: {mean_complexity:.2f} (oczekiwana: {expected_complexity:.2f})")
        print(f"   [STATS] Odchylenie std: {std_complexity:.2f}")
        
        # Chi-square test
        # Dzielimy zakres złożoności na kategorie
        bins = np.linspace(0, M, 20)
        observed, _ = np.histogram(complexities, bins=bins)
        
        # Oczekiwany rozkład (normalny wokół M/2)
        expected = np.diff(stats.norm.cdf(bins, loc=expected_complexity, scale=np.sqrt(M/12)))
        expected = expected * num_blocks
        expected = np.maximum(expected, 0.1)  # Unikaj dzielenia przez 0
        
        chi2 = np.sum((observed - expected) ** 2 / expected)
        df = len(observed) - 1
        p_value = 1 - stats.chi2.cdf(chi2, df=df)
        
        print(f"   [CALC] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Linear Complexity Test (NIST)',
            'n': int(n),
            'sample_size': len(sample_binary),
            'block_size': M,
            'num_blocks': num_blocks,
            'mean_complexity': float(mean_complexity),
            'expected_complexity': float(expected_complexity),
            'std_complexity': float(std_complexity),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Linear complexity test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

