#!/usr/bin/env python3
"""
Wyciągnij pełny ciąg liczb przypisanych do voxela (0,0,0)
"""

import numpy as np
from pathlib import Path

def load_pi_digits(n=10_000_000):
    """Wczytaj cyfry π"""
    print(f"Wczytywanie {n:,} cyfr π...")
    digits = []
    chunk_size = 100_000_000
    files_needed = min(10, (n // chunk_size) + 1)
    pi_dir = Path("/home/baver/hexstrike-ai/OMNIS-PI-ENGINE/pi_10b_parts")
    
    for file_idx in range(1, files_needed + 1):
        start_pos = (file_idx - 1) * chunk_size + 1
        end_pos = file_idx * chunk_size
        filename = f"{start_pos}-{end_pos}.txt"
        filepath = pi_dir / filename
        
        print(f"  Wczytywanie {filename}...")
        
        if filepath.exists():
            with open(filepath, 'rb') as f:
                content = f.read(n * 2)
                content_arr = np.frombuffer(content, dtype=np.uint8)
                mask = (content_arr >= 48) & (content_arr <= 57)
                digits_found = content_arr[mask] - 48
                digits.extend(digits_found[:n - len(digits)])
                
                if len(digits) >= n:
                    break
    
    return np.array(digits[:n], dtype=np.uint8)

def extract_voxel_000(digits):
    """Wyciągnij wszystkie trójki (0,0,0) z ciągu π"""
    print(f"\nSzukanie trójek (0,0,0) w {len(digits):,} cyfrach...")
    
    count = len(digits) // 3
    voxel_000_data = []
    
    for i in range(count):
        idx = i * 3
        if idx + 2 >= len(digits):
            break
        
        x = int(digits[idx])
        y = int(digits[idx + 1])
        z = int(digits[idx + 2])
        
        # Jeśli to voxel (0,0,0)
        if x == 0 and y == 0 and z == 0:
            value_3digit = int(f"{digits[idx]}{digits[idx+1]}{digits[idx+2]}")
            voxel_000_data.append({
                'position': i,  # pozycja trójki w ciągu
                'digit_position': idx,  # pozycja pierwszej cyfry w ciągu π
                'triplet': (x, y, z),
                'value': value_3digit,
                'context_before': ''.join(map(str, digits[max(0, idx-5):idx])) if idx >= 5 else '',
                'context_after': ''.join(map(str, digits[idx+3:idx+8])) if idx+8 < len(digits) else ''
            })
    
    return voxel_000_data

def save_voxel_000_sequence(data, filename='voxel_0_0_0_ciag.txt'):
    """Zapisz ciąg liczb do pliku"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('='*80 + '\n')
        f.write('Ciąg liczb przypisanych do kwadratu (voxela) o położeniu (0,0,0)\n')
        f.write('='*80 + '\n\n')
        f.write(f'Znaleziono {len(data):,} trójek (0,0,0) w ciągu π\n\n')
        
        f.write('Format: [pozycja_trójki] wartość_3-cyfrowa | kontekst_przed ... (0,0,0) ... kontekst_po\n')
        f.write('-'*80 + '\n\n')
        
        # Zapisz wszystkie wartości
        for i, item in enumerate(data, 1):
            f.write(f"[{item['position']:8,}] {item['value']:03d}")
            
            # Dodaj kontekst jeśli dostępny
            if item['context_before'] or item['context_after']:
                f.write(f" | ...{item['context_before']} ({item['triplet'][0]},{item['triplet'][1]},{item['triplet'][2]}) {item['context_after']}...")
            
            f.write('\n')
            
            # Co 100 linii dodaj separator
            if i % 100 == 0:
                f.write(f'\n--- {i:,} / {len(data):,} ---\n\n')
        
        f.write('\n' + '='*80 + '\n')
        f.write('PODSUMOWANIE:\n')
        f.write('='*80 + '\n')
        f.write(f'Łączna liczba trójek (0,0,0): {len(data):,}\n')
        f.write(f'Wszystkie wartości 3-cyfrowe: 000 (bo to zawsze trójka (0,0,0))\n')
        f.write(f'Pozycje w ciągu π: od {data[0]["position"]:,} do {data[-1]["position"]:,}\n')
        
        # Statystyki odstępów
        if len(data) > 1:
            intervals = [data[i+1]['position'] - data[i]['position'] for i in range(len(data)-1)]
            f.write(f'\nStatystyki odstępów między trójkami:\n')
            f.write(f'  Średni odstęp: {np.mean(intervals):.2f} pozycji\n')
            f.write(f'  Minimalny odstęp: {min(intervals)} pozycji\n')
            f.write(f'  Maksymalny odstęp: {max(intervals)} pozycji\n')
    
    print(f"\n✅ Zapisano ciąg do: {filename}")
    return filename

def save_values_only(data, filename='voxel_0_0_0_wartosci.txt'):
    """Zapisz tylko wartości 3-cyfrowe (ciąg liczb)"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Ciąg wartości 3-cyfrowych z voxela (0,0,0):\n')
        f.write('='*80 + '\n\n')
        
        # Zapisz wszystkie wartości w jednej linii (dla łatwego kopiowania)
        values = [f"{item['value']:03d}" for item in data]
        f.write(' '.join(values))
        f.write('\n\n')
        
        # Zapisz w formacie z pozycjami
        f.write('Z pozycjami:\n')
        f.write('-'*80 + '\n')
        for i, item in enumerate(data, 1):
            f.write(f"{item['value']:03d} (pozycja {item['position']:,})")
            if i % 10 == 0:
                f.write('\n')
            else:
                f.write(' | ')
        f.write('\n')
    
    print(f"✅ Zapisano wartości do: {filename}")
    return filename

if __name__ == '__main__':
    # Wczytaj dane
    digits = load_pi_digits(10_000_000)  # 10M cyfr
    
    # Wyciągnij voxel (0,0,0)
    voxel_data = extract_voxel_000(digits)
    
    print(f"\nZnaleziono {len(voxel_data):,} trójek (0,0,0)")
    
    # Zapisz pełny ciąg
    save_voxel_000_sequence(voxel_data)
    
    # Zapisz tylko wartości
    save_values_only(voxel_data)
    
    print("\n✅ Gotowe!")

