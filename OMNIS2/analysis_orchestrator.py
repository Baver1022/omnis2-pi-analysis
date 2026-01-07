#!/usr/bin/env python3
"""
ORCHESTRATOR ANALIZY - uruchamia poszczególne kroki niezależnie
- Każdy krok może być przerwany i wznowiony
- Można uruchomić tylko wybrane kroki
- Automatyczne checkpointy
"""

import numpy as np
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Import kroków
from analysis_steps.step_01_frequency import Step01Frequency
from analysis_steps.step_02_runs import Step02Runs
from analysis_steps.step_03_block_frequency import Step03BlockFrequency
from analysis_steps.step_04_entropy import Step04Entropy
from analysis_steps.step_05_spectral_fft import Step05SpectralFFT
from analysis_steps.step_06_compression import Step06Compression
from analysis_steps.step_07_entropy_bounds import Step07EntropyBounds
from analysis_steps.step_08_ml_lstm import Step08MLLSTM
from analysis_steps.step_09_cumulative_sums import Step09CumulativeSums
from analysis_steps.step_10_approximate_entropy import Step10ApproximateEntropy
from analysis_steps.step_11_serial import Step11Serial
from analysis_steps.step_12_linear_complexity import Step12LinearComplexity
from analysis_steps.step_13_random_excursions import Step13RandomExcursions
from analysis_steps.step_14_random_excursions_variant import Step14RandomExcursionsVariant
from analysis_steps.step_15_universal_statistical import Step15UniversalStatistical
from analysis_steps.step_16_non_overlapping_template import Step16NonOverlappingTemplate
from analysis_steps.step_17_overlapping_template import Step17OverlappingTemplate
from analysis_steps.step_18_birthday_spacings import Step18BirthdaySpacings
from analysis_steps.step_19_collision import Step19Collision
from analysis_steps.step_20_gap import Step20Gap
from analysis_steps.step_21_simple_poker import Step21SimplePoker
from analysis_steps.step_22_coupon_collector import Step22CouponCollector
from analysis_steps.step_23_maxoft import Step23MaxOft
from analysis_steps.step_24_weight_distrib import Step24WeightDistrib
from analysis_steps.step_25_matrix_rank import Step25MatrixRank
from analysis_steps.step_26_hamming_indep import Step26HammingIndep
from analysis_steps.step_27_random_walk1 import Step27RandomWalk1


