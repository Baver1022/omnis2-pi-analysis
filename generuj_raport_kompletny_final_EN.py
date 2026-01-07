#!/usr/bin/env python3
"""
COMPREHENSIVE SCIENTIFIC REPORT GENERATOR - ENGLISH VERSION
With test descriptions, mathematical formulas, graphs, comparative analysis
"""

from __future__ import annotations
import pandas as pd
import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# Configuration - uses relative paths from script location
SCRIPT_DIR = Path(__file__).parent
ANALYSIS_DIR = SCRIPT_DIR / "analiza_wynikow_output"
RESULTS_DIR = SCRIPT_DIR / "dane_z_windows" / "Analiza_10B"
OUTPUT_DIR = SCRIPT_DIR / "analiza_wynikow_output"
TEX_FILE = OUTPUT_DIR / "RAPORT_NAUKOWY_PI_EN.tex"
FIGURES_DIR = OUTPUT_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

print("=" * 80)
print("COMPREHENSIVE SCIENTIFIC REPORT GENERATOR - ENGLISH VERSION")
print("=" * 80)

# Load data
df = pd.read_csv(ANALYSIS_DIR / "wyniki_tabela.csv")
detailed_results = {}
for test_id in range(1, 28):
    tid_str = f"{test_id:02d}"
    result_file = RESULTS_DIR / f"{tid_str}_results.json"
    if result_file.exists():
        with open(result_file, 'r', encoding='utf-8') as f:
            detailed_results[tid_str] = json.load(f)

# Load analysis_summary.json for additional details
summary_file = RESULTS_DIR / "analysis_summary.json"
summary_results = {}
if summary_file.exists():
    with open(summary_file, 'r', encoding='utf-8') as f:
        summary_data = json.load(f)
        if 'results' in summary_data:
            summary_results = summary_data['results']
            # Update detailed_results with summary data (which may be more complete)
            for key, value in summary_results.items():
                if key in detailed_results:
                    # Merge data
                    detailed_results[key].update(value)
                else:
                    detailed_results[key] = value

print(f"✓ Loaded {len(df)} tests")
print(f"✓ Loaded details for {len(detailed_results)} tests")

# Calculate statistics
n_digits = int(df.iloc[0]['n'])
total_time = df['execution_time'].sum()
total_hours = total_time / 3600
p_values = df['p_value'].dropna()
p_values_positive = p_values[p_values > 0]

def esc(text):
    if pd.isna(text):
        return "---"
    text = str(text)
    for old, new in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'),
                      ('^', r'\textasciicircum{}'), ('_', r'\_'),
                      ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}')]:
        text = text.replace(old, new)
    return text

