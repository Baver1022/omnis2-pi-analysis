#!/usr/bin/env python3
"""
Base class dla wszystkich kroków analizy
- Każdy krok jest niezależny
- Ma własny checkpoint
- Może być przerwany i wznowiony
"""

from __future__ import annotations
import json
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, TYPE_CHECKING
import time

if TYPE_CHECKING:
    import numpy.typing as npt


class AnalysisStep:
    """
    Bazowa klasa dla kroku analizy
    """
    
    def __init__(self, step_id: str, step_name: str, output_dir: Path):
        self.step_id = step_id
        self.step_name = step_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Pliki checkpoint i wyników
        self.checkpoint_file = self.output_dir / f"{step_id}_checkpoint.json"
        self.results_file = self.output_dir / f"{step_id}_results.json"
        self.status_file = self.output_dir / f"{step_id}_status.json"
        
        # Stan kroku
        self.state = {
            'step_id': step_id,
            'step_name': step_name,
            'status': 'pending',  # pending, running, completed, failed, skipped
            'started_at': None,
            'completed_at': None,
            'digits_processed': 0,
            'total_digits': 0,
            'error': None
        }
        
        self._load_status()
    
    def _load_status(self):
        """Wczytaj status kroku"""
        if self.status_file.exists():
            try:
                with open(self.status_file, 'r') as f:
                    self.state = json.load(f)
            except:
                pass
    
    def _save_status(self):
        """Zapisz status kroku"""
        with open(self.status_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def _save_checkpoint(self, checkpoint_data: Dict):
        """Zapisz checkpoint"""
        checkpoint_data['timestamp'] = datetime.now().isoformat()
        with open(self.checkpoint_file, 'w') as f:
            json.dump(checkpoint_data, f, indent=2)
    
    def _load_checkpoint(self) -> Optional[Dict]:
        """Wczytaj checkpoint"""
        if self.checkpoint_file.exists():
            try:
                with open(self.checkpoint_file, 'r') as f:
                    return json.load(f)
            except:
                return None
        return None
    
    def _save_results(self, results: Dict):
        """Zapisz wyniki"""
        results['step_id'] = self.step_id
        results['step_name'] = self.step_name
        results['timestamp'] = datetime.now().isoformat()
        results['status'] = self.state['status']
        
        with open(self.results_file, 'w') as f:
            json.dump(results, f, indent=2)
    
    def is_completed(self) -> bool:
        """Sprawdź czy krok jest zakończony"""
        return self.state['status'] == 'completed'
    
    def is_skipped(self) -> bool:
        """Sprawdź czy krok jest pominięty"""
        return self.state['status'] == 'skipped'
    
    def skip(self, reason: str = "User skipped"):
        """Pomiń krok"""
        self.state['status'] = 'skipped'
        self.state['error'] = reason
        self._save_status()
    
    def start(self, total_digits: int):
        """Rozpocznij krok"""
        self.state['status'] = 'running'
        self.state['started_at'] = datetime.now().isoformat()
        self.state['total_digits'] = total_digits
        self._save_status()
    
    def complete(self, results: Dict):
        """Zakończ krok z wynikami"""
        self.state['status'] = 'completed'
        self.state['completed_at'] = datetime.now().isoformat()
        self.state['digits_processed'] = self.state['total_digits']
        self._save_status()
        self._save_results(results)
    
    def fail(self, error: str):
        """Oznacz krok jako nieudany"""
        self.state['status'] = 'failed'
        self.state['error'] = str(error)
        self.state['completed_at'] = datetime.now().isoformat()
        self._save_status()
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        """
        Wykonaj krok analizy
        To powinno być nadpisane w klasach pochodnych
        """
        raise NotImplementedError("Subclass must implement execute()")
    
    def run(self, digits: np.ndarray, force: bool = False) -> Dict:
        """
        Uruchom krok (z automatycznym checkpointing)
        """
        # Sprawdź czy już zakończony
        if self.is_completed() and not force:
            print(f"[SKIP] Krok {self.step_id} juz zakonczony - pomijam", flush=True)
            if self.results_file.exists():
                with open(self.results_file, 'r') as f:
                    return json.load(f)
            return {}
        
        if self.is_skipped():
            print(f"[SKIP] Krok {self.step_id} pominiety", flush=True)
            return {}
        
        # Rozpocznij
        self.start(len(digits))
        print(f"\n{'='*70}")
        print(f" KROK {self.step_id}: {self.step_name}")
        print(f"{'='*70}")
        
        start_time = time.time()
        
        try:
            # Wczytaj checkpoint jeśli istnieje
            checkpoint = self._load_checkpoint() if not force else None
            
            # Wykonaj krok
            results = self.execute(digits, checkpoint)
            
            # Zakończ
            elapsed = time.time() - start_time
            results['execution_time'] = elapsed
            self.complete(results)
            
            print(f"\n Krok {self.step_id} zakończony w {elapsed:.1f}s")
            return results
            
        except Exception as e:
            self.fail(str(e))
            print(f"\n Krok {self.step_id} nieudany: {e}")
            raise