class AnalysisOrchestrator:
    """
    Orchestrator dla modularnej analizy
    """
    
    def __init__(self, output_dir: str, pi_file: str, max_digits: Optional[int] = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.pi_file = Path(pi_file)
        self.max_digits = max_digits
        
        # Plik konfiguracji
        self.config_file = self.output_dir / "analysis_config.json"
        self.summary_file = self.output_dir / "analysis_summary.json"
        
        # Lista wszystkich kroków (OPCJA B: 25 testów + ML)
        self.steps = [
            # Podstawowe testy NIST (6)
            ('01', 'Frequency Test (NIST)', Step01Frequency),
            ('02', 'Runs Test (NIST)', Step02Runs),
            ('03', 'Block Frequency Test (NIST)', Step03BlockFrequency),
            ('04', 'Entropy Analysis', Step04Entropy),
            ('05', 'Spectral FFT Analysis (GPU)', Step05SpectralFFT),
            ('06', 'Compression Test', Step06Compression),
            # Rozszerzone analizy
            ('07', 'Empirical Entropy Bounds', Step07EntropyBounds),
            ('08', 'ML LSTM Anomaly Detection', Step08MLLSTM),
            # Dodatkowe testy NIST (9) - W TRAKCIE IMPLEMENTACJI
            ('09', 'Cumulative Sums Test (NIST)', Step09CumulativeSums),
            ('10', 'Approximate Entropy Test (NIST)', Step10ApproximateEntropy),
            ('11', 'Serial Test (NIST)', Step11Serial),
            ('12', 'Linear Complexity Test (NIST)', Step12LinearComplexity),
            ('13', 'Random Excursions Test (NIST)', Step13RandomExcursions),
            ('14', 'Random Excursions Variant (NIST)', Step14RandomExcursionsVariant),
            ('15', 'Universal Statistical Test (NIST)', Step15UniversalStatistical),
            ('16', 'Non-overlapping Template (NIST)', Step16NonOverlappingTemplate),
            ('17', 'Overlapping Template (NIST)', Step17OverlappingTemplate),
            # SmallCrush tests (10)
            ('18', 'SmallCrush: BirthdaySpacings', Step18BirthdaySpacings),
            ('19', 'SmallCrush: Collision', Step19Collision),
            ('20', 'SmallCrush: Gap', Step20Gap),
            ('21', 'SmallCrush: SimplePoker', Step21SimplePoker),
            ('22', 'SmallCrush: CouponCollector', Step22CouponCollector),
            ('23', 'SmallCrush: MaxOft', Step23MaxOft),
            ('24', 'SmallCrush: WeightDistrib', Step24WeightDistrib),
            ('25', 'SmallCrush: MatrixRank', Step25MatrixRank),
            ('26', 'SmallCrush: HammingIndep', Step26HammingIndep),
            ('27', 'SmallCrush: RandomWalk1', Step27RandomWalk1),
            # ('13', 'Random Excursions Test (NIST)', ...),
            # ('14', 'Random Excursions Variant (NIST)', ...),
            # ('15', 'Universal Statistical Test (NIST)', ...),
            # ('16', 'Non-overlapping Template (NIST)', ...),
            # ('17', 'Overlapping Template (NIST)', ...),
            # TODO: SmallCrush (10 testów) - do implementacji
            # ('18', 'SmallCrush: smarsa_BirthdaySpacings', ...),
            # ('19', 'SmallCrush: smarsa_Collision', ...),
            # ... (8 więcej)
        ]
        
        # Instancje kroków
        self.step_instances = {}
        for step_id, step_name, step_class in self.steps:
            self.step_instances[step_id] = step_class(
                step_id=step_id,
                step_name=step_name,
                output_dir=self.output_dir
            )
    
    def load_digits(self) -> np.ndarray:
        """Load Pi digits (batch-wise for large files)"""
        print(f"[LOAD] Reading digits from: {self.pi_file}", flush=True)
        
        digits = []
        total_read = 0
        batch_size = 10_000_000  # 10M digits per batch
        
        # Limit to safe memory size
        max_safe_digits = 1_000_000_000  # 1B digits max in RAM
        
        effective_max = min(self.max_digits, max_safe_digits) if self.max_digits else max_safe_digits
        
        if self.max_digits and self.max_digits > max_safe_digits:
            print(f"[WARNING] Limiting to {max_safe_digits:,} digits (safe memory limit)", flush=True)
            print(f"[WARNING] Full 10B analysis requires streaming processing", flush=True)
        
        with open(self.pi_file, 'r') as f:
            # Skip "3."
            header = f.read(2)
            if header != '3.':
                f.seek(0)
            
            while True:
                if effective_max and total_read >= effective_max:
                    break
                
                # Read batch
                remaining = (effective_max - total_read) if effective_max else batch_size
                batch = f.read(min(batch_size, remaining))
                
                if not batch:
                    break
                
                # Convert to digits
                batch_digits = [int(d) for d in batch if d.isdigit()]
                digits.extend(batch_digits)
                total_read += len(batch_digits)
                
                # Progress
                if total_read % 10_000_000 == 0:
                    print(f"[PROGRESS] Loaded {total_read:,} digits...", flush=True)
                
                if effective_max and total_read >= effective_max:
                    break
        
        result = np.array(digits[:effective_max] if effective_max else digits, dtype=np.uint8)
        print(f"[SUCCESS] Loaded {len(result):,} digits total", flush=True)
        return result
    
    def get_status(self) -> Dict:
        """Pobierz status wszystkich kroków"""
        status = {
            'total_steps': len(self.steps),
            'completed': 0,
            'running': 0,
            'failed': 0,
            'skipped': 0,
            'pending': 0,
            'steps': {}
        }
        
        for step_id, step_name, _ in self.steps:
            step = self.step_instances[step_id]
            step_status = step.state['status']
            status['steps'][step_id] = {
                'name': step_name,
                'status': step_status,
                'started_at': step.state.get('started_at'),
                'completed_at': step.state.get('completed_at'),
                'error': step.state.get('error')
            }
            
            if step_status == 'completed':
                status['completed'] += 1
            elif step_status == 'running':
                status['running'] += 1
            elif step_status == 'failed':
                status['failed'] += 1
            elif step_status == 'skipped':
                status['skipped'] += 1
            else:
                status['pending'] += 1
        
        return status
    
    def print_status(self):
        """Wyświetl status"""
        status = self.get_status()
        
        print(f"\n{'='*70}")
        print(f"📊 STATUS ANALIZY")
        print(f"{'='*70}")
        print(f"Zakończone: {status['completed']}/{status['total_steps']}")
        print(f"W trakcie: {status['running']}")
        print(f"Nieudane: {status['failed']}")
        print(f"Pominięte: {status['skipped']}")
        print(f"Oczekujące: {status['pending']}")
        print()
        
        for step_id, step_info in status['steps'].items():
            status_icon = {
                'completed': '✅',
                'running': '🔄',
                'failed': '❌',
                'skipped': '⏭️',
                'pending': '⏳'
            }.get(step_info['status'], '❓')
            
            print(f"  {status_icon} {step_id}: {step_info['name']} - {step_info['status']}")
            if step_info['error']:
                print(f"      Błąd: {step_info['error']}")
    
    def run_step(self, step_id: str, digits: np.ndarray, force: bool = False):
        """Uruchom pojedynczy krok"""
        if step_id not in self.step_instances:
            print(f"❌ Nieznany krok: {step_id}")
            return None
        
        step = self.step_instances[step_id]
        return step.run(digits, force=force)
    
    def run_all(self, step_ids: Optional[List[str]] = None, force: bool = False):
        """Uruchom wszystkie kroki (lub wybrane)"""
        # Wybór kroków
        if step_ids is None:
            step_ids = [step_id for step_id, _, _ in self.steps]
        
        print(f"\n[START] Running {len(step_ids)} steps...", flush=True)
        
        results = {}
        
        for step_id in step_ids:
            if step_id not in self.step_instances:
                print(f"[WARNING] Unknown step: {step_id} - skipping", flush=True)
                continue
            
            try:
                print(f"\n{'='*70}", flush=True)
                print(f"[STEP] Running step {step_id}: {self.step_instances[step_id].step_name}", flush=True)
                print(f"{'='*70}", flush=True)
                
                # Load digits for this step (streaming)
                print(f"[LOADING] Loading digits for step {step_id}...", flush=True)
                digits = self.load_digits()
                
                step_result = self.run_step(step_id, digits, force=force)
                if step_result:
                    results[step_id] = step_result
                    print(f"\n[SUCCESS] Step {step_id} completed!", flush=True)
                
                # Free memory
                del digits
                import gc
                gc.collect()
                
            except Exception as e:
                print(f"\n[ERROR] Step {step_id} failed: {e}", flush=True)
                import traceback
                traceback.print_exc()
                continue
        
        # Zapisz podsumowanie
        self.save_summary(results)
        
        return results
    
    def save_summary(self, results: Dict):
        """Zapisz podsumowanie"""
        status = self.get_status()
        
        summary = {
            'timestamp': datetime.now().isoformat(),
            'pi_file': str(self.pi_file),
            'max_digits': self.max_digits,
            'status': status,
            'results': results
        }
        
        with open(self.summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n💾 Podsumowanie zapisane: {self.summary_file}")


def main():
    parser = argparse.ArgumentParser(description='Modular Analysis Orchestrator')
    parser.add_argument('--pi-file', type=str, required=True, help='Plik z cyframi π')
    parser.add_argument('--output-dir', type=str, default='analysis_results', help='Katalog wyników')
    parser.add_argument('--max-digits', type=int, default=None, help='Maksymalna liczba cyfr')
    parser.add_argument('--steps', type=str, nargs='+', default=None, 
                       help='Lista kroków do uruchomienia (np. 01 02 03)')
    parser.add_argument('--status', action='store_true', help='Pokaż status i wyjdź')
    parser.add_argument('--force', action='store_true', help='Wymuś ponowne uruchomienie')
    
    args = parser.parse_args()
    
    orchestrator = AnalysisOrchestrator(
        output_dir=args.output_dir,
        pi_file=args.pi_file,
        max_digits=args.max_digits
    )
    
    # Status
    if args.status:
        orchestrator.print_status()
        return
    
    # Uruchom kroki
    orchestrator.run_all(step_ids=args.steps, force=args.force)
    
    # Pokaż status końcowy
    orchestrator.print_status()


if __name__ == "__main__":
    main()

