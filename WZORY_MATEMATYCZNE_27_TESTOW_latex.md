# Wzory Matematyczne - 27 Testów Statystycznych dla Analizy Pi

## NIST Statistical Test Suite (17 testów)

### Step 01 - Frequency Test (Test Częstotliwości)

**Wzór Chi-square:**
```
$\chi^2$ = $\sum$ᵢ₌₀⁹ (fᵢ - n/10)$^2$ / (n/10)
```

**Gdzie:**
- `fᵢ` = częstotliwość cyfry `i` (0-9)
- `n` = całkowita liczba cyfr
- `E[fᵢ] = n/10` = oczekiwana częstotliwość każdej cyfry

**P-value:**
```
p-value = 1 - CDF($\chi^2$, df=9)
```

---

### Step 02 - Runs Test (Test Przejść)

**Oczekiwana liczba runs:**
```
E[runs] = 2 $\cdot$ ones $\cdot$ zeros / n
```

**Wariancja:**
```
Var[runs] = (2 $\cdot$ ones $\cdot$ zeros $\cdot$ (2 $\cdot$ ones $\cdot$ zeros - n)) / (n$^2$ $\cdot$ (n-1))
```

**Z-score:**
```
Z = (runs - E[runs]) / $\sqrt{}$Var[runs]
```

**P-value:**
```
p-value = 2 $\cdot$ (1 - $\Phi$(|Z|))
```

**Gdzie:**
- `ones` = liczba nieparzystych cyfr
- `zeros` = liczba parzystych cyfr
- `runs` = liczba przejść między parzystymi a nieparzystymi

---

### Step 03 - Block Frequency Test (Test Częstotliwości w Blokach)

**Chi-square dla bloków:**
```
$\chi^2$ = $\sum$ⱼ (ones_per_blockⱼ - block_size/2)$^2$ / (block_size/2)
```

**Gdzie:**
- `ones_per_blockⱼ` = liczba jedynek w bloku `j`
- `block_size` = rozmiar bloku
- `E[ones] = block_size/2` = oczekiwana liczba jedynek w bloku

**P-value:**
```
p-value = 1 - CDF($\chi^2$, df=num_blocks)
```

---

### Step 04 - Entropy Test (Test Entropii)

**Entropia Shannona:**
```
H(X) = -$\sum$ₓ₌₀⁹ p(x) $\cdot$ $\log_2$(p(x))
```

**Gdzie:**
- `p(x) = count(x) / n` = prawdopodobieństwo wystąpienia cyfry `x`
- `H_max = log₂(10) ≈ 3.321928` = maksymalna entropia dla 10 cyfr

**Stosunek entropii:**
```
ratio = H(X) / H_max
```

---

### Step 05 - Spectral FFT Test (Test Spektralny FFT)

**Transformata Fouriera:**
```
X[k] = $\sum$ₙ₌₀ᴺ⁻¹ x[n] $\cdot$ e^(-2$\pi$ikn/N)
```

**Widmo mocy:**
```
P[k] = |X[k]|$^2$
```

**Entropia spektralna:**
```
H_s = -$\sum$ₖ (P[k]/$\sum$P) $\cdot$ $\log_2$(P[k]/$\sum$P + ε)
```

**Gdzie:**
- `x[n]` = pary cyfr (digits[i]·10 + digits[i+1])
- `ε = 1e-10` = mała stała dla stabilności numerycznej

---

### Step 06 - Compression Test (Test Kompresji)

**Współczynnik kompresji:**
```
compression_ratio = compressed_size / original_size
```

**Gdzie:**
- `original_size` = rozmiar oryginalnych danych (cyfry jako string)
- `compressed_size` = rozmiar po kompresji zlib (level 9)

**Interpretacja:** Niższy współczynnik = większa losowość

---

### Step 07 - Empirical Entropy Bounds (Empiryczne Granice Entropii)

**Model entropii:**
```
H(N) = $\log_2$(10) $\cdot$ (1 - c/log(N))
```

**Gdzie:**
- `N` = liczba analizowanych cyfr
- `c` = parametr dopasowania (estymowany przez curve fitting)
- `H_max = log₂(10) ≈ 3.321928`

