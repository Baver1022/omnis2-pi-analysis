#!/usr/bin/env python3
from __future__ import annotations
"""
KROK 4: Entropy Analysis
- Lokalna entropia
- Średnia entropia
- Porównanie z maksymalną
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
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step04Entropy(AnalysisStep):
    """Analiza entropii"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        # GPU detection
        xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
        is_gpu = xp == cp
        
        n = len(digits)
        print(f"   [STATS] Analizuję {n:,} cyfr...")
        max_entropy = log2(10)  # ~3.321928
        print(f"   📐 Maksymalna entropia: {max_entropy:.6f}")
        
        # Oblicz globalną entropię
        print("   [PROC] Obliczanie globalnej entropii...")
        counter = Counter(digits)
        global_entropy = -sum((count/n)*log2(count/n) for count in counter.values() if count > 0)
        print(f"   [OK] Globalna entropia: {global_entropy:.6f}")
        
        # Lokalna entropia (okna po 10k)
        window_size = min(10000, n // 10)
        print(f"   [PROC] Analiza lokalnej entropii (okna {window_size:,} cyfr)...")
        entropy_samples = []
        num_windows = (n - window_size) // window_size
        print(f"   [STATS] Analizuję {num_windows:,} okien...")
        
        for i in range(0, n - window_size, window_size):
            window = digits[i:i+window_size]
            c = Counter(window)
            local_entropy = -sum((v/len(window))*log2(v/len(window)) for v in c.values() if v > 0)
            entropy_samples.append(local_entropy)
            if len(entropy_samples) % 1000 == 0:
                print(f"      - Przetworzono {len(entropy_samples):,}/{num_windows:,} okien...")
        
        avg_entropy = np.mean(entropy_samples) if entropy_samples else global_entropy
        print(f"   [OK] Średnia lokalna entropia: {avg_entropy:.6f}")
        
        results = {
            'test_name': 'Entropy Analysis',
            'n': int(n),
            'global_entropy': float(global_entropy),
            'avg_local_entropy': float(avg_entropy),
            'max_entropy': float(max_entropy),
            'entropy_ratio': float(global_entropy / max_entropy),
            'num_samples': len(entropy_samples),
            'interpretation': f"Entropy: {global_entropy:.6f} / {max_entropy:.6f} = {global_entropy/max_entropy:.4f}"
        }
        
        return results

