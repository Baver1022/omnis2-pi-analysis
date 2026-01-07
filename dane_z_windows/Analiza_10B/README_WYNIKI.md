# Wyniki Analizy Statystycznej 10 Miliardów Cyfr Liczby Pi

## Opis

Ten katalog zawiera **55 plików JSON** z wynikami kompleksowej analizy statystycznej 10 miliardów cyfr liczby Pi przy użyciu 27 testów statystycznych (17 testów NIST + 10 testów SmallCrush).

## Struktura plików

- `01_results.json` - `27_results.json` (27 plików) - Szczegółowe wyniki poszczególnych testów statystycznych
- `01_status.json` - `27_status.json` (27 plików) - Status wykonania testów (czas, liczba przetworzonych cyfr)
- `analysis_summary.json` (1 plik) - Podsumowanie wszystkich testów z interpretacją wyników

**Łącznie: 55 plików JSON (~236 KB)**

## Format danych

### Pliki `XX_results.json` (27 plików)
Zawierają szczegółowe wyniki testów:
- `test_id` - ID testu (01-27)
- `test_name` - Nazwa testu
- `p_value` - Wartość p-value (jeśli dostępna)
- `result` - Wynik testu (PASS/FAIL/N/A)
- `statistics` - Szczegółowe statystyki testu
- `execution_time` - Czas wykonania testu
- `interpretation` - Interpretacja wyników

### Pliki `XX_status.json` (27 plików)
Zawierają metadane wykonania:
- `step_id` - ID kroku (01-27)
- `step_name` - Nazwa testu
- `status` - Status wykonania (completed/running/failed)
- `started_at` - Czas rozpoczęcia
- `completed_at` - Czas zakończenia
- `digits_processed` - Liczba przetworzonych cyfr
- `total_digits` - Całkowita liczba cyfr
- `error` - Informacje o błędach (jeśli wystąpiły)

### Plik `analysis_summary.json` (1 plik)
Zawiera agregowane podsumowanie wszystkich testów z interpretacją wyników.

## Kluczowe wyniki

### Testy PASS (~70%)
- Frequency Test (01)
- Runs Test (02)
- Block Frequency (03)
- Entropy Analysis (04) - H ≈ 3.32
- Universal Statistical (15)
- Overlapping Template (17)

### Testy FAIL (Granice losowości)
- Random Excursions (13) - p=0.0
- Random Excursions Variant (14) - p=0.0
- Non-overlapping Template (16) - p=2e-11
- BirthdaySpacings (18) - p=0.0
- SimplePoker (21) - p=0.0
- MaxOft (23) - p=0.0
- RandomWalk1 (27) - p=0.0

## Rozmiar danych

- **55 plików JSON** - łącznie ~236 KB
- Każdy plik zawiera szczegółowe wyniki jednego testu statystycznego

## Użycie

Wyniki mogą być wykorzystane do:
- Generowania raportów naukowych (LaTeX/PDF)
- Analizy porównawczej z innymi badaniami
- Weryfikacji hipotez o losowości cyfr Pi
- Zastosowań kryptograficznych

## Powiązane pliki

- `../analiza_wynikow_output/RAPORT_NAUKOWY_PI.pdf` - Raport naukowy PL (70+ stron)
- `../analiza_wynikow_output/RAPORT_NAUKOWY_PI_EN.pdf` - Raport naukowy EN (70+ stron)
- `../../WZORY_MATEMATYCZNE_27_TESTOW.pdf` - Dokumentacja wzorów matematycznych

## Licencja

Wyniki badań są częścią projektu OMNIS2 - Analiza Statystyczna 10 Miliardów Cyfr Liczby Pi.