**Dopasowanie modelu:**
```
c = argmin $\sum$ (H_observed(N) - H_model(N, c))$^2$
```

**Confidence interval (95%):**
```
CI = c ± 1.96 $\cdot$ σ_c
```

---

### Step 09 - Cumulative Sums Test (Test Skumulowanych Sum)

**Forward cumulative sum:**
```
S_forward[i] = $\sum$ⱼ₌₀ⁱ (2$\cdot$binary[j] - 1)
```

**Backward cumulative sum:**
```
S_backward[i] = $\sum$ⱼ₌ᵢⁿ (2$\cdot$binary[j] - 1)
```

**Maksymalna wartość:**
```
max_forward = max |S_forward[i]|
max_backward = max |S_backward[i]|
```

**Oczekiwana wartość:**
```
E[max] $\approx$ 0.95 $\cdot$ $\sqrt{}$n
```

**Z-score:**
```
Z_forward = max_forward / $\sqrt{}$n
Z_backward = max_backward / $\sqrt{}$n
```

**P-value:**
```
p-value = min(1 - $\Phi$(Z_forward), 1 - $\Phi$(Z_backward))
```

**Gdzie:**
- `binary[j] = digits[j] % 2` = konwersja na binarną (0 lub 1)

---

### Step 10 - Approximate Entropy Test (Test Przybliżonej Entropii)

**Przybliżona entropia:**
```
ApEn(m) = φ(m) - φ(m+1)
```

**Gdzie:**
```
φ(m) = -$\sum$_pattern p(pattern) $\cdot$ $\log_2$(p(pattern))
```

**P-value (uproszczony):**
```
$\chi^2$ = (ApEn - 0)$^2$ / 0.1
p-value = 1 - CDF($\chi^2$, df=1)
```

**Gdzie:**
- `m` = długość wzorca (zwykle m=2)
- `p(pattern)` = częstotliwość wzorca w sekwencji

---

### Step 11 - Serial Test (Test Seryjny)

**Chi-square dla par:**
```
$\chi^2$_pairs = $\sum$_pair (count_pair - expected)$^2$ / expected
```

**Gdzie:**
- `expected = n_pairs / 100` (100 możliwych par: 00-99)
- `n_pairs = n - 1` = liczba par

**Chi-square dla trójek:**
```
$\chi^2$_triplets = $\sum$_triplet (count_triplet - expected)$^2$ / expected
```

**Gdzie:**
- `expected = n_triplets / 1000` (1000 możliwych trójek: 000-999)
- `n_triplets = n - 2` = liczba trójek

**P-value:**
```
p-value = min(p-value_pairs, p-value_triplets)
```

---

### Step 12 - Linear Complexity Test (Test Złożoności Liniowej)

**Algorytm Berlekamp-Massey:**
```
L = Berlekamp-Massey(sequence)
```

**Oczekiwana złożoność:**
```
E[L] = M/2 + (9 + (-1)^(M+1)) / 36
```

**Gdzie:**
- `M` = długość bloku (zwykle M=500)
- `L` = długość najkrótszego LFSR generującego sekwencję

**Chi-square test:**
```
$\chi^2$ = $\sum$ (observed_complexity - expected)$^2$ / expected
```

---

### Step 13 - Random Excursions Test (Test Losowych Wycieczek)

**Random walk:**
```
S[i] = $\sum$ⱼ₌₀ⁱ (2$\cdot$binary[j] - 1)
```

**Oczekiwana liczba odwiedzin stanu x:**
```
E[visits(x)] = 1 / (2|x|)  dla |x| $\geq$ 1
E[visits(0)] = 0.5
```

**Prawdopodobieństwa:**
```
p₀ = 1 - E[visits]
p₁ = E[visits] $\cdot$ (1 - E[visits])
p₂₊ = E[visits]$^2$
```

**Chi-square:**
```
$\chi^2$ = $\sum$ (observed - expected)$^2$ / expected
```

**Gdzie:**
- `x ∈ {-4, -3, -2, -1, 1, 2, 3, 4}` = stany do analizy

---

### Step 14 - Random Excursions Variant Test (Wariant Testu Losowych Wycieczek)