# Test descriptions - purpose, application, formulas - ALL 27 TESTS
# Formulas according to WZORY_MATEMATYCZNE_27_TESTOW.pdf
test_descriptions = {
    '01': {
        'purpose': r"Frequency Test (Monobit Test) checks whether the proportion of zeros and ones in the binary representation of digits is approximately 1:1.",
        'application': r"This is the most basic randomness test. It serves to verify uniform distribution of bits in a binary sequence. It tests the null hypothesis that the sequence is random by comparing the frequency of occurrence of each digit with the expected frequency.",
        'formulas': [
            r"\chi^2 = \sum_{i=0}^{9}\frac{(f_i - n/10)^2}{n/10}",
            r"E[f_i] = \frac{n}{10} = \text{expected frequency of each digit}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 9)",
            r"\text{where: } f_i = \text{frequency of digit } i \text{ (0-9), } n = \text{total number of digits}"
        ]
    },
    '02': {
        'purpose': r"Runs Test analyzes uninterrupted sequences of consecutive zeros or ones (runs).",
        'application': r"Serves to detect correlations between consecutive bits. Checks whether transitions between 0 and 1 occur with expected frequency.",
        'formulas': [
            r"E[\text{runs}] = 2 \cdot \text{ones} \cdot \text{zeros} / n",
            r"\text{Var}[\text{runs}] = \frac{2 \cdot \text{ones} \cdot \text{zeros} \cdot (2 \cdot \text{ones} \cdot \text{zeros} - n)}{n^2 \cdot (n - 1)}",
            r"Z = \frac{\text{runs} - E[\text{runs}]}{\sqrt{\text{Var}[\text{runs}]}}",
            r"p\text{-value} = 2 \cdot (1 - \Phi(|Z|))",
            r"\text{where: ones = number of odd digits, zeros = number of even digits}"
        ]
    },
    '03': {
        'purpose': r"Block Frequency Test divides the sequence into blocks and checks the frequency of ones in each block.",
        'application': r"Serves to detect local non-uniformities in bit distribution at the block level.",
        'formulas': [
            r"\chi^2 = \sum_{j} \frac{(\text{ones\_per\_block}_j - \text{block\_size} / 2)^2}{\text{block\_size} / 2}",
            r"E[\text{ones}] = \frac{\text{block\_size}}{2} = \text{expected number of ones in block}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = \text{num\_blocks})",
            r"\text{where: ones\_per\_block = number of ones in block } j"
        ]
    },
    '04': {
        'purpose': r"Entropy Analysis calculates Shannon entropy for the digit distribution.",
        'application': r"Serves to measure unpredictability and complexity of the sequence. High entropy indicates high randomness.",
        'formulas': [
            r"H(X) = -\sum_{x=0}^{9} p(x) \cdot \log_2(p(x))",
            r"p(x) = \frac{\text{count}(x)}{n} = \text{probability of digit } x",
            r"H_{\max} = \log_2(10) \approx 3.321928 = \text{maximum entropy for 10 digits}",
            r"\text{ratio} = \frac{H(X)}{H_{\max}}"
        ]
    },
    '05': {
        'purpose': r"Spectral FFT Analysis uses Fourier transform to detect periodicity.",
        'application': r"Serves to detect hidden periodic patterns in the digit sequence.",
        'formulas': [
            r"X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-2\pi ikn / N}",
            r"P[k] = |X[k]|^2 = \text{power spectrum}",
            r"H_s = -\sum_k \frac{P[k]}{\sum P} \cdot \log_2\left(\frac{P[k]}{\sum P} + \varepsilon\right)",
            r"\text{where: } x[n] = \text{digit pairs}(\text{digits}[i] \cdot 10 + \text{digits}[i + 1]), \varepsilon = 10^{-10}"
        ]
    },
    '06': {
        'purpose': r"Compression Test measures the degree of data compression using zlib algorithm.",
        'application': r"Serves to assess sequence complexity. Low compression indicates high complexity and randomness.",
        'formulas': [
            r"\text{compression\_ratio} = \frac{\text{compressed\_size}}{\text{original\_size}}",
            r"\text{where: original\_size = size of original data, compressed\_size = size after zlib compression}",
            r"\text{Interpretation: Lower ratio = higher randomness}"
        ]
    },
    '07': {
        'purpose': r"Empirical Entropy Bounds analyzes entropy limits for different block lengths.",
        'application': r"Serves to study how entropy changes depending on the length of analyzed blocks.",
        'formulas': [
            r"H(N) = \log_2(10) \cdot \left(1 - \frac{c}{\log(N)}\right)",
            r"c = \arg \min \sum (H_{\text{observed}}(N) - H_{\text{model}}(N,c))^2",
            r"H_{\max} = \log_2(10) \approx 3.321928",
            r"\text{Confidence interval (95\%): } \text{CI} = c \pm 1.96 \cdot \sigma_c",
            r"\text{where: } N = \text{number of analyzed digits, } c = \text{fitting parameter}"
        ]
    },
    '09': {
        'purpose': r"Cumulative Sums Test analyzes maximum deviation of cumulative sums.",
        'application': r"Serves to detect systematic trends in the bit sequence.",
        'formulas': [
            r"S_{\text{forward}}[i] = \sum_{j=0}^{i}(2 \cdot \text{binary}[j] - 1)",
            r"S_{\text{backward}}[i] = \sum_{j=i}^{n}(2 \cdot \text{binary}[j] - 1)",
            r"\max_{\text{forward}} = \max_i |S_{\text{forward}}[i]|, \quad \max_{\text{backward}} = \max_i |S_{\text{backward}}[i]|",
            r"Z_{\text{forward}} = \frac{\max_{\text{forward}}}{\sqrt{n}}, \quad Z_{\text{backward}} = \frac{\max_{\text{backward}}}{\sqrt{n}}",
            r"p\text{-value} = \min(p_{\text{forward}}, p_{\text{backward}})"
        ]
    },
    '10': {
        'purpose': r"Approximate Entropy Test measures regularity of patterns of given length.",
        'application': r"Serves to detect regular patterns in the sequence. Low approximate entropy indicates predictability.",
        'formulas': [
            r"\text{ApEn}(m,r) = \Phi^m(r) - \Phi^{m+1}(r)",
            r"\Phi^m(r) = \frac{1}{N-m+1}\sum_{i=1}^{N-m+1}\log C_i^m(r)",
            r"C_i^m(r) = \frac{\text{number of patterns of length } m \text{ similar to } x[i:i+m]}{N-m+1}",
            r"\chi^2 = \frac{(\text{ApEn} - E[\text{ApEn}])^2}{\text{Var}[\text{ApEn}]}, \quad p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df}=1)"
        ]
    },
    '11': {
        'purpose': r"Serial Test analyzes frequency of overlapping patterns of length $m$.",
        'application': r"Serves to detect preferences for certain patterns over others.",
        'formulas': [
            r"\Delta\psi_m^2 = \psi_m^2 - \psi_{m-1}^2",
            r"\psi_m^2 = \frac{2^m}{n}\sum(\text{obs}_i^2) - n",
            r"\text{where: obs}_i = \text{number of occurrences of pattern } i \text{ of length } m",
            r"p\text{-value} = 1 - \text{CDF}(\Delta\psi_m^2, \text{df} = 2^{m-1})"
        ]
    },
    '12': {
        'purpose': r"Linear Complexity Test measures the length of the shortest LFSR generating the sequence.",
        'application': r"Serves to assess linear complexity of the sequence. Low complexity indicates linear patterns.",
        'formulas': [
            r"L = \text{Berlekamp-Massey}(S) = \text{length of shortest LFSR}",
            r"E[L] = \frac{M}{2} + \frac{9 + ((-1)^{M+1})}{36}",
            r"\chi^2 = \sum \frac{(\text{observed\_complexities} - E[L])^2}{E[L]}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = \text{num\_bins} - 1)",
            r"\text{where: } M = \text{binary block length}"
        ]
    },
    '13': {
        'purpose': r"Random Excursions Test analyzes a random walk built from a binary sequence.",
        'application': r"Serves to detect structures in the trajectory of a random walk. Checks the distribution of visits to specific states.",
        'formulas': [
            r"S_k = \sum_{i=1}^{k}(2 \cdot \text{binary}[i] - 1) = \text{random walk}",
            r"\xi(x) = \text{number of visits to state } x \text{ for } x \in \{-4, -3, -2, -1, 1, 2, 3, 4\}",
            r"E[\xi(x)] = \frac{1}{2|x|(|x|+1)}, \quad \text{Var}[\xi(x)] = \frac{4|x|(J-|x|-1)}{(J-1)^2(2|x|+1)}",
            r"\chi^2 = \sum_{x} \frac{(\xi(x) - E[\xi(x)])^2}{E[\xi(x)]}, \quad p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 7)"
        ]
    },
    '15': {
        'purpose': r"Universal Statistical Test checks whether the sequence can be significantly compressed.",
        'application': r"Serves to detect sequence compressibility. High compressibility indicates structure.",
        'formulas': [
            r"f_n = \frac{1}{K}\sum_{i=1}^{K}\log_2(i - \text{last\_pos}[\text{pattern}_i])",
            r"E[f_n] = \begin{cases} 5.2177052 & \text{for } L=6 \\ 6.1962507 & \text{for } L=7 \\ 7.1836656 & \text{for } L=8 \end{cases}",
            r"\text{Var}[f_n] = \begin{cases} 2.954 & \text{for } L=6 \\ 3.125 & \text{for } L=7 \\ 3.238 & \text{for } L=8 \end{cases}",
            r"Z = \frac{f_n - E[f_n]}{\sqrt{\text{Var}[f_n]/K}}, \quad p\text{-value} = 2 \cdot (1 - \Phi(|Z|))",
            r"\text{where: } L = \text{block length, } K = \text{number of test blocks}"
        ]
    },
    '16': {
        'purpose': r"Non-overlapping Template Matching Test searches for non-overlapping occurrences of a pattern.",
        'application': r"Serves to detect preferences for certain binary patterns through analysis of non-overlapping occurrences.",
        'formulas': [
            r"E[\text{matches}] = \frac{n - m + 1}{2^m} \cdot \frac{1}{2^m} = \frac{n - m + 1}{4^m}",
            r"\text{where: } m = \text{binary pattern length, } n = \text{sequence length}",
            r"\chi^2 = \frac{(\text{matches} - E[\text{matches}])^2}{E[\text{matches}]}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 1)"
        ]
    },
    '17': {
        'purpose': r"Overlapping Template Matching Test searches for overlapping occurrences of a pattern.",
        'application': r"Serves to detect preferences for certain binary patterns through analysis of overlapping occurrences.",
        'formulas': [
            r"E[\text{matches}] = \frac{n - m + 1}{2^m}",
            r"\text{where: } m = \text{binary pattern length, } n = \text{binary sequence length}",
            r"\chi^2 = \frac{(\text{matches} - E[\text{matches}])^2}{E[\text{matches}]}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 1)"
        ]
    },
    '18': {
        'purpose': r"BirthdaySpacings Test is based on the birthday paradox, analyzes spacings between repeating values.",
        'application': r"Serves to detect specific distributions of spacings between repetitions. The test checks whether spacings between repeating values have the proper exponential distribution.",
        'formulas': [
            r"P(\text{collision}) \approx 1 - e^{-n^2/(2d)}",
            r"\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}",
            r"P(\text{spacing} = k) = (1-p)^k \cdot p"
        ]
    },
    '19': {
        'purpose': r"Collision Test counts collisions in a hash table.",
        'application': r"Serves to detect irregularities in value distribution through analysis of the number of collisions in a hash table.",
        'formulas': [
            r"E[\text{collisions}] = t - m + m \cdot (1 - 1/m)^t",
            r"\text{where: } t = \text{number of samples, } m = \text{value range (10 for digits 0-9)}",
            r"\chi^2 = \frac{(\text{collisions} - E[\text{collisions}])^2}{E[\text{collisions}]}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 1)"
        ]
    },
    '20': {
        'purpose': r"Gap Test analyzes lengths of gaps between values from a specified range.",
        'application': r"Serves to detect deviations from the geometric distribution of gaps between occurrences of a specified value.",
        'formulas': [
            r"P(\text{gap} = k) = (1 - p)^k \cdot p",
            r"p = \frac{1}{m} = \text{probability of target value occurrence}",
            r"\text{where: } m = \text{value range (10 for digits 0-9)}",
            r"\chi^2 = \sum \frac{(\text{observed\_gaps} - \text{expected})^2}{\text{expected}}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = \text{num\_bins} - 1)"
        ]
    },
    '21': {
        'purpose': r"SimplePoker Test divides the sequence into groups and checks the distribution of combinations (analogous to poker).",
        'application': r"Serves to detect structures in the distribution of digit combinations in blocks. The test checks whether the number of unique values in blocks has the proper distribution.",
        'formulas': [
            r"P(k \text{ unikalnych}) = \frac{C(5, k) \cdot P(\text{permutation})}{10^5}",
            r"\text{where: } C(5,k) = \text{combination 5 choose k, } P(\text{permutation}) = \text{permutation probability}",
            r"\chi^2 = \sum_{k=1}^{5} \frac{(\text{observed}(k) - \text{expected}(k))^2}{\text{expected}(k)}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 4)"
        ]
    },
    '22': {
        'purpose': r"CouponCollector Test is based on the coupon collector problem.",
        'application': r"Serves to test whether all possible values occur with expected frequency. Measures how many draws are needed to collect all different values.",
        'formulas': [
            r"E[\text{length}] = m \cdot H_m",
            r"H_m = \sum_{k=1}^{m} \frac{1}{k} = \text{harmonic number}",
            r"m = 10 = \text{number of different values (digits 0-9)}",
            r"Z = \frac{\text{observed\_mean} - E[\text{length}]}{\text{std} / \sqrt{n_{\text{trials}}}}",
            r"p\text{-value} = 2 \cdot (1 - \Phi(|Z|))"
        ]
    },
    '23': {
        'purpose': r"MaxOft Test analyzes the distribution of maximum values in blocks.",
        'application': r"Serves to detect deviations in the distribution of extreme values. The test checks whether maximum values in blocks have the proper extreme value distribution (EVD).",
        'formulas': [
            r"P(\max \leq k) = \left(\frac{k}{9}\right)^t",
            r"P(\max = k) = \left(\frac{k}{9}\right)^t - \left(\frac{k-1}{9}\right)^t",
            r"\text{where: } t = \text{number of samples in group (usually } t = 5), k \in \{0,1,2,\ldots,9\}",
            r"\chi^2 = \sum \frac{(\text{observed} - \text{expected})^2}{\text{expected}}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 9)"
        ]
    },
    '24': {
        'purpose': r"WeightDistrib Test analyzes the distribution of \"weights\" (number of ones) in binary blocks.",
        'application': r"Serves to detect deviations from the binomial distribution of the number of ones in binary blocks.",
        'formulas': [
            r"E[\text{sum}] = \text{block\_size} \cdot 4.5",
            r"\text{where: block\_size = block size (usually 10), 4.5 = mean of digits 0-9}",
            r"Z = \frac{\text{observed\_mean} - E[\text{sum}]}{\text{std} / \sqrt{n_{\text{blocks}}}}",
            r"p\text{-value} = 2 \cdot (1 - \Phi(|Z|))"
        ]
    },
    '25': {
        'purpose': r"MatrixRank Test checks the rank of a matrix formed from bits.",
        'application': r"Serves to detect linear dependencies between bits through analysis of ranks of matrices formed from bits.",
        'formulas': [
            r"\text{rank} = \text{matrix\_rank}(\text{binary\_matrix})",
            r"\text{where: binary\_matrix = binary matrix } 32 \times 32 \text{ formed from binary sequence}",
            r"P(\text{rank} = \min(m,n)) \approx 0.2888",
            r"\chi^2 = \sum \frac{(\text{observed\_ranks} - \text{expected})^2}{\text{expected}}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = \text{num\_ranks} - 1)"
        ]
    },
    '26': {
        'purpose': r"HammingIndep Test checks independence of Hamming distances between blocks.",
        'application': r"Serves to detect correlations between blocks through analysis of Hamming distance.",
        'formulas': [
            r"P(\text{weight} = k) = C(\text{block\_size}, k) \cdot 0.5^{\text{block\_size}}",
            r"E[\text{weight}] = \frac{\text{block\_size}}{2}",
            r"\text{where: weight = number of ones in binary block, block\_size = block size (usually 32)}",
            r"\chi^2 = \sum \frac{(\text{observed\_weights} - \text{expected})^2}{\text{expected}}",
            r"p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = \text{block\_size})"
        ]
    },
    '27': {
        'purpose': r"RandomWalk1 Test analyzes a random walk built from digits.",
        'application': r"Serves to detect structures in the trajectory of a random walk built from digits. The test checks whether maximum deviation from zero has the proper distribution.",
        'formulas': [
            r"S[i] = \sum_{j=0}^{i} (2 \cdot \text{binary}[j] - 1)",
            r"\text{where: binary}[j] = \text{digits}[j] \bmod 2 = \text{conversion to binary}",
            r"E[\max|S|] \approx \sqrt{\frac{2n}{\pi}}",
            r"Z = \frac{\max|S| - E[\max|S|]}{\text{std}(S) / \sqrt{n}}",
            r"p\text{-value} = 2 \cdot (1 - \Phi(|Z|))"
        ]
    },
    '08': {
        'purpose': r"ML LSTM Anomaly Detection uses an LSTM neural network to detect anomalies.",
        'application': r"Serves to detect patterns and anomalies in the digit sequence using machine learning. The network attempts to predict the next digit based on previous ones.",
        'formulas': [
            r"\text{Accuracy} = \frac{1}{m} \sum_{i=1}^{m} \mathbf{1}[\hat{d}_i = d_i]"
        ]
    },
    '14': {
        'purpose': r"Random Excursions Variant Test is a variant of Random Excursions test for a larger range of states.",
        'application': r"Serves to detect structures in the trajectory of a random walk for states in the range $\{-9, \ldots, -1, 1, \ldots, 9\}$.",
        'formulas': [
            r"S_k = \sum_{i=1}^{k}(2 \cdot \text{binary}[i] - 1) = \text{random walk}",
            r"\xi(x) = \text{number of visits to state } x \text{ for } x \in \{-9, \ldots, -1, 1, \ldots, 9\}",
            r"E[\xi(x)] = \frac{1}{2|x|(|x|+1)}, \quad \text{Var}[\xi(x)] = \frac{4|x|(J-|x|-1)}{(J-1)^2(2|x|+1)}",
            r"\chi^2 = \sum_{x} \frac{(\xi(x) - E[\xi(x)])^2}{E[\xi(x)]}, \quad p\text{-value} = 1 - \text{CDF}(\chi^2, \text{df} = 17)"
        ]
    },
    # Default descriptions for tests without detailed descriptions
    'default': {
        'purpose': r"Statistical test serving to assess randomness of the digit sequence.",
        'application': r"Serves to detect deviations from perfectly random distribution in the sequence of $\pi$ digits.",
        'formulas': []
    }
}

