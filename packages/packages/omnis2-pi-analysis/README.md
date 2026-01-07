# OMNIS2 Pi Analysis Package

## Opis

Pakiet zawierający kompleksową analizę statystyczną 10 miliardów cyfr liczby Pi przy użyciu 27 testów statystycznych (NIST + SmallCrush) z akceleracją GPU.

## Instalacja

```bash
# Z repozytorium GitHub
git clone https://github.com/Baver1022/omnis2-pi-analysis.git
cd omnis2-pi-analysis
git checkout OMNIS2
pip install -r requirements.txt
```

## Użycie

```bash
# Uruchomienie analizy
python3 analysis_orchestrator.py --pi-file pi_10billion.txt

# Sprawdzenie statusu
python3 analysis_orchestrator.py --status-only
```

## Zawartość Pakietu

- **27 testów statystycznych** (NIST + SmallCrush)
- **Wyniki analizy** (55 plików JSON)
- **Dokumentacja** (README, wzory matematyczne)
- **Kod źródłowy** (Python)

## Wymagania

- Python 3.8+
- NumPy, SciPy, Pandas
- Matplotlib (opcjonalne)
- CuPy (opcjonalne, dla GPU)

## Dokumentacja

Pełna dokumentacja dostępna w repozytorium:  
https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2

## Licencja

Zobacz plik LICENSE w repozytorium.

## Autor

baver
