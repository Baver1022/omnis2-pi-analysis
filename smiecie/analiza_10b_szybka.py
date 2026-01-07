#!/usr/bin/env python3
"""
SZYBKA ANALIZA 10 MILIARDÓW CYFR π
Uproszczona wersja - tylko kluczowe metryki
"""

import numpy as np
from pathlib import Path
import zlib
from collections import defaultdict
import json
from datetime import datetime

def load_pi_fragment(start_pos, size):
    """Wczytaj fragment π"""
    pi_dir = Path("/home/baver/hexstrike-ai/OMNIS-PI-ENGINE/pi_10b_parts")
    chunk_size = 100_000_000
    
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
            if file_idx == (start_pos - 1) // chunk_size + 1 and pos_in_file > 0:
                content = f.read()
                content_arr = np.frombuffer(content, dtype=np.uint8)
                mask = (content_arr >= 48) & (content_arr <= 57)
                digits_found = content_arr[mask] - 48
                digits_found = digits_found[pos_in_file:]
            else:
                content = f.read()
                content_arr = np.frombuffer(content, dtype=np.uint8)
                mask = (content_arr >= 48) & (content_arr <= 57)
                digits_found = content_arr[mask] - 48
            
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
    return len(compressed) / original_size

def test_prediction_accuracy(digits, order=1, test_size=50_000):
    """Test predykcji - uproszczony"""
    if len(digits) < test_size * 2:
        test_size = len(digits) // 2
    
    train_size = len(digits) - test_size
    train = digits[:train_size]
    test = digits[train_size:]
    
    model = defaultdict(lambda: defaultdict(int))
    for i in range(len(train) - order):
        context = tuple(train[i:i+order])
        next_digit = train[i + order]
        model[context][next_digit] += 1
    
    for context in model:
        total = sum(model[context].values())
        for digit in model[context]:
            model[context][digit] /= total
    
    correct = 0
    total = 0
    for i in range(min(len(test) - order, 10_000)):  # Ograniczenie dla szybkości
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

def frequency_test(digits):
    """Test częstotliwości"""
    from scipy import stats
    n = len(digits)
    if n == 0:
        return {'chi2': 0, 'p_value': 1.0}
    
    freq = np.bincount(digits, minlength=10)
    expected = n / 10
    chi2 = np.sum((freq - expected) ** 2 / expected)
    df = 9
    p_value = 1 - stats.chi2.cdf(chi2, df)
    
    return {'chi2': chi2, 'p_value': p_value, 'frequencies': freq.tolist()}

def analyze_fragment_fast(start_pos, size, name):
    """Szybka analiza fragmentu"""
    print(f"\n{'='*70}")
    print(f"{name}")
    print(f"Pozycja: {start_pos:,} - {start_pos + size:,} ({size:,} cyfr)")
    print(f"{'='*70}")
    
    print("📊 Wczytywanie...")
    digits = load_pi_fragment(start_pos, size)
    print(f"✅ Wczytano {len(digits):,} cyfr")
    
    if len(digits) == 0:
        return None
    
    results = {'name': name, 'start_pos': start_pos, 'size': len(digits)}
    
    # 1. Kompresja
    print("  Kompresja...")
    ratio = test_compression_ratio(digits)
    results['compression_ratio'] = ratio
    print(f"    Ratio: {ratio:.6f}")
    
    # 2. Predykcja
    print("  Predykcja...")
    accuracy = test_prediction_accuracy(digits, order=1, test_size=min(50_000, size//10))
    results['prediction_accuracy'] = accuracy
    print(f"    Accuracy: {accuracy:.4f}%")
    
    # 3. Frequency Test
    print("  Frequency Test...")
    freq = frequency_test(digits)
    results['frequency_chi2'] = freq['chi2']
    results['frequency_pvalue'] = freq['p_value']
    print(f"    Chi2: {freq['chi2']:.4f}, p-value: {freq['p_value']:.6f}")
    
    return results

def main():
    print("="*70)
    print("SZYBKA ANALIZA 10 MILIARDÓW CYFR π")
    print("Weryfikacja spójności - kluczowe metryki")
    print("="*70)
    
    # Fragmenty do analizy
    fragments = [
        (1, 1_000_000, "Początek 1M"),
        (1, 10_000_000, "Początek 10M"),
        (1_000_000_000, 1_000_000, "Pozycja 1B"),
        (2_000_000_000, 1_000_000, "Pozycja 2B"),
        (3_000_000_000, 1_000_000, "Pozycja 3B"),
        (5_000_000_000, 1_000_000, "Pozycja 5B"),
        (5_000_000_000, 10_000_000, "Pozycja 5B (10M)"),
        (7_000_000_000, 1_000_000, "Pozycja 7B"),
        (9_000_000_000, 1_000_000, "Pozycja 9B"),
        (9_900_000_000, 1_000_000, "Koniec 9.9B"),
        (9_900_000_000, 10_000_000, "Koniec 9.9B (10M)"),
    ]
    
    all_results = []
    
    for start_pos, size, name in fragments:
        try:
            result = analyze_fragment_fast(start_pos, size, name)
            if result:
                all_results.append(result)
        except Exception as e:
            print(f"\n❌ Błąd: {name}: {e}")
            continue
    
    # Analiza spójności
    print("\n" + "="*70)
    print("ANALIZA SPÓJNOŚCI")
    print("="*70)
    
    if len(all_results) == 0:
        print("❌ Brak wyników")
        return
    
    metrics = ['compression_ratio', 'prediction_accuracy', 'frequency_chi2']
    
    print("\n📊 STATYSTYKI:")
    print("-" * 70)
    
    for metric in metrics:
        values = [r.get(metric) for r in all_results if r.get(metric) is not None]
        
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
            
            if cv < 1.0:
                status = "✅ BARDZO SPÓJNE"
            elif cv < 5.0:
                status = "✅ SPÓJNE"
            elif cv < 10.0:
                status = "⚠️  UMIARKOWANIE"
            else:
                status = "❌ NIESPÓJNE"
            
            print(f"  Status: {status}")
    
    # Tabela wyników
    print("\n" + "="*70)
    print("TABELA WYNIKÓW")
    print("="*70)
    print(f"{'Fragment':<25} {'Kompresja':<12} {'Predykcja':<12} {'Chi2':<10}")
    print("-" * 70)
    for r in all_results:
        comp = r.get('compression_ratio', 0)
        pred = r.get('prediction_accuracy', 0)
        chi2 = r.get('frequency_chi2', 0)
        print(f"{r['name']:<25} {comp:<12.6f} {pred:<12.4f} {chi2:<10.4f}")
    
    # Zapisz
    output_file = Path("/home/baver/hexstrike-ai/OMNIS2/analiza_10b_szybka_wyniki.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'fragments': all_results,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Wyniki zapisane: {output_file}")

if __name__ == '__main__':
    main()