**Oczekiwana liczba odwiedzin:**
```
E[visits(x)] = n / (2|x|)  dla |x| $\geq$ 1
E[visits(0)] = n / 2
```

**Chi-square:**
```
$\chi^2$ = (observed - expected)$^2$ / expected
```

**Gdzie:**
- `x ∈ {-9, -8, ..., -1, 1, 2, ..., 9}` = stany do analizy
- `n` = liczba kroków w random walk

---

### Step 15 - Universal Statistical Test (Test Uniwersalny Statystyczny)

**Statystyka testowa:**
```
f_n = (1/K) $\cdot$ $\sum$ $\log_2$(distance)
```

**Gdzie:**
- `distance` = odległość między powtórzeniami wzorca
- `K` = liczba bloków

**Oczekiwana wartość (dla L=6):**
```
E[f_n] $\approx$ 5.2177052
Var[f_n] $\approx$ 2.954
```

**Z-score:**
```
Z = (f_n - E[f_n]) / $\sqrt{}$(Var[f_n]/K)
```

**P-value:**
```
p-value = 2 $\cdot$ (1 - $\Phi$(|Z|))
```

---

### Step 16 - Non-overlapping Template Matching Test

**Oczekiwana liczba wystąpień:**
```
E[matches] = n / (2^m + m - 1)
```

**Gdzie:**
- `m` = długość wzorca binarnego
- `n` = długość sekwencji binarnej

**Chi-square:**
```
$\chi^2$ = (matches - E[matches])$^2$ / E[matches]
```

**P-value:**
```
p-value = 1 - CDF($\chi^2$, df=1)
```

---

### Step 17 - Overlapping Template Matching Test

**Oczekiwana liczba wystąpień:**
```
E[matches] = (n - m + 1) / 2^m
```

**Gdzie:**
- `m` = długość wzorca binarnego
- `n` = długość sekwencji binarnej

**Chi-square:**
```
$\chi^2$ = (matches - E[matches])$^2$ / E[matches]
```

**P-value:**
```
p-value = 1 - CDF($\chi^2$, df=1)
```

---

## SmallCrush Test Suite (10 testów)

### Step 18 - Birthday Spacings Test

**Rozkład odstępów:**
```
P(spacing = k) = (1 - 1/m)^k $\cdot$ (1/m)
```

**Gdzie:**
- `m` = zakres wartości (10 dla cyfr 0-9)
- `spacing` = odległość między powtarzającymi się wartościami

**Chi-square:**
```
$\chi^2$ = $\sum$ (observed_spacings - expected)$^2$ / expected
```

---

### Step 19 - Collision Test

**Oczekiwana liczba kolizji:**
```
E[collisions] = t - m + m $\cdot$ (1 - 1/m)^t
```

**Gdzie:**
- `t` = liczba próbek
- `m` = zakres wartości (10 dla cyfr 0-9)
- `collisions` = liczba powtórzeń wartości

**Chi-square:**
```
$\chi^2$ = (collisions - E[collisions])$^2$ / E[collisions]
```

---

### Step 20 - Gap Test

**Rozkład geometryczny:**
```
P(gap = k) = (1-p)^k $\cdot$ p
```

**Gdzie:**
- `p = 1/m` = prawdopodobieństwo wystąpienia wartości docelowej
- `m` = zakres wartości (10 dla cyfr 0-9)

**Chi-square:**
```
$\chi^2$ = $\sum$ (observed_gaps - expected)$^2$ / expected
```

---

### Step 21 - Simple Poker Test

**Prawdopodobieństwo k unikalnych wartości w bloku 5:**
```
P(k unique) = $C(5,k)$ $\cdot$ P(permutation) / 10^5
```

**Gdzie:**
- `C(5,k)` = kombinacja 5 po k
- `P(permutation)` = prawdopodobieństwo permutacji

**Chi-square:**
```
$\chi^2$ = $\sum$ₖ₌₁⁵ (observed(k) - expected(k))$^2$ / expected(k)
```

---

### Step 22 - Coupon Collector Test

**Oczekiwana długość:**
```
E[length] = m $\cdot$ H_m
```

**Gdzie:**
- `H_m = Σₖ₌₁ᵐ 1/k` = liczba harmoniczna
- `m = 10` = liczba różnych wartości (cyfry 0-9)

