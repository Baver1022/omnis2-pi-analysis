#!/usr/bin/env python3
"""
ORCHESTRATOR ANALIZY - uruchamia poszczególne kroki niezależnie
- Każdy krok może być przerwany i wznowiony
- Można uruchomić tylko wybrane kroki
- Automatyczne checkpointy
"""

from __future__ import annotations
import numpy as np
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# GPU acceleration
try:
    import cupy as cp
    # Test if CuPy actually works
    test = cp.array([1, 2, 3])
    _ = cp.sum(test)
    _ = cp.empty(10, dtype=cp.uint8)
    GPU_AVAILABLE = True
    print("[GPU] CuPy loaded and tested - GPU acceleration enabled", flush=True)
except Exception as e:
    print(f"[WARNING] CuPy failed: {e}", flush=True)
    print("[CPU] Falling back to CPU mode", flush=True)
    cp = np
    GPU_AVAILABLE = False

# Lazy import - importuj tylko potrzebne kroki
def get_step_class(step_id: str):
    """Lazy loading of step classes"""
    step_map = {
        '01': ('analysis_steps.step_01_frequency', 'Step01Frequency'),
        '02': ('analysis_steps.step_02_runs', 'Step02Runs'),
        '03': ('analysis_steps.step_03_block_frequency', 'Step03BlockFrequency'),
        '04': ('analysis_steps.step_04_entropy', 'Step04Entropy'),
        '05': ('analysis_steps.step_05_spectral_fft', 'Step05SpectralFFT'),
        '06': ('analysis_steps.step_06_compression', 'Step06Compression'),
        '07': ('analysis_steps.step_07_entropy_bounds', 'Step07EntropyBounds'),
        '08': ('analysis_steps.step_08_ml_lstm', 'Step08MLLSTM'),
        '09': ('analysis_steps.step_09_cumulative_sums', 'Step09CumulativeSums'),
        '10': ('analysis_steps.step_10_approximate_entropy', 'Step10ApproximateEntropy'),
        '11': ('analysis_steps.step_11_serial', 'Step11Serial'),
        '12': ('analysis_steps.step_12_linear_complexity', 'Step12LinearComplexity'),
        '13': ('analysis_steps.step_13_random_excursions', 'Step13RandomExcursions'),
        '14': ('analysis_steps.step_14_random_excursions_variant', 'Step14RandomExcursionsVariant'),
        '15': ('analysis_steps.step_15_universal_statistical', 'Step15UniversalStatistical'),
        '16': ('analysis_steps.step_16_non_overlapping_template', 'Step16NonOverlappingTemplate'),
        '17': ('analysis_steps.step_17_overlapping_template', 'Step17OverlappingTemplate'),
        '18': ('analysis_steps.step_18_birthday_spacings', 'Step18BirthdaySpacings'),
        '19': ('analysis_steps.step_19_collision', 'Step19Collision'),
        '20': ('analysis_steps.step_20_gap', 'Step20Gap'),
        '21': ('analysis_steps.step_21_simple_poker', 'Step21SimplePoker'),
        '22': ('analysis_steps.step_22_coupon_collector', 'Step22CouponCollector'),
        '23': ('analysis_steps.step_23_maxoft', 'Step23MaxOft'),
        '24': ('analysis_steps.step_24_weight_distrib', 'Step24WeightDistrib'),
        '25': ('analysis_steps.step_25_matrix_rank', 'Step25MatrixRank'),
        '26': ('analysis_steps.step_26_hamming_indep', 'Step26HammingIndep'),
        '27': ('analysis_steps.step_27_random_walk1', 'Step27RandomWalk1'),
    }
    
    if step_id not in step_map:
        raise ValueError(f"Unknown step: {step_id}")
    
    module_name, class_name = step_map[step_id]
    module = __import__(module_name, fromlist=[class_name])
    return getattr(module, class_name)


