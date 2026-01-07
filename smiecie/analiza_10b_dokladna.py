#!/usr/bin/env python3
"""
DOKŁADNA ANALIZA 10 MILIARDÓW CYFR π
Weryfikacja spójności wyników metodologicznych na różnych fragmentach
"""

import numpy as np
from pathlib import Path
import zlib
from collections import defaultdict
from scipy import stats
import json
from datetime import datetime

# Import funkcji z advanced_statistical_methodology.py
import sys
sys.path.append('/home/baver/hexstrike-ai/OMNIS2')
from advanced_statistical_methodology import (
    lempel_ziv_complexity,
    approximate_entropy,
    sample_entropy,
    spectral_test,
    runs_test,
    frequency_test
)

def load_pi_fragment(start_pos, size):
    """
    Wczytaj fragment π z określonej pozycji
    start_pos: pozycja startowa (1-based, po przecinku)
    size: liczba cyfr do wczytania
    """
    pi_dir = Path("/home/baver/hexstrike-ai/OMNIS-PI-ENGINE/pi_10b_parts")
    chunk_size = 100_000_000
    
    # Oblicz który plik
    file_idx = (start_pos - 1) // chunk_size + 1
    pos_in_file = (start_pos - 1) % chunk_size
    
    digits = []
    remaining = size
    
    while remaining > 0:
        start_file_pos = (file_idx - 1) * chunk_size + 1
        end_file_pos = file_idx * chunk_size
        filename = f"{start_file_pos}-{end_file_pos}.txt"
        filepath = pi_dir / filename
        
        if not filepath.exists():
            break
        
        with open(filepath, 'rb') as f:
            # Dla pierwszego pliku, przeskocz do pozycji
            if file_idx == (start_pos - 1) // chunk_size + 1 and pos_in_file > 0:
                # Wczytaj cały plik
                content = f.read()
                content_arr = np.frombuffer(content, dtype=np.uint8)
                mask = (content_arr >= 48) & (content_arr <= 57)
                digits_found = content_arr[mask] - 48
                # Użyj offset
                digits_found = digits_found[pos_in_file:]
            else:
                content = f.read()
                content_arr = np.frombuffer(content, dtype=np.uint8)
                mask = (content_arr >= 48) & (content_arr <= 57)
                digits_found = content_arr[mask] - 48
            
            # Dodaj tylko tyle ile potrzebujemy
            needed = min(remaining, len(digits_found))
            digits.extend(digits_found[:needed])
            remaining -= needed
        
        file_idx += 1
        pos_in_file = 0
        
        if len(digits) >= size:
            break
    
    return np.array(digits[:size], dtype=np.uint8)

def test_compression_ratio(digits):
    """Test kompresji"""
    if len(digits) == 0:
        return 0.0
    digits_str = ''.join(map(str, digits))
    original_size = len(digits_str.encode('utf-8'))
    if original_size == 0:
        return 0.0
    compressed = zlib.compress(digits_str.encode('utf-8'))
    compressed_size = len(compressed)
    return compressed_size / original_size

def test_prediction_accuracy(digits, order=1, test_size=100_000):
    """Test predykcji Markowa"""
    if len(digits) < test_size * 2:
        test_size = len(digits) // 2
    
    train_size = len(digits) - test_size
    train = digits[:train_size]
    test = digits[train_size:]
    
    # Model Markowa
    model = defaultdict(lambda: defaultdict(int))
    for i in range(len(train) - order):
        context = tuple(train[i:i+order])
        next_digit = train[i + order]
        model[context][next_digit] += 1
    
    # Normalizuj
    for context in model:
        total = sum(model[context].values())
        for digit in model[context]:
            model[context][digit] /= total
    
    # Test
    correct = 0
    total = 0
    for i in range(len(test) - order):
        context = tuple(test[i:i+order])
        actual = test[i + order]
        
        if context in model:
            predicted = max(model[context].items(), key=lambda x: x[1])[0]
        else:
            predicted = np.random.randint(0, 10)
        
        if predicted == actual:
            correct += 1
        total += 1
    
    return (correct / total) * 100 if total > 0 else 0

