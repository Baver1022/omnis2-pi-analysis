#!/usr/bin/env python3
"""
KROK 8: ML LSTM Anomaly Detection
- Trening LSTM na 1B cyfr
- Test na 10B cyfr (lub dostępnych)
- Accuracy powinno być ~10% (losowość)
"""

import numpy as np
from .base_step import AnalysisStep
from typing import Dict, Optional

# ML libraries
try:
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, confusion_matrix
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense
    TENSORFLOW_AVAILABLE = True
except ImportError:
    TENSORFLOW_AVAILABLE = False


class Step08MLLSTM(AnalysisStep):
    """ML LSTM Anomaly Detection"""
    
    def execute(self, digits: np.ndarray, checkpoint_data: Optional[Dict] = None) -> Dict:
        n = len(digits)
        
        # Sprawdź dostępność bibliotek
        if not SKLEARN_AVAILABLE:
            return {
                'test_name': 'ML LSTM Anomaly Detection',
                'n': int(n),
                'status': 'SKIP',
                'reason': 'sklearn not available'
            }
        
        if not TENSORFLOW_AVAILABLE:
            return {
                'test_name': 'ML LSTM Anomaly Detection',
                'n': int(n),
                'status': 'SKIP',
                'reason': 'tensorflow not available'
            }
        
        # Parametry
        sequence_length = 10  # Długość sekwencji wejściowej
        train_size = min(1_000_000_000, n // 2)  # Trening na 1B lub połowie
        test_size = min(100_000_000, n - train_size)  # Test na 100M
        
        if train_size < 100_000 or test_size < 10_000:
            return {
                'test_name': 'ML LSTM Anomaly Detection',
                'n': int(n),
                'status': 'SKIP',
                'reason': f'Too few digits: train={train_size}, test={test_size}'
            }
        
        # Przygotuj dane
        print(f"   Przygotowywanie danych: train={train_size:,}, test={test_size:,}")
        
        train_digits = digits[:train_size]
        test_digits = digits[train_size:train_size+test_size]
        
        # Twórz sekwencje (X, y)
        def create_sequences(data, seq_len):
            X, y = [], []
            for i in range(len(data) - seq_len):
                X.append(data[i:i+seq_len])
                y.append(data[i+seq_len])
            return np.array(X), np.array(y)
        
        # Ogranicz rozmiar dla szybkości
        max_train_samples = 1_000_000
        max_test_samples = 100_000
        
        X_train, y_train = create_sequences(train_digits, sequence_length)
        if len(X_train) > max_train_samples:
            indices = np.random.choice(len(X_train), max_train_samples, replace=False)
            X_train = X_train[indices]
            y_train = y_train[indices]
        
        X_test, y_test = create_sequences(test_digits, sequence_length)
        if len(X_test) > max_test_samples:
            indices = np.random.choice(len(X_test), max_test_samples, replace=False)
            X_test = X_test[indices]
            y_test = y_test[indices]
        
        # Normalizuj (0-1)
        X_train = X_train.astype(np.float32) / 9.0
        X_test = X_test.astype(np.float32) / 9.0
        
        # Reshape dla LSTM
        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
        
        # One-hot encode y
        y_train_onehot = tf.keras.utils.to_categorical(y_train, num_classes=10)
        y_test_onehot = tf.keras.utils.to_categorical(y_test, num_classes=10)
        
        # Model LSTM
        print(f"   Trening modelu LSTM...")
        model = Sequential([
            LSTM(50, input_shape=(sequence_length, 1)),
            Dense(10, activation='softmax')
        ])
        
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        # Trening (ograniczony czas)
        epochs = 5  # Szybki trening
        batch_size = 1000
        
        history = model.fit(
            X_train, y_train_onehot,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=0.1,
            verbose=0
        )
        
        # Test
        print(f"   Testowanie modelu...")
        test_loss, test_accuracy = model.evaluate(X_test, y_test_onehot, verbose=0)
        
        # Predykcje
        y_pred = model.predict(X_test, verbose=0)
        y_pred_classes = np.argmax(y_pred, axis=1)
        
        # Accuracy
        accuracy = accuracy_score(y_test, y_pred_classes)
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred_classes)
        
        # Baseline (random guess)
        baseline_accuracy = 0.1  # 10% dla 10 klas
        
        # Status
        if accuracy <= baseline_accuracy * 1.1:  # Tolerancja 10%
            status = 'PASS'  # Losowość potwierdzona
        else:
            status = 'FAIL'  # Wykryto wzorce
        
        results = {
            'test_name': 'ML LSTM Anomaly Detection',
            'n': int(n),
            'train_size': int(train_size),
            'test_size': int(test_size),
            'sequence_length': sequence_length,
            'test_accuracy': float(accuracy),
            'baseline_accuracy': baseline_accuracy,
            'accuracy_ratio': float(accuracy / baseline_accuracy),
            'status': status,
            'interpretation': f"LSTM accuracy: {accuracy*100:.2f}% (baseline: {baseline_accuracy*100:.1f}%) - {'PASS' if status == 'PASS' else 'FAIL'}"
        }
        
        return results