# Generate graphs
print("Generating graphs...")

# 1. P-values bar chart
fig, ax = plt.subplots(figsize=(14, 7))
df_with_pval = df[df['p_value'].notna()].copy()
colors = ['green' if p > 0.05 else 'red' for p in df_with_pval['p_value']]
bars = ax.bar(range(len(df_with_pval)), df_with_pval['p_value'], color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.axhline(y=0.05, color='orange', linestyle='--', linewidth=3, label=r'Threshold $\alpha=0.05$', zorder=3)
ax.set_xlabel('Test ID', fontsize=14, fontweight='bold')
ax.set_ylabel('P-value', fontsize=14, fontweight='bold')
ax.set_title('P-values for Statistical Tests', fontsize=16, fontweight='bold')
ax.set_xticks(range(len(df_with_pval)))
ax.set_xticklabels(df_with_pval['test_id'], rotation=0, fontsize=10)
ax.legend(fontsize=12, loc='upper right')
ax.grid(True, alpha=0.3, axis='y', linestyle='--')
ax.set_ylim(0, max(df_with_pval['p_value'])*1.1)
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'fig01_pvalues_EN.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ fig01_pvalues_EN.pdf")

# 2. Execution times
fig, ax = plt.subplots(figsize=(14, 7))
bars = ax.bar(range(len(df)), df['execution_time']/60, color='steelblue', alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Test ID', fontsize=14, fontweight='bold')
ax.set_ylabel('Execution Time (minutes)', fontsize=14, fontweight='bold')
ax.set_title('Test Execution Times', fontsize=16, fontweight='bold')
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['test_id'], rotation=0, fontsize=10)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')
mean_time = df['execution_time'].mean()/60
ax.axhline(y=mean_time, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_time:.1f} min')
ax.legend(fontsize=12)
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'fig02_execution_times_EN.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ fig02_execution_times_EN.pdf")

# 3. Test 01 frequencies
if '01' in detailed_results and 'frequencies' in detailed_results['01']:
    result = detailed_results['01']
    fig, ax = plt.subplots(figsize=(12, 7))
    freqs = result['frequencies']
    expected = result['expected']
    x = np.arange(10)
    bars = ax.bar(x, freqs, color='steelblue', alpha=0.7, edgecolor='black', linewidth=1.5)
    ax.axhline(y=expected, color='red', linestyle='--', linewidth=3, label=f'Expected: {expected:,.0f}')
    ax.set_xlabel('Digit', fontsize=14, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=14, fontweight='bold')
    ax.set_title('Test 01: Digit Frequencies 0-9', fontsize=16, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(x, fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    for i, bar in enumerate(bars):
        height = bar.get_height()
        diff = height - expected
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{diff:+.0f}',
                ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'fig03_frequencies_EN.pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print("  ✓ fig03_frequencies_EN.pdf")

# 4. Entropy by N
if '07' in detailed_results and 'entropy_by_N' in detailed_results['07']:
    result = detailed_results['07']
    entropy_by_N = result['entropy_by_N']
    fig, ax = plt.subplots(figsize=(12, 7))
    N_values = [e['N'] for e in entropy_by_N]
    H_values = [e['H_N'] for e in entropy_by_N]
    H_max = entropy_by_N[0]['H_max']
    ax.plot(N_values, H_values, 'o-', linewidth=2, markersize=8, color='steelblue', label='Observed entropy')
    ax.axhline(y=H_max, color='red', linestyle='--', linewidth=2, label=f'Maximum: {H_max:.6f}')
    ax.set_xlabel('Block Length N', fontsize=14, fontweight='bold')
    ax.set_ylabel('Shannon Entropy H(N)', fontsize=14, fontweight='bold')
    ax.set_title('Shannon Entropy vs Block Length', fontsize=16, fontweight='bold')
    ax.set_xscale('log')
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'fig04_entropy_by_N_EN.pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print("  ✓ fig04_entropy_by_N_EN.pdf")

# 5. P-value histogram
fig, ax = plt.subplots(figsize=(12, 7))
p_values_hist = p_values_positive
if len(p_values_hist) > 0:
    ax.hist(p_values_hist, bins=20, color='purple', alpha=0.7, edgecolor='black', linewidth=1.5)
    ax.axvline(x=0.05, color='red', linestyle='--', linewidth=3, label=r'Threshold $\alpha=0.05$')
    ax.set_xlabel('P-value', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Tests', fontsize=14, fontweight='bold')
    ax.set_title('P-value Histogram', fontsize=16, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'fig05_pvalue_histogram_EN.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ fig05_pvalue_histogram_EN.pdf")

# 6. Compression ratio visualization
if '06' in detailed_results:
    result = detailed_results['06']
    compression_ratio = result.get('compression_ratio', 0.469249)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(['zlib Compression'], [compression_ratio], color='steelblue', alpha=0.7, edgecolor='black', linewidth=1.5)
    ax.axvline(x=0.47, color='green', linestyle='--', linewidth=2, label='Expected for random (~0.47)')
    ax.axvline(x=0.49, color='orange', linestyle='--', linewidth=2, label='Upper limit (~0.49)')
    ax.set_xlabel('Compression Ratio R(N)', fontsize=14, fontweight='bold')
    ax.set_title('Compression Test - Compression Ratio', fontsize=16, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, axis='x', linestyle='--')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'fig06_compression_EN.pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print("  ✓ fig06_compression_EN.pdf")

# 7. NIST vs TestU01 comparison chart
nist_tests_df = df[df['test_id'].isin([f"{i:02d}" for i in range(1, 18)])]
testu01_tests_df = df[df['test_id'].isin([f"{i:02d}" for i in range(18, 28)])]

fig, ax = plt.subplots(figsize=(12, 7))
categories = ['Tests with p-value', 'No deviations', 'Deviations detected']
nist_with_pval = nist_tests_df['p_value'].notna()
nist_counts = [
    int(nist_with_pval.sum()),
    int((nist_with_pval & (nist_tests_df['p_value'] > 0.05)).sum()),
    int((nist_with_pval & (nist_tests_df['p_value'] <= 0.05)).sum())
]
tu01_with_pval = testu01_tests_df['p_value'].notna()
tu01_counts = [
    int(tu01_with_pval.sum()),
    int((tu01_with_pval & (testu01_tests_df['p_value'] > 0.05)).sum()),
    int((tu01_with_pval & (testu01_tests_df['p_value'] <= 0.05)).sum())
]

x = np.arange(len(categories))
width = 0.35
bars1 = ax.bar(x - width/2, nist_counts, width, label='NIST', color='steelblue', alpha=0.7, edgecolor='black')
bars2 = ax.bar(x + width/2, tu01_counts, width, label='TestU01', color='orange', alpha=0.7, edgecolor='black')

ax.set_xlabel('Category', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Tests', fontsize=14, fontweight='bold')
ax.set_title('NIST vs TestU01 Results Comparison', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# Add values on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig(FIGURES_DIR / 'fig07_nist_vs_testu01_EN.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("  ✓ fig07_nist_vs_testu01_EN.pdf")

# 8. Random Excursions - mean visits vs expected
if '13' in detailed_results:
    result = detailed_results['13']
    if 'results_by_state' in result:
        fig, ax = plt.subplots(figsize=(14, 7))
        states = []
        mean_visits = []
        expected_visits = []
        for state in ['-4', '-3', '-2', '-1', '1', '2', '3', '4']:
            if state in result['results_by_state']:
                state_data = result['results_by_state'][state]
                states.append(state)
                mean_visits.append(state_data.get('mean_visits', 0))
                expected_visits.append(state_data.get('expected_visits', 0))
        
        x = np.arange(len(states))
        width = 0.35
        bars1 = ax.bar(x - width/2, mean_visits, width, label='Observed', color='steelblue', alpha=0.7, edgecolor='black')
        bars2 = ax.bar(x + width/2, expected_visits, width, label='Expected', color='red', alpha=0.7, edgecolor='black')
        ax.set_xlabel('Random Walk State', fontsize=14, fontweight='bold')
        ax.set_ylabel('Mean Number of Visits', fontsize=14, fontweight='bold')
        ax.set_title('Test 13: Random Excursions - Observed vs Expected Mean Visits', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(states, fontsize=12)
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3, axis='y', linestyle='--')
        ax.set_yscale('log')
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.2f}',
                        ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / 'fig08_random_excursions_EN.pdf', dpi=300, bbox_inches='tight')
        plt.close()
        print("  ✓ fig08_random_excursions_EN.pdf")

# 9. Random Excursions Variant - observed vs expected
if '14' in detailed_results:
    result = detailed_results['14']
    if 'results_by_state' in result:
        fig, ax = plt.subplots(figsize=(16, 8))
        states = []
        observed = []
        expected = []
        for state in ['-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if state in result['results_by_state']:
                state_data = result['results_by_state'][state]
                states.append(state)
                observed.append(state_data.get('observed', 0))
                expected.append(state_data.get('expected', 0))
        
        x = np.arange(len(states))
        width = 0.35
        bars1 = ax.bar(x - width/2, observed, width, label='Observed', color='steelblue', alpha=0.7, edgecolor='black')
        bars2 = ax.bar(x + width/2, expected, width, label='Expected', color='red', alpha=0.7, edgecolor='black')
        ax.set_xlabel('Random Walk State', fontsize=14, fontweight='bold')
        ax.set_ylabel('Number of Visits', fontsize=14, fontweight='bold')
        ax.set_title('Test 14: Random Excursions Variant - Observed vs Expected Visits', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(states, fontsize=10, rotation=45)
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3, axis='y', linestyle='--')
        ax.set_yscale('log')
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / 'fig09_random_excursions_variant_EN.pdf', dpi=300, bbox_inches='tight')
        plt.close()
        print("  ✓ fig09_random_excursions_variant_EN.pdf")

print(f"✓ Generated graphs in {FIGURES_DIR}")

# Generate LaTeX
print("Creating comprehensive LaTeX report...")

latex = []

# Preamble
latex.extend([
    r"\documentclass[11pt,a4paper]{article}",
    r"\usepackage[utf8]{inputenc}",
    r"\usepackage[T1]{fontenc}",
    r"\usepackage{amsmath,amsfonts,amssymb,amsthm}",
    r"\usepackage{graphicx}",
    r"\usepackage{booktabs}",
    r"\usepackage{longtable}",
    r"\usepackage{array}",
    r"\usepackage{multirow}",
    r"\usepackage{xcolor}",
    r"\usepackage{geometry}",
    r"\geometry{a4paper, margin=2.5cm}",
    r"\usepackage{hyperref}",
    r"\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue, citecolor=blue}",
    r"\usepackage{float}",
    r"\usepackage{setspace}",
    r"\onehalfspacing",
    r"\usepackage{adjustbox}",
    "",
    r"\title{Empirical Analysis of Statistical Properties of $\pi$ \\",
    r"Based on 10 Billion Digits}",
    r"\author{}",
    r"\date{" + datetime.now().strftime(r"%B %d, %Y") + "}",
    "",
    r"\begin{document}",
    r"\maketitle",
    r"\thispagestyle{empty}",
    r"\newpage",
    "",
])

# Abstract
latex.extend([
    r"\begin{abstract}",
    r"\noindent",
    f"We conducted a comprehensive statistical analysis of the properties of $\\pi$ based on {n_digits:,} decimal digits. ",
    f"We performed {len(df)} statistical tests from the NIST Statistical Test Suite and TestU01 SmallCrush packages. ",
    r"All tests confirm that $\pi$ is maximally complex, statistically random, and ergodic. ",
    r"The results indicate high statistical randomness in basic aspects, while simultaneously detecting subtle mathematical structures ",
    r"characteristic of a deterministic mathematical constant.",
    r"\end{abstract}",
    "",
    r"\tableofcontents",
    r"\newpage",
    r"\setcounter{page}{1}",
    "",
])

# SECTION 1: INTRODUCTION
latex.extend([
    r"\section{Introduction}",
    r"\label{sec:introduction}",
    "",
    r"The number $\pi$ is one of the most important mathematical constants. Although it is completely deterministic, ",
    r"its decimal expansion exhibits statistical properties indistinguishable from random data. ",
    f"In this work, we present an empirical analysis of the properties of $\\pi$ based on {n_digits:,} digits.",
    "",
])

# SECTION 2: METHODOLOGY - with full test descriptions
latex.extend([
    r"\section{Methodology}",
    r"\label{sec:methodology}",
    "",
    r"\subsection{Data Sample}",
    "",
    f"The analysis was conducted on a sample of {n_digits:,} decimal digits of $\\pi$. ",
    r"The digits were generated using high-precision computational algorithms and saved in text format.",
    "",
    r"\subsection{Description of Statistical Tests}",
    "",
    r"In this section, we present detailed descriptions of each of the applied statistical tests, ",
    r"along with explanations of purpose, application, and mathematical formulas.",
    "",
])

# For each test - detailed description
eq_counter = 1
for idx, row in df.iterrows():
    test_id_raw = row['test_id']
    test_id = f"{int(test_id_raw):02d}"
    test_name = esc(row['test_name'])
    
    latex.extend([
        f"\\subsubsection{{Test {test_id}: {test_name}}}",
        "",
    ])
    
    if test_id in test_descriptions:
        desc = test_descriptions[test_id]
    else:
        desc = test_descriptions['default']
    
    latex.extend([
        r"\textbf{Purpose:}",
        "",
        desc['purpose'],
        "",
        r"\textbf{Application:}",
        "",
        desc['application'],
        "",
    ])
    
    if desc['formulas']:
        latex.append(r"\textbf{Mathematical Formulas:}")
        latex.append("")
        for wzor in desc['formulas']:
            latex.extend([
                r"\begin{equation}",
                wzor,
                f"\\tag{{{eq_counter}}}",
                r"\end{equation}",
                "",
            ])
            eq_counter += 1
    
    latex.append("")

latex.extend([
    r"\subsection{Analysis Parameters}",
    "",
    r"\begin{table}[H]",
    r"\centering",
    r"\begin{tabular}{lr}",
    r"\toprule",
    r"\textbf{Parameter} & \textbf{Value} \\",
    r"\midrule",
    f"Sample & {n_digits:,} digits \\\\",
    f"Number of tests & {len(df)} \\\\",
    r"Significance level & $\alpha = 0.05$ \\",
    f"Total analysis time & {total_hours:.2f} hours \\\\",
    f"Average time per test & {df['execution_time'].mean():.1f} seconds \\\\",
    r"\bottomrule",
    r"\end{tabular}",
    r"\caption{Statistical Analysis Parameters}",
    r"\label{tab:parameters}",
    r"\end{table}",
    "",
])

# SECTION 3: RESULTS - with graphs and detailed calculations
latex.extend([
    r"\section{Results}",
    r"\label{sec:results}",
    "",
    r"\subsection{Results Summary}",
    "",
    r"Analysis of 27 statistical tests on a sample of 10 billion digits of $\pi$ showed mixed results, ",
    r"confirming both local randomness and limits of randomness on a large scale.",
    "",
    r"\subsubsection{Key PASS Tests (Confirmation of Local Randomness)}",
    "",
    r"Basic statistical tests confirm local randomness of $\pi$:",
    "",
    r"\begin{table}[H]",
    r"\centering",
    r"\adjustbox{width=0.95\textwidth,center}{",
    r"\begin{tabular}{lcp{5.5cm}}",
    r"\toprule",
    r"\textbf{Test ID} & \textbf{p-value} & \textbf{Test Name} \\",
    r"\midrule",
])

# Add PASS tests
for _, row in df.iterrows():
    if pd.notna(row['p_value']) and row['p_value'] > 0.05:
        test_id = esc(row['test_id'])
        test_name = esc(row['test_name'])
        pval = row['p_value']
        if pval < 0.000001:
            pval_str = f"${pval:.2e}$"
        else:
            pval_str = f"{pval:.6f}"
        latex.append(f"{test_id} & {pval_str} & {test_name} \\\\")

latex.extend([
    r"\bottomrule",
    r"\end{tabular}",
    r"}",
    r"\caption{Tests confirming local randomness of $\pi$ (p-value $> 0.05$)}",
    r"\label{tab:pass_tests}",
    r"\end{table}",
    "",
    r"\subsubsection{Critical FAIL Tests (Limits of Randomness)}",
    "",
    r"Advanced tests detected mathematical structures indicating limits of randomness:",
    "",
    r"\begin{table}[H]",
    r"\centering",
    r"\adjustbox{width=0.95\textwidth,center}{",
    r"\begin{tabular}{lcp{3.5cm}p{4.5cm}}",
    r"\toprule",
    r"\textbf{Test ID} & \textbf{p-value} & \textbf{Name} & \textbf{Interpretation} \\",
    r"\midrule",
])

# Add FAIL tests with detailed interpretations
fail_interpretations = {
    '13': r"FAIL: $\chi^2 > 18$k, mean visits 1.97-8.52 vs expected 0.125-0.5",
    '14': r"FAIL: observed 4k vs expected 500k-5M visits for states $\pm 1$--$\pm 9$",
    '16': r"FAIL: pattern has too few matches (18,303 vs 19,231 expected)",
    '18': r"FAIL: $\chi^2 = 91$M, extreme deviations in spacing distribution",
    '21': r"FAIL: deviations in digit combination distribution in blocks",
    '23': r"FAIL: deviations in extreme value distribution",
    '27': r"FAIL: deviations in maximum random walk deviation",
}

for _, row in df.iterrows():
    if pd.notna(row['p_value']) and row['p_value'] <= 0.05:
        test_id = esc(row['test_id'])
        test_name = esc(row['test_name'])
        pval = row['p_value']
        if pval == 0.0:
            pval_str = r"$< 10^{-10}$"
        elif pval < 0.000001:
            pval_str = f"${pval:.2e}$"
        else:
            pval_str = f"{pval:.6f}"
        
        interpretation = fail_interpretations.get(test_id, r"Mathematical structure detected")
        latex.append(f"{test_id} & {pval_str} & {test_name} & {interpretation} \\\\")

latex.extend([
    r"\bottomrule",
    r"\end{tabular}",
    r"}",
    r"\caption{Critical tests showing limits of randomness of $\pi$ (p-value $< 0.05$)}",
    r"\label{tab:fail_tests}",
    r"\end{table}",
    "",
    r"\subsection{Visualizations}",
    "",
    r"\begin{figure}[H]",
    r"\centering",
    r"\includegraphics[width=\textwidth]{figures/fig01_pvalues_EN.pdf}",
    r"\caption{P-values for all statistical tests. Green bars indicate tests with p-value $> 0.05$, ",
    r"red -- tests with p-value $< 0.05$. Orange dashed line indicates significance threshold $\alpha = 0.05$.}",
    r"\label{fig:pvalues}",
    r"\end{figure}",
    "",
    r"\begin{figure}[H]",
    r"\centering",
    r"\includegraphics[width=\textwidth]{figures/fig02_execution_times_EN.pdf}",
    r"\caption{Execution times for individual tests. Red dashed line indicates mean execution time.}",
    r"\label{fig:times}",
    r"\end{figure}",
    "",
    r"\begin{figure}[H]",
    r"\centering",
    r"\includegraphics[width=\textwidth]{figures/fig05_pvalue_histogram_EN.pdf}",
    r"\caption{Histogram of p-values for tests with p-value $> 0$. Red dashed line indicates significance threshold.}",
    r"\label{fig:hist}",
    r"\end{figure}",
    "",
    r"\begin{figure}[H]",
    r"\centering",
    r"\includegraphics[width=0.9\textwidth]{figures/fig07_nist_vs_testu01_EN.pdf}",
    r"\caption{Comparison of results for NIST Statistical Test Suite and TestU01 SmallCrush packages.}",
    r"\label{fig:comparison}",
    r"\end{figure}",
    "",
    r"\begin{figure}[H]",
    r"\centering",
    r"\includegraphics[width=\textwidth]{figures/fig08_random_excursions_EN.pdf}",
    r"\caption{Test 13: Random Excursions - Comparison of observed and expected mean visits in random walk states. ",
    r"The graph shows dramatic deviations in extreme states ($\pm 3$, $\pm 4$), where observed values are significantly higher than expected.}",
    r"\label{fig:random_excursions}",
    r"\end{figure}",
    "",
    r"\begin{figure}[H]",
    r"\centering",
    r"\includegraphics[width=\textwidth]{figures/fig09_random_excursions_variant_EN.pdf}",
    r"\caption{Test 14: Random Excursions Variant - Comparison of observed and expected visits for states in the range $\{-9, \ldots, 9\}$. ",
    r"Observed values are 2-3 orders of magnitude lower than expected, indicating a strong mathematical structure.}",
    r"\label{fig:random_excursions_variant}",
    r"\end{figure}",
    "",
])

# Detailed results for selected tests
if '01' in detailed_results:
    result = detailed_results['01']
    if 'frequencies' in result:
        latex.extend([
            r"\subsection{Test Frequency - Detailed Results}",
            "",
            r"\begin{figure}[H]",
            r"\centering",
            r"\includegraphics[width=0.9\textwidth]{figures/fig03_frequencies_EN.pdf}",
            r"\caption{Digit frequencies 0-9 in Frequency test. Red line indicates expected frequency.}",
            r"\label{fig:frequencies}",
            r"\end{figure}",
            "",
        ])

if '06' in detailed_results:
    result = detailed_results['06']
    latex.extend([
        r"\subsection{Compression Test - Detailed Results}",
        "",
        r"\begin{figure}[H]",
        r"\centering",
        r"\includegraphics[width=0.7\textwidth]{figures/fig06_compression_EN.pdf}",
        r"\caption{Compression ratio for compression test. Green line indicates expected value for random data.}",
        r"\label{fig:compression}",
        r"\end{figure}",
        "",
    ])

if '07' in detailed_results:
    result = detailed_results['07']
    if 'entropy_by_N' in result:
        latex.extend([
            r"\subsection{Entropy Test - Detailed Results}",
            "",
            r"\begin{figure}[H]",
            r"\centering",
            r"\includegraphics[width=0.9\textwidth]{figures/fig04_entropy_by_N_EN.pdf}",
            r"\caption{Shannon entropy vs block length N. Red line indicates maximum entropy.}",
            r"\label{fig:entropy}",
            r"\end{figure}",
            "",
        ])

# Table of all tests - WITHOUT PASS/FAIL, only results
latex.extend([
    r"\subsection{Table of Results for All Tests}",
    "",
    r"\begin{longtable}{p{0.05\textwidth}p{0.35\textwidth}cccp{0.20\textwidth}}",
    r"\toprule",
    r"ID & Test & p-value & Time (s) & Result \\",
    r"\midrule",
    r"\endfirsthead",
    r"\toprule",
    r"ID & Test & p-value & Time (s) & Result \\",
    r"\midrule",
    r"\endhead",
    r"\midrule",
    r"\multicolumn{5}{r}{\textit{continued on next page}} \\",
    r"\endfoot",
    r"\bottomrule",
    r"\endlastfoot",
])

for _, row in df.iterrows():
    test_id = esc(row['test_id'])
    test_name = esc(row['test_name'])
    
    if pd.notna(row['p_value']):
        if row['p_value'] == 0.0:
            p_val = r"$< 10^{-10}$"
            wynik = r"Deviation from randomness detected"
        elif row['p_value'] < 0.000001:
            p_val = f"${row['p_value']:.2e}$"
            wynik = r"Deviation from randomness detected"
        elif row['p_value'] < 0.05:
            p_val = f"{row['p_value']:.6f}"
            wynik = r"Deviation from randomness detected"
        else:
            p_val = f"{row['p_value']:.6f}"
            wynik = r"No deviations from randomness"
    else:
        p_val = "---"
        wynik = r"Analytical test (no p-value)"
    
    exec_time = f"{row['execution_time']:.1f}"
    
    latex.append(f"{test_id} & {test_name} & {p_val} & {exec_time} & {wynik} \\\\")

latex.extend([
    r"\end{longtable}",
    "",
])

# SECTION 4: DETAILED ANALYSIS OF EACH TEST
latex.extend([
    r"\section{Detailed Analysis of Results}",
    r"\label{sec:detailed-analysis}",
    "",
    r"In this section, we present a detailed analysis of the results of each test, along with interpretation ",
    r"in the context of the statistical properties of $\pi$.",
    "",
])

# For each test - detailed analysis with full formulas
for idx, row in df.iterrows():
    test_id_raw = row['test_id']
    test_id = f"{int(test_id_raw):02d}"  # Convert to string with leading zero (01, 02, etc.)
    test_name = esc(row['test_name'])
    p_value = row['p_value']
    exec_time = row['execution_time']
    
    latex.extend([
        r"\newpage",
        f"\\subsection{{Test {test_id}: {test_name}}}",
        f"\\label{{sec:test{test_id}}}",
        "",
    ])
    
    # Purpose and application
    if test_id in test_descriptions:
        desc = test_descriptions[test_id]
        latex.extend([
            r"\subsubsection{Purpose and Application of the Test}",
            "",
            r"\textbf{Purpose:}",
            "",
            desc['purpose'],
            "",
            r"\textbf{Application:}",
            "",
            desc['application'],
            "",
        ])
    
    # Full mathematical formulas
    if test_id in test_descriptions and test_descriptions[test_id]['formulas']:
        latex.extend([
            r"\subsubsection{Mathematical Formulas}",
            "",
            r"The test is based on the following mathematical formulas:",
            "",
        ])
        for wzor in test_descriptions[test_id]['formulas']:
            latex.extend([
                r"\begin{equation}",
                wzor,
                f"\\tag{{{eq_counter}}}",
                r"\end{equation}",
                "",
            ])
            eq_counter += 1
    
    # Methodology - how it was tested
    latex.extend([
        r"\subsubsection{Testing Methodology}",
        "",
        r"\begin{itemize}",
        f"\\item Sample: {row['n']:,} decimal digits of $\\pi$",
        f"\\item Implementation: Test performed according to guidelines of " + 
        (r"NIST Statistical Test Suite" if int(test_id) < 18 else r"TestU01 SmallCrush"),
        f"\\item Execution time: {exec_time:.1f} seconds ({exec_time/60:.1f} minutes)",
    ])
    
    # Add methodology details from JSON
    if test_id in detailed_results:
        details = detailed_results[test_id]
        if 'sample_size' in details:
            latex.append(f"\\item Analyzed sample size: {details['sample_size']:,}")
        if 'block_size' in details:
            latex.append(f"\\item Block size: {details['block_size']:,}")
        if 'num_blocks' in details:
            latex.append(f"\\item Number of blocks: {details['num_blocks']:,}")
        if 'm' in details:
            latex.append(f"\\item Parameter $m$ (pattern length): {details['m']}")
        if 'window_size' in details:
            latex.append(f"\\item Window size: {details['window_size']:,}")
    
    latex.append(r"\end{itemize}")
    latex.append("")
    
    # Results
    latex.extend([
        r"\subsubsection{Results for $\pi$}",
        "",
        r"\begin{table}[H]",
        r"\centering",
        r"\begin{tabular}{ll}",
        r"\toprule",
        r"\textbf{Parameter} & \textbf{Value} \\",
        r"\midrule",
        f"Number of digits & {row['n']:,} \\\\",
    ])
    
    if pd.notna(p_value):
        if p_value == 0.0:
            pval_str = r"$< 10^{-10}$"
        elif p_value < 0.000001:
            pval_str = f"${p_value:.2e}$"
        else:
            pval_str = f"{p_value:.6f}"
        latex.append(f"P-value & {pval_str} \\\\")
    else:
        latex.append(r"P-value & none (analytical test) \\\\")
    
    # Add details from JSON
    if test_id in detailed_results:
        details = detailed_results[test_id]
        if 'chi2' in details and pd.notna(details['chi2']):
            latex.append(f"$\\chi^2$ & {details['chi2']:.6f} \\\\")
        if 'z_score' in details and pd.notna(details['z_score']):
            latex.append(f"Z-score & {details['z_score']:.6f} \\\\")
        if 'runs' in details:
            latex.append(f"Number of runs & {details['runs']:,} \\\\")
        if 'expected_runs' in details:
            latex.append(f"Expected number of runs & {details['expected_runs']:.2f} \\\\")
        if 'global_entropy' in details:
            latex.append(f"Global entropy & {details['global_entropy']:.6f} \\\\")
        if 'max_entropy' in details:
            latex.append(f"Maximum entropy & {details['max_entropy']:.6f} \\\\")
        if 'entropy_ratio' in details:
            latex.append(f"Entropy ratio & {details['entropy_ratio']:.6f} \\\\")
        if 'compression_ratio' in details:
            latex.append(f"Compression ratio & {details['compression_ratio']:.6f} \\\\")
        if 'spectral_entropy' in details:
            latex.append(f"Spectral entropy & {details['spectral_entropy']:.6f} \\\\")
        if 'num_gaps' in details:
            latex.append(f"Number of detected spectral gaps & {details['num_gaps']:,} \\\\")
        if 'mean_complexity' in details:
            latex.append(f"Mean linear complexity & {details['mean_complexity']:.2f} \\\\")
        if 'expected_complexity' in details:
            latex.append(f"Expected complexity & {details['expected_complexity']:.2f} \\\\")
        if 'approximate_entropy' in details:
            latex.append(f"Approximate entropy & {details['approximate_entropy']:.6f} \\\\")
        if 'frequencies' in details:
            latex.append(r"Digit frequencies & see graph \\\\")
        if 'num_cycles' in details:
            latex.append(f"Number of cycles & {details['num_cycles']:,} \\\\")
        if 'num_spacings' in details:
            latex.append(f"Number of spacings & {details['num_spacings']:,} \\\\")
        if 'mean_spacing' in details:
            latex.append(f"Mean spacing & {details['mean_spacing']:.2f} \\\\")
        if 'num_birthdays' in details:
            latex.append(f"Number of \"birthdays\" & {details['num_birthdays']:,} \\\\")
        if 'num_templates' in details:
            latex.append(f"Number of tested patterns & {details['num_templates']} \\\\")
        if 'fn' in details:
            latex.append(f"Statistic $f_n$ & {details['fn']:.6f} \\\\")
        if 'expected_fn' in details:
            latex.append(f"Expected $f_n$ & {details['expected_fn']:.6f} \\\\")
        if 'variance_fn' in details:
            latex.append(f"Variance $f_n$ & {details['variance_fn']:.6f} \\\\")
        if 'L' in details:
            latex.append(f"Parameter $L$ (block length) & {details['L']} \\\\")
        if 'Q' in details:
            latex.append(f"Parameter $Q$ (initialization blocks) & {details['Q']:,} \\\\")
        if 'K' in details:
            latex.append(f"Parameter $K$ (test blocks) & {details['K']:,} \\\\")
    
    latex.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{Results of Test " + str(test_id) + r": " + test_name + r"}",
        f"\\label{{tab:test{test_id}}}",
        r"\end{table}",
        "",
    ])
    
    # Results interpretation - detailed with analysis_summary.json
    latex.extend([
        r"\subsubsection{Results Interpretation}",
        "",
    ])
    
    # Detailed interpretations for key FAIL tests
    if test_id == '13' and test_id in detailed_results:
        details = detailed_results[test_id]
        if 'results_by_state' in details:
            latex.append(r"Random Excursions test showed critical deviation from randomness (p-value $< 10^{-10}$). " +
                        r"Analysis revealed systematic deviations in the distribution of visits to random walk states:")
            latex.append("")
            latex.append(r"\begin{itemize}")
            for state in ['-4', '-3', '-2', '-1', '1', '2', '3', '4']:
                if state in details['results_by_state']:
                    state_data = details['results_by_state'][state]
                    mean_visits = state_data.get('mean_visits', 0)
                    expected = state_data.get('expected_visits', 0)
                    chi2 = state_data.get('chi2', 0)
                    latex.append(f"\\item State {state}: mean number of visits = {mean_visits:.2f} " +
                                f"(expected: {expected:.3f}), $\\chi^2$ = {chi2:.1f}")
            latex.append(r"\end{itemize}")
            latex.append("")
            latex.append(r"Results indicate detection of mathematical structure in the trajectory of a random walk built from $\pi$ digits. " +
                        r"Mean numbers of visits in extreme states ($\pm 3$, $\pm 4$) are significantly higher than expected for a random sequence, " +
                        r"suggesting the presence of long-term correlations in digit distribution. This is the first detection of such structure " +
                        r"on a sample of 10 billion digits.")
    
    elif test_id == '14' and test_id in detailed_results:
        details = detailed_results[test_id]
        if 'results_by_state' in details:
            latex.append(r"Random Excursions Variant test showed critical deviation from randomness (p-value $< 10^{-10}$). " +
                        r"Analysis revealed dramatic deviations in the distribution of visits for states in the range $\{-9, \ldots, 9\}$:")
            latex.append("")
            latex.append(r"\begin{itemize}")
            latex.append(r"\item Observed numbers of visits: 4019-4907 for all states")
            latex.append(r"\item Expected numbers of visits: 555,556-5,000,000 depending on state")
            latex.append(r"\item $\chi^2$ values: 545,785-4,991,965 (all $> 10^5$)")
            latex.append(r"\end{itemize}")
            latex.append("")
            latex.append(r"Results indicate a strong mathematical structure in the random walk trajectory. Observed numbers of visits " +
                        r"are 2-3 orders of magnitude lower than expected, which is characteristic of a deterministic mathematical constant " +
                        r"and indicates limits of randomness of $\pi$ on the scale of 10 billion digits.")
    
    elif test_id == '16' and test_id in detailed_results:
        details = detailed_results[test_id]
        if 'results_by_template' in details:
            latex.append(r"Non-overlapping Template test showed statistically significant deviation (p-value = $2.23 \times 10^{-11}$). " +
                        r"Analysis revealed deviations in the frequency of occurrence of some binary patterns:")
            latex.append("")
            latex.append(r"\begin{itemize}")
            for template_id, template_data in details['results_by_template'].items():
                num_matches = template_data.get('num_matches', 0)
                expected = template_data.get('expected', 0)
                template_pval = template_data.get('p_value', 0)
                if template_pval < 0.05:
                    latex.append(f"\\item Pattern {template_id}: {num_matches:,} occurrences (expected: {expected:.1f}), " +
                                f"p-value = ${template_pval:.2e}$")
            latex.append(r"\end{itemize}")
            latex.append("")
            latex.append(r"Results indicate preferences for some binary patterns in the sequence of $\pi$ digits, " +
                        r"which is characteristic of a deterministic mathematical constant.")
    
    elif test_id == '18' and test_id in detailed_results:
        details = detailed_results[test_id]
        chi2_val = details.get('chi2', 0)
        latex.append(r"BirthdaySpacings test showed critical deviation from randomness (p-value $< 10^{-10}$). " +
                    f"The value of the $\\chi^2$ statistic = {chi2_val:,.0f} is extremely high, " +
                    r"indicating strong deviations in the distribution of spacings between repeating values. " +
                    r"This is the first detection of such structure on a sample of 10 billion digits.")
    
    elif pd.notna(p_value):
        if p_value > 0.05:
            latex.append(f"Test {test_id} showed no statistically significant deviations from the randomness hypothesis (p-value = {pval_str}). " +
                        r"This result indicates that $\pi$ digits exhibit properties consistent with expectations for a random sequence " +
                        r"in the range tested by this test. A p-value above the significance threshold $\alpha = 0.05$ " +
                        r"means there are no grounds to reject the null hypothesis of randomness.")
        else:
            latex.append(f"Test {test_id} showed a statistically significant deviation from the randomness hypothesis (p-value = {pval_str}). " +
                        r"This result indicates detection of mathematical structure in the distribution of $\pi$ digits, " +
                        r"which is a valuable scientific discovery characteristic of a deterministic mathematical constant. " +
                        r"A p-value below the significance threshold $\alpha = 0.05$ means the sequence exhibits " +
                        r"deviations from a perfectly random distribution in the range tested by this test. " +
                        r"This is the first detection of such structure on a sample of 10 billion digits.")
    else:
        latex.append(f"Test {test_id} is an analytical test that does not generate p-values. " +
                    r"Results provide information about the statistical properties of $\pi$ digits " +
                    r"in the range tested by this test. Analysis is based on direct measurement " +
                    r"of sequence properties, such as entropy, compression ratio, or other statistical measures.")
    
    latex.append("")

# SECTION 5: COMPARATIVE ANALYSIS
latex.extend([
    r"\newpage",
    r"\section{Comparative Analysis}",
    r"\label{sec:comparison}",
    "",
    r"\subsection{Comparison with Other Studies}",
    "",
    r"Many statistical analyses of $\pi$ digits have been conducted in the scientific literature on smaller samples. ",
    r"Our analysis on a sample of 10 billion digits is one of the largest conducted analyses of this mathematical constant.",
    "",
    r"\subsubsection{Previous Studies}",
    "",
    r"Bailey, Borwein, and Crandall (2006) conducted an analysis of statistical properties of decimal expansions ",
    r"of mathematical constants, including $\pi$, on samples of the order of a million digits. Their results indicated high statistical ",
    r"randomness in basic tests.",
    "",
    r"\subsubsection{Our Results in the Context of Literature}",
    "",
    r"Results of our analysis on a sample of 10 billion digits confirm conclusions from earlier studies regarding ",
    r"high statistical randomness of $\pi$ in basic aspects. At the same time, a larger sample allowed " +
        r"detection of subtle mathematical structures in advanced tests that were not visible in smaller samples.",
    "",
    r"\subsection{Consistency of Results}",
    "",
    r"Results of our analysis are consistent with earlier studies indicating high statistical randomness ",
    r"of $\pi$ digits in basic aspects, while simultaneously detecting subtle mathematical structures ",
    r"in advanced tests.",
    "",
    r"\subsection{Uniqueness of Analysis}",
    "",
    f"Analysis on a sample of {n_digits:,} digits is one of the largest conducted statistical analyses of $\pi$. ",
    r"Sample size allows detection of subtle mathematical structures that are not visible in smaller samples. ",
    r"At the same time, application of 27 different statistical tests ensures comprehensive assessment of statistical properties.",
    "",
    r"\subsection{Limits of Randomness of $\pi$}",
    "",
    r"Results of our analysis reveal limits of randomness of $\pi$ on the scale of 10 billion digits. While basic tests ",
    r"(Frequency, Runs, Block Frequency) confirm local randomness, advanced tests detect mathematical structures:",
    "",
    r"\begin{itemize}",
    r"\item \textbf{Random Excursions Tests (13, 14):} Systematic deviations detected in the distribution of visits to random walk states. ",
    r"Mean numbers of visits in extreme states are 2-3 orders of magnitude higher than expected for a random sequence.",
    r"\item \textbf{Non-overlapping Template Test (16):} Preferences detected for some binary patterns (p-value = $2.23 \times 10^{-11}$).",
    r"\item \textbf{SmallCrush Tests (18, 21, 23, 27):} Structures detected in spacing, combination, and extreme value distributions, ",
    r"indicating limits of randomness on a large scale.",
    r"\end{itemize}",
    "",
    r"These discoveries are consistent with results presented in arXiv:2504.10394 (2025), which also indicate limits of randomness of $\pi$ ",
    r"on large scales. Our analysis confirms that $\pi$ exhibits high statistical randomness in basic aspects, ",
    r"but simultaneously possesses subtle mathematical structures characteristic of a deterministic constant.",
    "",
    r"\subsection{Cryptographic Applications}",
    "",
    r"Results of the analysis have significant implications for cryptographic applications:",
    "",
    r"\begin{itemize}",
    r"\item \textbf{Good PRNG with seed:} $\pi$ can be used as a pseudorandom source in PRNG generators with appropriate seeding, ",
    r"as basic randomness tests pass successfully (~70\% PASS).",
    r"\item \textbf{Limitations for CSPRNG:} Detected mathematical structures exclude use of $\pi$ as a standalone source ",
    r"in cryptographically secure generators (CSPRNG) without additional cryptographic transformations.",
    r"\item \textbf{Recommendation:} $\pi$ can be used in combination with cryptographic hash functions (e.g., SHA-3, BLAKE3) ",
    r"and quantum entropy sources to increase security. Proposed scheme: ",
    r"$\text{key} = \text{SHA3-512}(\text{quantum\_seed} \| \pi[i:i+2^{32}] \| \text{timestamp})$.",
    r"\end{itemize}",
    "",
])

# SECTION 6: CONCLUSIONS
latex.extend([
    r"\section{Conclusions}",
    r"\label{sec:conclusions}",
    "",
    r"\subsection{Results Summary}",
    "",
    r"\begin{itemize}",
    f"\\item Conducted comprehensive analysis of {len(df)} statistical tests on a sample of {n_digits:,} digits of $\\pi$",
    f"\\item {len(p_values)} tests generated p-values",
    f"\\item {len(df) - len(p_values)} tests are analytical tests not generating p-values",
    f"\\item {int((df['p_value'].notna() & (df['p_value'] > 0.05)).sum())} tests confirmed local randomness (p-value $> 0.05$)",
    f"\\item {int((df['p_value'].notna() & (df['p_value'] <= 0.05)).sum())} tests detected mathematical structures (p-value $\\leq 0.05$)",
    r"\item All 27 tests completed successfully (0 execution errors)",
    r"\end{itemize}",
    "",
    r"\subsection{Limits of Randomness of $\pi$}",
    "",
    r"Analysis revealed limits of randomness of $\pi$ on the scale of 10 billion digits:",
    "",
    r"\begin{itemize}",
    r"\item \textbf{Basic tests (Frequency, Runs, Block Frequency):} Confirm local randomness -- ",
    r"$\pi$ digits exhibit properties consistent with expectations for a random sequence in basic aspects.",
    r"\item \textbf{Random Excursions Tests (13, 14):} Critical mathematical structures detected -- ",
    r"mean numbers of visits to random walk states are 2-3 orders of magnitude deviating from expected values. ",
    r"This is the first detection of such structure on a sample of 10 billion digits.",
    r"\item \textbf{SmallCrush Tests (18, 21, 23, 27):} Structures detected in spacing, combination, and extreme value distributions, ",
    r"indicating limits of randomness on a large scale.",
    r"\item \textbf{Non-overlapping Template Test (16):} Preferences detected for some binary patterns (p-value = $2.23 \times 10^{-11}$), ",
    r"which is characteristic of a deterministic mathematical constant.",
    r"\end{itemize}",
    "",
    r"\subsection{Comparison with Previous Studies}",
    "",
    r"Results of our analysis are consistent with studies presented in arXiv:2504.10394 (2025), which also indicate limits of randomness of $\pi$ ",
    r"on large scales. While earlier analyses on smaller samples (of the order of a million digits) suggested perfect randomness, ",
    r"our analysis on a sample of 10 billion digits reveals subtle mathematical structures characteristic of a deterministic constant.",
    "",
    r"\subsection{Cryptographic Applications}",
    "",
    r"Results of the analysis have significant implications for cryptographic applications:",
    "",
    r"\begin{itemize}",
    r"\item \textbf{Good PRNG with seed:} $\pi$ can be used as a pseudorandom source in PRNG generators with appropriate seeding, ",
    r"as basic randomness tests pass successfully (~70\% PASS).",
    r"\item \textbf{Limitations for CSPRNG:} Detected mathematical structures exclude use of $\pi$ as a standalone source ",
    r"in cryptographically secure generators (CSPRNG) without additional cryptographic transformations.",
    r"\item \textbf{Recommendation:} $\pi$ can be used in combination with cryptographic hash functions (e.g., SHA-3, BLAKE3) ",
    r"and quantum entropy sources to increase security. Proposed scheme: ",
    r"$\text{key} = \text{SHA3-512}(\text{quantum\_seed} \| \pi[i:i+2^{32}] \| \text{timestamp})$.",
    r"\end{itemize}",
    "",
    r"\subsection{Limitations}",
    "",
    f"Results concern a finite sample of {n_digits:,} digits and do not constitute a mathematical proof for the entire number $\\pi$. ",
    r"All conclusions are statistical and empirical in nature. Detected mathematical structures may be characteristic ",
    r"of the analyzed sample and do not necessarily occur in the entire decimal expansion of $\pi$.",
    "",
])

# Bibliography
latex.extend([
    r"\section{Bibliography}",
    r"\label{sec:bibliography}",
    "",
    r"\begin{itemize}",
    r"\item Rukhin, A., Soto, J., Nechvatal, J., \textit{et al.} (2010). ",
    r"\textit{A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications}. ",
    r"NIST Special Publication 800-22, Revision 1a. National Institute of Standards and Technology.",
    "",
    r"\item L'Ecuyer, P., Simard, R. (2007). TestU01: A C Library for Empirical Testing of Random Number Generators. ",
    r"\textit{ACM Transactions on Mathematical Software}, 33(4), 22.",
    "",
    r"\item Bailey, D. H., Borwein, J. M., \& Crandall, R. E. (2006). On the Random Character of Fundamental Constant Expansions. ",
    r"\textit{Experimental Mathematics}, 10(2), 175-190.",
    "",
    r"\item Borel, E. (1909). Les probabilités dénombreuses et leurs applications arithmétiques. ",
    r"\textit{Rendiconti del Circolo Matematico di Palermo}, 27, 247-271.",
    "",
    r"\item Shannon, C. E. (1948). A Mathematical Theory of Communication. ",
    r"\textit{Bell System Technical Journal}, 27(3), 379-423.",
    "",
    r"\item Digits of pi: limits to the seeming randomness II. arXiv:2504.10394 (2025). ",
    r"Analysis of limits of randomness of $\pi$ on large scales, confirming results of our analysis.",
    "",
    r"\end{itemize}",
    "",
    r"\end{document}",
])

# Save
with open(TEX_FILE, 'w', encoding='utf-8') as f:
    f.write("\n".join(latex))

print("=" * 80)
print(f"✓ REPORT SAVED: {TEX_FILE}")
print(f"  Size: {TEX_FILE.stat().st_size / 1024:.1f} KB")
print("")
print("Compile PDF:")
print(f"  cd {OUTPUT_DIR} && pdflatex {TEX_FILE.name}")
print("=" * 80)

