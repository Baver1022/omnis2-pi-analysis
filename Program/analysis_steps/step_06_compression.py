#!/usr/bin/env python3
"""
KROK 6: Compression Test
- Test kompresji (LZ78-like)
- Compression ratio
"""

import zlib
import numpy as np
from .base_step import AnalysisStep
from typing import Dict, Optional


class Step06Compression(AnalysisStep):
    """Test kompresji"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        
        # Dla bardzo dużych zbiorów, użyj próbki
        max_sample_size = 100_000_000  # 100M cyfr max dla kompresji
        
        if n > max_sample_size:
            # Losowa próbka
            print(f"   🔄 Losowanie próbki {max_sample_size:,} cyfr z {n:,}...")
            sample_indices = np.random.choice(n, max_sample_size, replace=False)
            sample_digits = digits[sample_indices]
            print(f"   ✅ Próbka wybrana")
        else:
            sample_digits = digits
        
        # Konwersja na string (batch-wise dla dużych zbiorów)
        print("   🔄 Konwersja na string (batch-wise)...")
        batch_size = 10_000_000
        original_bytes = bytearray()
        num_batches = (len(sample_digits) + batch_size - 1) // batch_size
        
        for i in range(0, len(sample_digits), batch_size):
            batch = sample_digits[i:i+batch_size]
            batch_str = ''.join(map(str, batch))
            original_bytes.extend(batch_str.encode('utf-8'))
            if (i // batch_size + 1) % 10 == 0:
                print(f"      - Przetworzono {(i // batch_size + 1):,}/{num_batches:,} batchy...")
        
        original_size = len(original_bytes)
        print(f"   ✅ Rozmiar oryginalny: {original_size:,} bajtów")
        
        # Kompresja
        print("   🔄 Kompresja zlib (level 9)...")
        try:
            compressed = zlib.compress(bytes(original_bytes), level=9)
            compressed_size = len(compressed)
            compression_ratio = compressed_size / original_size if original_size > 0 else 0
            print(f"   ✅ Rozmiar skompresowany: {compressed_size:,} bajtów")
            print(f"   📊 Compression ratio: {compression_ratio:.6f}")
        except Exception as e:
            return {
                'test_name': 'Compression Test',
                'n': int(n),
                'sample_size': len(sample_digits),
                'status': 'FAIL',
                'error': str(e),
                'interpretation': f"Compression failed: {e}"
            }
        
        results = {
            'test_name': 'Compression Test',
            'n': int(n),
            'sample_size': len(sample_digits),
            'original_size': original_size,
            'compressed_size': compressed_size,
            'compression_ratio': float(compression_ratio),
            'interpretation': f"Compression ratio: {compression_ratio:.6f} (lower = more random, sample: {len(sample_digits):,} cyfr)"
        }
        
        return results

