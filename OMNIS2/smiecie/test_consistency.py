#!/usr/bin/env python3
"""
Test spójności: Czy wyniki są zawsze takie same?
Sprawdza różne fragmenty π i różne rozmiary próbek
"""

import numpy as np
import zlib
from pathlib import Path
from collections import defaultdict
from scipy import stats

def load_pi_digits(n=10_000_000, offset=0):
    """Wczytaj cyfry π z offsetem"""
    digits = []
    chunk_size = 100_000_000
    pi_dir = Path("/home/baver/hexstrike-ai/OMNIS-PI-ENGINE/pi_10b_parts")
    
    # Oblicz który plik i pozycję
    start_file_idx = (offset // chunk_size) + 1
    start_pos_in_file = offset % chunk_size
    
    # Oblicz ile plików potrzebujemy
    total_needed = offset + n
    end_file_idx = (total_needed // chunk_size) + 1
    
    for file_idx in range(start_file_idx, end_file_idx + 1):
        start_pos = (file_idx - 1) * chunk_size + 1
        end_pos = file_idx * chunk_size
        filename = f"{start_pos}-{end_pos}.txt"
        filepath = pi_dir / filename
        
        if filepath.exists():
            with open(filepath, 'rb') as f:
                # Dla pierwszego pliku, przeskocz offset
                if file_idx == start_file_idx and start_pos_in_file > 0:
                    # Wczytaj cały plik i przetwórz
                    content = f.read()
                    content_arr = np.frombuffer(content, dtype=np.uint8)
                    mask = (content_arr >= 48) & (content_arr <= 57)
                    digits_found = content_arr[mask] - 48
                    # Użyj offsetu
                    digits_found = digits_found[start_pos_in_file:]
                else:
                    # Wczytaj cały plik
                    content = f.read()
                    content_arr = np.frombuffer(content, dtype=np.uint8)
                    mask = (content_arr >= 48) & (content_arr <= 57)
                    digits_found = content_arr[mask] - 48
                
                # Dodaj tylko tyle ile potrzebujemy
                needed = n - len(digits)
                digits.extend(digits_found[:needed])
                
                if len(digits) >= n:
                    break
    
    result = np.array(digits[:n], dtype=np.uint8)
    if len(result) == 0:
        print(f"⚠️  Ostrzeżenie: Wczytano 0 cyfr (offset={offset}, n={n})")
    return result

def test_compression_ratio(digits):
    """Test kompresji - zwraca ratio"""
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
    """Test predykcji - zwraca dokładność"""
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

def test_chaos_correlation(digits, n=100_000):
    """Test chaosu - zwraca maksymalną korelację"""
    digits = digits[:n]
    
    # Mapa logistyczna
    def logistic_map(x0, r, n):
        x = np.zeros(n)
        x[0] = x0
        for i in range(1, n):
            x[i] = r * x[i-1] * (1 - x[i-1])
        return x
    
    def normalize_to_digits(sequence):
        min_val = np.min(sequence)
        max_val = np.max(sequence)
        if max_val > min_val:
            normalized = ((sequence - min_val) / (max_val - min_val)) * 9
        else:
            normalized = sequence * 9
        return np.round(normalized).astype(int) % 10
    
    max_corr = 0
    for r in [3.5, 3.7, 3.8, 3.9]:
        sequence = logistic_map(0.5, r, n)
        simulated = normalize_to_digits(sequence)
        corr, _ = stats.pearsonr(digits, simulated)
        max_corr = max(max_corr, abs(corr))
    
    return max_corr

def main():
    print("="*60)
    print("TEST SPÓJNOŚCI - Czy wyniki są zawsze takie same?")
    print("="*60)
    
    # Test 1: Różne fragmenty π
    print("\n1. TEST RÓŻNYCH FRAGMENTÓW π")
    print("-"*60)
    
    fragments = [
        (0, 1_000_000, "Początek"),
        (10_000_000, 1_000_000, "Pozycja 10M"),
        (50_000_000, 1_000_000, "Pozycja 50M"),
        (100_000_000, 1_000_000, "Pozycja 100M"),
    ]
    
    compression_ratios = []
    prediction_accuracies = []
    chaos_correlations = []
    
    for offset, size, name in fragments:
        print(f"\n{name} (offset={offset:,}, size={size:,}):")
        digits = load_pi_digits(size, offset)
        
        # Kompresja
        ratio = test_compression_ratio(digits)
        compression_ratios.append(ratio)
        print(f"  Kompresja ratio: {ratio:.6f}")
        
        # Predykcja
        accuracy = test_prediction_accuracy(digits, order=1, test_size=min(100_000, size//10))
        prediction_accuracies.append(accuracy)
        print(f"  Predykcja accuracy: {accuracy:.4f}%")
        
        # Chaos
        correlation = test_chaos_correlation(digits, n=min(100_000, size))
        chaos_correlations.append(correlation)
        print(f"  Chaos correlation: {correlation:.6f}")
    
    # Test 2: Różne rozmiary próbek
    print("\n\n2. TEST RÓŻNYCH ROZMIARÓW PRÓBEK")
    print("-"*60)
    
    sizes = [100_000, 500_000, 1_000_000, 5_000_000, 10_000_000]
    
    compression_by_size = []
    prediction_by_size = []
    
    for size in sizes:
        print(f"\nRozmiar {size:,}:")
        digits = load_pi_digits(size)
        
        ratio = test_compression_ratio(digits)
        compression_by_size.append(ratio)
        print(f"  Kompresja ratio: {ratio:.6f}")
        
        accuracy = test_prediction_accuracy(digits, order=1, test_size=min(100_000, size//10))
        prediction_by_size.append(accuracy)
        print(f"  Predykcja accuracy: {accuracy:.4f}%")
    
    # Analiza spójności
    print("\n\n" + "="*60)
    print("ANALIZA SPÓJNOŚCI")
    print("="*60)
    
    # Kompresja
    comp_std = np.std(compression_ratios)
    comp_mean = np.mean(compression_ratios)
    comp_cv = (comp_std / comp_mean) * 100 if comp_mean > 0 else 0
    
    print(f"\nKompresja (różne fragmenty):")
    print(f"  Średnia: {comp_mean:.6f}")
    print(f"  Odchylenie std: {comp_std:.6f}")
    print(f"  Współczynnik zmienności: {comp_cv:.4f}%")
    
    if comp_cv < 1.0:
        print(f"  ⚠️  BARDZO MAŁA ZMIENNOŚĆ - wyniki są prawie identyczne!")
    elif comp_cv < 5.0:
        print(f"  ⚠️  Mała zmienność - wyniki są bardzo podobne")
    else:
        print(f"  ✅ Normalna zmienność")
    
    # Predykcja
    pred_std = np.std(prediction_accuracies)
    pred_mean = np.mean(prediction_accuracies)
    pred_cv = (pred_std / pred_mean) * 100 if pred_mean > 0 else 0
    
    print(f"\nPredykcja (różne fragmenty):")
    print(f"  Średnia: {pred_mean:.4f}%")
    print(f"  Odchylenie std: {pred_std:.4f}%")
    print(f"  Współczynnik zmienności: {pred_cv:.4f}%")
    
    if pred_cv < 1.0:
        print(f"  ⚠️  BARDZO MAŁA ZMIENNOŚĆ - wyniki są prawie identyczne!")
    elif pred_cv < 5.0:
        print(f"  ⚠️  Mała zmienność - wyniki są bardzo podobne")
    else:
        print(f"  ✅ Normalna zmienność")
    
    # Chaos
    chaos_std = np.std(chaos_correlations)
    chaos_mean = np.mean(chaos_correlations)
    chaos_cv = (chaos_std / chaos_mean) * 100 if chaos_mean > 0 else 0
    
    print(f"\nChaos (różne fragmenty):")
    print(f"  Średnia: {chaos_mean:.6f}")
    print(f"  Odchylenie std: {chaos_std:.6f}")
    print(f"  Współczynnik zmienności: {chaos_cv:.4f}%")
    
    # Zależność od rozmiaru
    print(f"\nZależność od rozmiaru próbki:")
    print(f"  Kompresja: {compression_by_size}")
    comp_size_std = np.std(compression_by_size)
    print(f"    Odchylenie: {comp_size_std:.6f}")
    
    print(f"  Predykcja: {[f'{x:.4f}%' for x in prediction_by_size]}")
    pred_size_std = np.std(prediction_by_size)
    print(f"    Odchylenie: {pred_size_std:.4f}%")
    
    # Wnioski
    print("\n" + "="*60)
    print("WNIOSKI")
    print("="*60)
    
    if comp_cv < 1.0 and pred_cv < 1.0:
        print("\n⚠️  UWAGA: Wyniki są BARDZO SPÓJNE (prawie identyczne)")
        print("   To może oznaczać:")
        print("   1. π ma rzeczywiście stałe właściwości statystyczne")
        print("   2. Testy są zbyt uproszczone (nie wykrywają zmian)")
        print("   3. To jest własność losowości (równomierność)")
        print("\n   → Wymaga dalszej analizy!")
    else:
        print("\n✅ Wyniki mają normalną zmienność")
        print("   → Różne fragmenty π dają różne wyniki (jak powinno być)")

if __name__ == '__main__':
    main()