**Z-test:**
```
Z = (observed_mean - E[length]) / (std / $\sqrt{}$n_trials)
```

**P-value:**
```
p-value = 2 $\cdot$ (1 - $\Phi$(|Z|))
```

---

### Step 23 - MaxOft Test

**Rozkład maksimum:**
```
P(max $\leq$ k) = (k/9)^t
```

**Gdzie:**
- `t` = liczba próbek w grupie (zwykle t=5)
- `k ∈ {0, 1, 2, ..., 9}` = wartości cyfr

**Prawdopodobieństwo:**
```
P(max = k) = (k/9)^t - ((k-1)/9)^t
```

**Chi-square:**
```
$\chi^2$ = $\sum$ (observed - expected)$^2$ / expected
```

---

### Step 24 - Weight Distribution Test

**Oczekiwana suma:**
```
E[sum] = block_size $\cdot$ 4.5
```

**Gdzie:**
- `block_size` = rozmiar bloku (zwykle 10)
- `4.5` = średnia cyfr 0-9

**Z-test:**
```
Z = (observed_mean - E[sum]) / (std / $\sqrt{}$n_blocks)
```

**P-value:**
```
p-value = 2 $\cdot$ (1 - $\Phi$(|Z|))
```

---

### Step 25 - Matrix Rank Test

**Ranga macierzy:**
```
rank = matrix_rank(binary_matrix)
```

**Gdzie:**
- `binary_matrix` = macierz binarna 32×32 utworzona z sekwencji binarnej

**Test:** Sprawdza rozkład rang macierzy binarnych (większość powinna mieć pełną rangę)

**Chi-square:**
```
$\chi^2$ = $\sum$ (observed_ranks - expected)$^2$ / expected
```

---

### Step 26 - Hamming Independence Test

**Rozkład binarny:**
```
P(weight = k) = $C(\text{block\_size}, k)$ $\cdot$ 0.5^block_size
```

**Gdzie:**
- `weight` = liczba jedynek w bloku binarnym
- `block_size` = rozmiar bloku (zwykle 32)
- `C(n,k)` = kombinacja n po k

**Oczekiwana waga:**
```
E[weight] = block_size / 2
```

**Chi-square:**
```
$\chi^2$ = $\sum$ (observed_weights - expected)$^2$ / expected
```

---

### Step 27 - Random Walk 1 Test

**Random walk:**
```
S[i] = $\sum$ⱼ₌₀ⁱ (2$\cdot$binary[j] - 1)
```

**Gdzie:**
- `binary[j] = digits[j] % 2` = konwersja na binarną
- `S[i]` = skumulowana suma (random walk)

**Test:** Sprawdza rozkład wartości `S[i]` (powinien być normalny dla losowej sekwencji)

---

## Wzory Ogólne

### Chi-square Test
```
$\chi^2$ = $\sum$ (observed - expected)$^2$ / expected
p-value = 1 - CDF($\chi^2$, df)
```

### Z-test
```
Z = (observed - expected) / (std / $\sqrt{}$n)
p-value = 2 $\cdot$ (1 - $\Phi$(|Z|))
```

### Entropia Shannona
```
H(X) = -$\sum$ p(x) $\cdot$ $\log_2$(p(x))
```

### P-value Interpretation
- `p-value ≥ 0.01` → **PASS** (sekwencja jest losowa)
- `p-value < 0.01` → **FAIL** (sekwencja nie jest losowa)

---

## Notacja

- `Σ` = suma
- `E[...]` = wartość oczekiwana
- `Var[...]` = wariancja
- `C(n,k)` = kombinacja n po k
- `Φ(x)` = dystrybuanta rozkładu normalnego
- `CDF(x, df)` = dystrybuanta rozkładu chi-square
- `log₂(x)` = logarytm o podstawie 2
- `√x` = pierwiastek kwadratowy
- `|x|` = wartość bezwzględna

---

**Data utworzenia:** 2024  
**Liczba testów:** 27 (17 NIST + 10 SmallCrush)  
**Zastosowanie:** Analiza statystyczna 10 miliardów cyfr liczby Pi