def analyze_fragment(start_pos, size, name):
    """
    Pełna analiza fragmentu π
    """
    print(f"\n{'='*80}")
    print(f"ANALIZA FRAGMENTU: {name}")
    print(f"Pozycja: {start_pos:,} - {start_pos + size:,} ({size:,} cyfr)")
    print(f"{'='*80}")
    
    # Wczytaj dane
    print("📊 Wczytywanie danych...")
    digits = load_pi_fragment(start_pos, size)
    print(f"✅ Wczytano {len(digits):,} cyfr")
    
    if len(digits) == 0:
        print("❌ Błąd: Nie wczytano żadnych cyfr")
        return None
    
    results = {
        'name': name,
        'start_pos': start_pos,
        'size': len(digits),
        'timestamp': datetime.now().isoformat()
    }
    
    # 1. Kompresja
    print("\n1. TEST KOMPRESJI")
    print("-" * 80)
    ratio = test_compression_ratio(digits)
    results['compression_ratio'] = ratio
    print(f"  Ratio: {ratio:.6f}")
    
    # 2. Predykcja
    print("\n2. TEST PREDYKCJI (Markov)")
    print("-" * 80)
    accuracy = test_prediction_accuracy(digits, order=1, test_size=min(100_000, size//10))
    results['prediction_accuracy'] = accuracy
    print(f"  Accuracy: {accuracy:.4f}%")
    
    # 3. Lempel-Ziv Complexity
    print("\n3. LEMPEL-ZIV COMPLEXITY")
    print("-" * 80)
    lz_complexity, lz_normalized = lempel_ziv_complexity(digits)
    results['lz_complexity'] = lz_complexity
    results['lz_normalized'] = lz_normalized
    print(f"  Złożoność: {lz_complexity:,}")
    print(f"  Znormalizowana: {lz_normalized:.6f}")
    
    # 4. Approximate Entropy (tylko dla mniejszych próbek)
    if size <= 500_000:
        print("\n4. APPROXIMATE ENTROPY (ApEn)")
        print("-" * 80)
        apen = approximate_entropy(digits.astype(float), m=2, r=0.2)
        results['apen'] = apen
        print(f"  ApEn: {apen:.6f}")
    else:
        print("\n4. APPROXIMATE ENTROPY (ApEn)")
        print("-" * 80)
        print("  ⏭️  Pomijam (za duża próbka)")
        results['apen'] = None
    
    # 5. Sample Entropy (tylko dla mniejszych próbek)
    if size <= 500_000:
        print("\n5. SAMPLE ENTROPY (SampEn)")
        print("-" * 80)
        sampen = sample_entropy(digits.astype(float), m=2, r=0.2)
        results['sampen'] = sampen if sampen != float('inf') else None
        print(f"  SampEn: {sampen:.6f if sampen != float('inf') else '∞'}")
    else:
        print("\n5. SAMPLE ENTROPY (SampEn)")
        print("-" * 80)
        print("  ⏭️  Pomijam (za duża próbka)")
        results['sampen'] = None
    
    # 6. Spectral Test
    print("\n6. SPECTRAL TEST (FFT)")
    print("-" * 80)
    spectral = spectral_test(digits)
    results['spectral'] = spectral
    print(f"  Maksymalna moc: {spectral['max_power']:.6f}")
    print(f"  Entropia spektralna: {spectral['spectral_entropy']:.6f}")
    
    # 7. Runs Test
    print("\n7. RUNS TEST (NIST)")
    print("-" * 80)
    runs = runs_test(digits)
    results['runs'] = runs
    print(f"  Liczba runów: {runs['runs']:,}")
    print(f"  P-value: {runs['p_value']:.6f}")
    print(f"  Status: {'✅ PASS' if runs['p_value'] > 0.01 else '❌ FAIL'}")
    
    # 8. Frequency Test
    print("\n8. FREQUENCY TEST (NIST)")
    print("-" * 80)
    freq = frequency_test(digits)
    results['frequency'] = freq
    print(f"  Chi-square: {freq['chi2']:.4f}")
    print(f"  P-value: {freq['p_value']:.6f}")
    print(f"  Status: {'✅ PASS' if freq['p_value'] > 0.01 else '❌ FAIL'}")
    
    return results

def main():
    """
    Główna analiza - różne fragmenty z 10B cyfr
    """
    print("="*80)
    print("DOKŁADNA ANALIZA 10 MILIARDÓW CYFR π")
    print("Weryfikacja spójności wyników metodologicznych")
    print("="*80)
    
    # Definicja fragmentów do analizy
    fragments = [
        # Początek
        (1, 1_000_000, "Początek (1M)"),
        (1, 10_000_000, "Początek (10M)"),
        
        # Środek
        (5_000_000_000, 1_000_000, "Środek 5B (1M)"),
        (5_000_000_000, 10_000_000, "Środek 5B (10M)"),
        
        # Koniec
        (9_900_000_000, 1_000_000, "Koniec 9.9B (1M)"),
        (9_900_000_000, 10_000_000, "Koniec 9.9B (10M)"),
        
        # Różne pozycje
        (1_000_000_000, 1_000_000, "Pozycja 1B (1M)"),
        (2_000_000_000, 1_000_000, "Pozycja 2B (1M)"),
        (3_000_000_000, 1_000_000, "Pozycja 3B (1M)"),
        (7_000_000_000, 1_000_000, "Pozycja 7B (1M)"),
        (8_000_000_000, 1_000_000, "Pozycja 8B (1M)"),
    ]
    
    all_results = []
    
    for start_pos, size, name in fragments:
        try:
            result = analyze_fragment(start_pos, size, name)
            if result:
                all_results.append(result)
        except Exception as e:
            print(f"\n❌ Błąd podczas analizy {name}: {e}")
            continue
    
    # Analiza spójności
    print("\n" + "="*80)
    print("ANALIZA SPÓJNOŚCI WYNIKÓW")
    print("="*80)
    
    if len(all_results) == 0:
        print("❌ Brak wyników do analizy")
        return
    
    # Statystyki dla każdej metryki
    metrics = ['compression_ratio', 'prediction_accuracy', 'lz_normalized', 
               'spectral_spectral_entropy']
    
    print("\n📊 STATYSTYKI SPÓJNOŚCI:")
    print("-" * 80)
    
    consistency_report = {}
    
    for metric in metrics:
        values = []
        for result in all_results:
            if metric == 'spectral_spectral_entropy':
                val = result.get('spectral', {}).get('spectral_entropy')
            else:
                val = result.get(metric)
            
            if val is not None:
                values.append(val)
        
        if len(values) > 0:
            mean_val = np.mean(values)
            std_val = np.std(values)
            cv = (std_val / mean_val * 100) if mean_val > 0 else 0
            min_val = np.min(values)
            max_val = np.max(values)
            
            print(f"\n{metric.upper().replace('_', ' ')}:")
            print(f"  Średnia: {mean_val:.6f}")
            print(f"  Std: {std_val:.6f}")
            print(f"  CV: {cv:.4f}%")
            print(f"  Min: {min_val:.6f}")
            print(f"  Max: {max_val:.6f}")
            print(f"  Zakres: {max_val - min_val:.6f}")
            
            # Ocena spójności
            if cv < 1.0:
                status = "✅ BARDZO SPÓJNE"
            elif cv < 5.0:
                status = "✅ SPÓJNE"
            elif cv < 10.0:
                status = "⚠️  UMIARKOWANIE SPÓJNE"
            else:
                status = "❌ NIESPÓJNE"
            
            print(f"  Status: {status}")
            
            consistency_report[metric] = {
                'mean': mean_val,
                'std': std_val,
                'cv': cv,
                'min': min_val,
                'max': max_val,
                'status': status
            }
    
    # Zapisz wyniki
    output_file = Path("/home/baver/hexstrike-ai/OMNIS2/analiza_10b_wyniki.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'fragments': all_results,
            'consistency': consistency_report,
            'summary': {
                'total_fragments': len(all_results),
                'total_digits_analyzed': sum(r['size'] for r in all_results)
            }
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Wyniki zapisane do: {output_file}")
    
    # Wnioski
    print("\n" + "="*80)
    print("WNIOSKI")
    print("="*80)
    
    very_consistent = sum(1 for m in consistency_report.values() if m['cv'] < 1.0)
    consistent = sum(1 for m in consistency_report.values() if m['cv'] < 5.0)
    
    print(f"\n📊 Podsumowanie spójności:")
    print(f"  Bardzo spójne (CV < 1%): {very_consistent}/{len(consistency_report)}")
    print(f"  Spójne (CV < 5%): {consistent}/{len(consistency_report)}")
    
    if very_consistent >= len(consistency_report) * 0.75:
        print("\n✅ WNIOSEK: Wyniki są BARDZO SPÓJNE we wszystkich fragmentach")
        print("   → To potwierdza ergodyczność i normalność π")
    elif consistent >= len(consistency_report) * 0.75:
        print("\n✅ WNIOSEK: Wyniki są SPÓJNE we wszystkich fragmentach")
        print("   → To potwierdza ergodyczność π")
    else:
        print("\n⚠️  WNIOSEK: Wyniki wykazują pewną zmienność")
        print("   → Wymaga dalszej analizy")

if __name__ == '__main__':
    main()

