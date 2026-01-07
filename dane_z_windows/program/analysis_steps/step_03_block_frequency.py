#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 3: Block Frequency Test (NIST)
- Test częstotliwości w blokach
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


class Step03BlockFrequency(AnalysisStep):
    """Test częstotliwości w blokach"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        
        block_size = min(10000, n // 100)  # 100 bloków
        print(f"   📐 Rozmiar bloku: {block_size:,}")
        
        if block_size < 10:
            print("   ⚠️  Za mało cyfr dla testu blokowego - pomijam")
            return {
                'test_name': 'Block Frequency Test (NIST)',
                'n': int(n),
                'status': 'SKIP',
                'reason': 'Too few digits for block test'
            }
        
        # Podziel na bloki
        num_blocks = n // block_size
        print(f"   [PROC] Dzielenie na {num_blocks:,} bloków...")
        blocks = digits[:num_blocks * block_size].reshape(num_blocks, block_size)
        
        # Test dla każdego bloku (częstotliwość jedynek)
        print("   [PROC] Konwersja bloków na binarne i liczenie jedynek...")
        binary_blocks = (blocks % 2).astype(int)
        ones_per_block = np.sum(binary_blocks, axis=1)
        expected_ones = block_size / 2.0
        print(f"   [OK] Oczekiwane jedynki na blok: {expected_ones:.2f}")
        
        # Chi-square test
        print("   [CALC] Obliczanie testu chi-square...")
        chi2 = np.sum((ones_per_block - expected_ones) ** 2 / expected_ones)
        p_value = 1 - stats.chi2.cdf(chi2, df=num_blocks)
        print(f"   [STATS] Chi-square: {chi2:.4f}, P-value: {p_value:.6f}")
        
        status = 'PASS' if p_value >= 0.01 else 'FAIL'
        print(f"   [OK] Status: {status}")
        
        results = {
            'test_name': 'Block Frequency Test (NIST)',
            'n': int(n),
            'block_size': int(block_size),
            'num_blocks': int(num_blocks),
            'chi2': float(chi2),
            'p_value': float(p_value),
            'status': status,
            'interpretation': f"Block frequency test {'PASSED' if status == 'PASS' else 'FAILED'} with p-value {p_value:.6f}"
        }
        
        return results

