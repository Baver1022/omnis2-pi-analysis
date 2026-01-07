#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 7: Empirical Entropy Bounds
- Analiza H(π)[N] dla różnych N
- Fit modelu: H(N) = log₂(10) * (1 - c/log(N))
- Confidence intervals
"""

import numpy as np

# GPU acceleration
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    cp = np
    GPU_AVAILABLE = False
from collections import Counter
from math import log2
from scipy.optimize import curve_fit
from scipy import stats
from .base_step import AnalysisStep
from typing import Dict, Optional


def entropy_model(N, c):
    """Model: H(N) = log₂(10) * (1 - c/log(N))"""
    max_entropy = log2(10)
    return max_entropy * (1 - c / np.log(N))


class Step07EntropyBounds(AnalysisStep):
    """Empiryczne granice entropii"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        max_entropy = log2(10)
        
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        max_entropy = log2(10)
        print(f"   📐 Maksymalna entropia: {max_entropy:.6f}")
        
        # Wartości N do analizy (logarytmicznie rozłożone)
        print("   [PROC] Przygotowywanie wartości N do analizy...")
        N_values = []
        current = 1000
        while current <= min(n, 1_000_000_000):
            N_values.append(int(current))
            current *= 10
        
        # Jeśli mamy więcej cyfr, dodaj większe wartości
        if n > 1_000_000:
            N_values.append(min(10_000_000, n))
        if n > 10_000_000:
            N_values.append(min(100_000_000, n))
        if n > 100_000_000:
            N_values.append(min(1_000_000_000, n))
        if n > 1_000_000_000:
            N_values.append(n)
        
        # Usuń duplikaty i posortuj
        N_values = sorted(list(set(N_values)))
        print(f"   [OK] Wartości N: {len(N_values)} punktów")
        
        # Oblicz entropię dla każdego N
        print("   [PROC] Obliczanie entropii dla każdego N...")
        entropy_results = []
        for idx, N in enumerate(N_values):
            if idx % 5 == 0:
                print(f"      - Analizuję N={N:,} ({idx+1}/{len(N_values)})...")
            if N > n:
                continue
            
            # Wczytaj pierwsze N cyfr
            sample = digits[:N]
            
            # Oblicz entropię
            counter = Counter(sample)
            H_N = -sum((count/N)*log2(count/N) for count in counter.values() if count > 0)
            
            entropy_results.append({
                'N': N,
                'H_N': float(H_N),
                'H_max': float(max_entropy),
                'ratio': float(H_N / max_entropy)
            })
        
        print(f"   [OK] Obliczono entropię dla {len(entropy_results)} wartości N")
        
        # Fit modelu (jeśli mamy wystarczająco punktów)
        model_fit = None
        if len(entropy_results) >= 3:
            print("   [CALC] Dopasowywanie modelu: H(N) = log₂(10) * (1 - c/log(N))...")
            try:
                N_array = np.array([r['N'] for r in entropy_results])
                H_array = np.array([r['H_N'] for r in entropy_results])
                
                # Fit: H(N) = log₂(10) * (1 - c/log(N))
                popt, pcov = curve_fit(
                    lambda N, c: entropy_model(N, c),
                    N_array,
                    H_array,
                    p0=[0.1],
                    bounds=(0, 10)
                )
                print(f"   [OK] Model dopasowany: c = {popt[0]:.6f}")
                
                c_estimate = float(popt[0])
                c_std = float(np.sqrt(pcov[0, 0]))
                
                # R²
                H_pred = entropy_model(N_array, c_estimate)
                ss_res = np.sum((H_array - H_pred) ** 2)
                ss_tot = np.sum((H_array - np.mean(H_array)) ** 2)
                r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
                
                # Confidence interval (95%)
                ci_lower = c_estimate - 1.96 * c_std
                ci_upper = c_estimate + 1.96 * c_std
                
                model_fit = {
                    'c_estimate': c_estimate,
                    'c_std': c_std,
                    'c_CI_lower': float(ci_lower),
                    'c_CI_upper': float(ci_upper),
                    'R_squared': float(r_squared),
                    'model': 'H(N) = log₂(10) * (1 - c/log(N))'
                }
            except Exception as e:
                model_fit = {'error': str(e)}
        
        results = {
            'test_name': 'Empirical Entropy Bounds',
            'n': int(n),
            'max_entropy': float(max_entropy),
            'entropy_by_N': entropy_results,
            'model_fit': model_fit,
            'interpretation': f"Entropy analysis for {len(entropy_results)} different N values"
        }
        
        return results

