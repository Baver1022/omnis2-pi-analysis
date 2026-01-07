#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 18: SmallCrush - BirthdaySpacings Test
- Test odstępów między "urodzinami" (birthday spacings)
- Sprawdza czy odstępy między powtarzającymi się wartościami są losowe
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
from collections import defaultdict
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step18BirthdaySpacings(AnalysisStep):
    """SmallCrush: BirthdaySpacings Test"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 10_000_000  # 10M
        
        if n > max_sample_size:
            print(f"   [PROC] Losowanie próbki {max_sample_size:,} z {n:,}...")
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            digits = digits[sample_indices]
            print(f"   [OK] Próbka wybrana")
            n = len(digits)
        
        # Parametry testu
        # n: liczba "urodzin" (wartości)
        # m: zakres wartości (modulo m)
        # lambda: oczekiwana liczba kolizji
        
        # Używamy cyfr bezpośrednio (0-9)
        m = 10  # Zakres wartości (cyfry 0-9)
        num_birthdays = min(10000, n // 10)  # Liczba "urodzin" do testowania
        
        print(f"   📐 Parametry: m={m}, liczba urodzin={num_birthdays}")
        
        # Wybierz losowe pozycje jako "urodziny"
        print("   [PROC] Losowanie pozycji urodzin...")
        np.random.seed(42)
        birthday_positions = np.sort(np.random.choice(n, num_birthdays, replace=False))
        birthday_values = digits[birthday_positions]
        
        # Grupuj pozycje według wartości (cyfry)
        print("   [PROC] Grupowanie urodzin według wartości...")
        value_positions = defaultdict(list)
        for pos, val in zip(birthday_positions, birthday_values):
            value_positions[val].append(pos)
        
        # Oblicz odstępy (spacings) dla każdej wartości
        print("   [PROC] Obliczanie odstępów (spacings)...")
        all_spacings = []
        
        for val, positions in value_positions.items():
            if len(positions) >= 2:
                # Sortuj pozycje
                sorted_pos = sorted(positions)
                # Oblicz odstępy między kolejnymi pozycjami
                spacings = [sorted_pos[i+1] - sorted_pos[i] for i in range(len(sorted_pos)-1)]
                all_spacings.extend(spacings)
        
        print(f"   [OK] Obliczono {len(all_spacings)} odstępów")
        
        if len(all_spacings) < 100:
            print(f"   ⚠️  Za mało odstępów ({len(all_spacings)})")
            return {
                'test_name': 'BirthdaySpacings Test (SmallCrush)',
                'n': int(n),
                'status': 'SKIP',
                'error': f'Insufficient spacings: {len(all_spacings)}'
            }
        
        # Test: sprawdź czy odstępy mają właściwy rozkład
        # Dla losowej sekwencji, odstępy powinny mieć rozkład wykładniczy
        print("   [CALC] Test rozkładu odstępów...")
        
        # Podziel odstępy na kategorie (bins)
        max_spacing = max(all_spacings)
        num_bins = min(20, max_spacing // 10 + 1)
        bins = np.linspace(0, max_spacing, num_bins + 1)
        
        observed, _ = np.histogram(all_spacings, bins=bins)
        
        # Oczekiwany rozkład wykładniczy
        # Dla losowej sekwencji: P(spacing = k) ≈ (1/m)^k * (1 - 1/m)
        lambda_param = 1.0 / m  # Prawdopodobieństwo kolizji
        expected_probs = []
        for i in range(len(bins) - 1):
            bin_start = bins[i]
            bin_end = bins[i+1]
            # Prawdopodobieństwo odstępu w tym zakresie
            prob = (1 - lambda_param) ** bin_start - (1 - lambda_param) ** bin_end
            expected_probs.append(prob)
        
        expected = np.array(expected_probs) * len(all_spacings)
        expected = np.maximum(expected, 0.1)  # Unikaj dzielenia przez 0
        
        # Chi-square test
        chi2 = np.sum((observed - expected) ** 2 / expected)
        df = len(observed) - 1
        p_value = 1 - stats.chi2.cdf(chi2, df=df)
        
        print(f"   [STATS] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'BirthdaySpacings Test (SmallCrush)',
            'n': int(n),
            'm': m,
            'num_birthdays': num_birthdays,
            'num_spacings': len(all_spacings),
            'mean_spacing': float(np.mean(all_spacings)),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"BirthdaySpacings test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