class AnalysisOrchestrator:
    """
    Orchestrator dla modularnej analizy
    """
    
    def __init__(self, output_dir: str, pi_file: str, max_digits: Optional[int] = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.pi_file = Path(pi_file)
        self.max_digits = max_digits
        
        # Plik podsumowania
        self.summary_file = self.output_dir / "analysis_summary.json"
        
        # Lista wszystkich kroków (27 testów) - tylko metadane
        self.steps = [
            ('01', 'Frequency Test (NIST)'),
            ('02', 'Runs Test (NIST)'),
            ('03', 'Block Frequency Test (NIST)'),
            ('04', 'Entropy Analysis'),
            ('05', 'Spectral FFT Analysis (GPU)'),
            ('06', 'Compression Test'),
            ('07', 'Empirical Entropy Bounds'),
            ('08', 'ML LSTM Anomaly Detection'),
            ('09', 'Cumulative Sums Test (NIST)'),
            ('10', 'Approximate Entropy Test (NIST)'),
            ('11', 'Serial Test (NIST)'),
            ('12', 'Linear Complexity Test (NIST)'),
            ('13', 'Random Excursions Test (NIST)'),
            ('14', 'Random Excursions Variant (NIST)'),
            ('15', 'Universal Statistical Test (NIST)'),
            ('16', 'Non-overlapping Template (NIST)'),
            ('17', 'Overlapping Template (NIST)'),
            ('18', 'SmallCrush: BirthdaySpacings'),
            ('19', 'SmallCrush: Collision'),
            ('20', 'SmallCrush: Gap'),
            ('21', 'SmallCrush: SimplePoker'),
            ('22', 'SmallCrush: CouponCollector'),
            ('23', 'SmallCrush: MaxOft'),
            ('24', 'SmallCrush: WeightDistrib'),
            ('25', 'SmallCrush: MatrixRank'),
            ('26', 'SmallCrush: HammingIndep'),
            ('27', 'SmallCrush: RandomWalk1')
        ]
        
        # Instancje kroków - lazy loading
        self.step_instances = {}
    
    def load_digits(self) -> np.ndarray:
        """Load Pi digits - OPTIMIZED: GPU + CPU parallel processing"""
        print(f"[LOAD] Streaming from: {self.pi_file}", flush=True)
        
        max_digits = self.max_digits if self.max_digits else 10_000_000_000
        print(f"[OPTIMIZED] Loading {max_digits:,} digits {'[GPU+CPU]' if GPU_AVAILABLE else '[CPU]'}...", flush=True)
        
        if GPU_AVAILABLE:
            # GPU PATH: Pre-allocate + CUDA streams + pinned memory
            print(f"[GPU] Pre-allocating {max_digits:,} digits in VRAM...", flush=True)
            result = cp.empty(max_digits, dtype=cp.uint8)
            
            # Create CUDA stream for async operations
            stream = cp.cuda.Stream()
            
            # Translation table for fast digit extraction (10x faster than list comprehension)
            trans_table = str.maketrans('', '', ''.join(chr(i) for i in range(256) if chr(i) not in '0123456789'))
            
            offset = 0
            batch_size = 100_000_000  # 100M per batch for better parallelism
            
            with open(self.pi_file, 'r', buffering=1024*1024) as f:
                # Skip "3."
                header = f.read(2)
                if header != '3.':
                    f.seek(0)
                
                while offset < max_digits:
                    # CPU: Read and clean (vectorized)
                    remaining = max_digits - offset
                    batch_chars = f.read(min(batch_size, remaining))
                    
                    if not batch_chars:
                        break
                    
                    # FAST: Use translate to remove non-digits (100x faster than list comp)
                    clean_chars = batch_chars.translate(trans_table)
                    
                    if not clean_chars:
                        continue
                    
                    # FAST: Convert string to bytes, then to numpy
                    batch_bytes = clean_chars.encode('ascii')
                    batch_np = np.frombuffer(batch_bytes, dtype='S1').view(np.uint8) - 48  # '0' = ASCII 48
                    
                    batch_len = len(batch_np)
                    if batch_len == 0:
                        continue
                    
                    # GPU: Async transfer using stream
                    with stream:
                        # Direct copy to pre-allocated GPU memory (no intermediate allocation)
                        result[offset:offset+batch_len] = cp.asarray(batch_np)
                    
                    offset += batch_len
                    
                    # Progress
                    if offset % 500_000_000 == 0 or offset >= max_digits:
                        stream.synchronize()  # Wait for GPU
                        print(f"[GPU+CPU] {offset:,}/{max_digits:,} ({100*offset/max_digits:.1f}%) | VRAM: {offset} bytes", flush=True)
                    
                    if offset >= max_digits:
                        break
            
            # Final sync
            stream.synchronize()
            print(f"[GPU] READY: {offset:,} digits in VRAM (pre-allocated, zero-copy)", flush=True)
            
            # Trim if we read less than expected
            if offset < max_digits:
                result = result[:offset]
            
            return result
        
        else:
            # CPU PATH: Simple and fast
            print(f"[CPU] Loading {max_digits:,} digits to RAM...", flush=True)
            
            trans_table = str.maketrans('', '', ''.join(chr(i) for i in range(256) if chr(i) not in '0123456789'))
            
            with open(self.pi_file, 'r', buffering=1024*1024) as f:
                header = f.read(2)
                if header != '3.':
                    f.seek(0)
                
                # Read in chunks - FAST without list comprehension
                print(f"[CPU] Reading file in chunks...", flush=True)
                chunks = []
                chunk_size = 100_000_000  # 100M per chunk
                total_read = 0
                
                while total_read < max_digits:
                    chunk = f.read(min(chunk_size, max_digits - total_read))
                    if not chunk:
                        break
                    
                    # Fast: filter only digits, convert to bytes, then numpy
                    clean = chunk.translate(trans_table)
                    if clean:
                        # Use bytearray for speed
                        byte_array = bytearray(clean, 'ascii')
                        # Subtract ASCII offset '0' = 48
                        chunk_arr = np.array(byte_array, dtype=np.uint8) - 48
                        chunks.append(chunk_arr)
                        total_read += len(chunk_arr)
                    
                    if total_read % 1_000_000_000 == 0 or (total_read % 1_000_000_000 < chunk_size and total_read > 0):
                        print(f"[CPU] Loaded {total_read:,}/{max_digits:,} digits ({100*total_read/max_digits:.1f}%)", flush=True)
                
                print(f"[CPU] Concatenating {len(chunks)} chunks...", flush=True)
                result = np.concatenate(chunks)
                print(f"[CPU] READY: {len(result):,} digits in RAM", flush=True)
                return result[:max_digits]
    
    def _get_step_instance(self, step_id: str):
        """Get or create step instance (lazy loading)"""
        if step_id not in self.step_instances:
            step_name = dict(self.steps).get(step_id, f"Step {step_id}")
            step_class = get_step_class(step_id)
            self.step_instances[step_id] = step_class(
                step_id=step_id,
                step_name=step_name,
                output_dir=self.output_dir
            )
        return self.step_instances[step_id]
    
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
        
        for step_id, step_name in self.steps:
            # Check status from files without loading step
            status_file = self.output_dir / f"{step_id}_status.json"
            if status_file.exists():
                try:
                    with open(status_file, 'r') as f:
                        step_state = json.load(f)
                    step_status = step_state.get('status', 'pending')
                except:
                    step_status = 'pending'
            else:
                step_status = 'pending'
            status['steps'][step_id] = {
                'name': step_name,
                'status': step_status
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
        print(f"STATUS ANALIZY")
        print(f"{'='*70}")
        print(f"Zakończone: {status['completed']}/{status['total_steps']}")
        print(f"W trakcie: {status['running']}")
        print(f"Nieudane: {status['failed']}")
        print(f"Pominięte: {status['skipped']}")
        print(f"Oczekujące: {status['pending']}")
        print()
        
        for step_id, step_info in status['steps'].items():
            status_icon = {
                'completed': '[OK]',
                'running': '[RUN]',
                'failed': '[FAIL]',
                'skipped': '[SKIP]',
                'pending': '[WAIT]'
            }.get(step_info['status'], '[?]')
            
            print(f"  {status_icon} {step_id}: {step_info['name']} - {step_info['status']}")
    
    def run_step(self, step_id: str, digits: np.ndarray, force: bool = False):
        """Uruchom pojedynczy krok"""
        try:
            step = self._get_step_instance(step_id)
            return step.run(digits, force=force)
        except Exception as e:
            print(f"[ERROR] Failed to load/run step {step_id}: {e}")
            return None
    
    def run_all(self, step_ids: Optional[List[str]] = None, force: bool = False):
        """Uruchom wszystkie kroki (lub wybrane) - OPTIMIZED"""
        if step_ids is None:
            step_ids = [step_id for step_id, _ in self.steps]
        
        print(f"\n[START] Running {len(step_ids)} steps...", flush=True)
        
        # OPTYMALIZACJA: Załaduj dane RAZ dla wszystkich kroków
        print(f"\n{'='*70}", flush=True)
        print(f"[LOADING] Loading digits ONCE for all {len(step_ids)} steps...", flush=True)
        print(f"{'='*70}", flush=True)
        
        try:
            digits = self.load_digits()
            print(f"[READY] Data loaded, starting tests...", flush=True)
        except Exception as e:
            print(f"[FATAL] Failed to load digits: {e}", flush=True)
            import traceback
            traceback.print_exc()
            return {}
        
        results = {}
        
        for i, step_id in enumerate(step_ids, 1):
            try:
                step = self._get_step_instance(step_id)
                print(f"\n{'='*70}", flush=True)
                print(f"[STEP {i}/{len(step_ids)}] {step_id}: {step.step_name}", flush=True)
                print(f"{'='*70}", flush=True)
                
                # Uruchom test (dane już załadowane w GPU/RAM)
                step_result = self.run_step(step_id, digits, force=force)
                if step_result:
                    results[step_id] = step_result
                    print(f"\n[SUCCESS] Step {step_id} completed and saved!", flush=True)
                
                # GPU memory cleanup po każdym kroku
                if GPU_AVAILABLE:
                    cp.get_default_memory_pool().free_all_blocks()
                
            except Exception as e:
                print(f"\n[ERROR] Step {step_id} failed: {e}", flush=True)
                import traceback
                traceback.print_exc()
                
                # Zapisz błąd
                try:
                    step = self._get_step_instance(step_id)
                except:
                    step = None
                if step:
                    error_result = {
                        'test_name': step.step_name,
                        'status': 'FAILED',
                        'error': str(e),
                        'timestamp': datetime.now().isoformat()
                    }
                    try:
                        step.fail(str(e))
                        step._save_results(error_result)
                        print(f"[SAVED] Error logged for step {step_id}", flush=True)
                    except:
                        pass
                
                # Kontynuuj z następnym testem
                continue
        
        # Zwolnij pamięć po wszystkich testach
        print(f"\n[CLEANUP] Freeing memory...", flush=True)
        del digits
        import gc
        gc.collect()
        if GPU_AVAILABLE:
            cp.get_default_memory_pool().free_all_blocks()
            print(f"[GPU] Memory freed", flush=True)
        
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
        
        print(f"\n[SAVED] Summary: {self.summary_file}")


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

