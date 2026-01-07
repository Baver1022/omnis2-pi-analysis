# GPU acceleration - dodaj na początku każdego kroku
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    cp = np
    GPU_AVAILABLE = False

# W execute() - detect GPU array
def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
    xp = cp.get_array_module(digits) if GPU_AVAILABLE else np
    is_gpu = xp == cp
    
    # Użyj xp zamiast np dla wszystkich obliczeń
    result = xp.sum(digits)  # przykład
    
    # Transfer wyników z GPU do CPU przed return
    if is_gpu:
        result = float(cp.asnumpy(result))
