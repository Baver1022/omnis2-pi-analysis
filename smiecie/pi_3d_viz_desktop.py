#!/usr/bin/env python3
"""
Desktopowa wizualizacja 3D cyfr π
Używa PyOpenGL dla wydajnej wizualizacji dużych zbiorów danych
"""

import sys
import os
import numpy as np
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QProgressBar)
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
import struct

class PiVisualization3D(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.points = None
        self.colors = None
        self.count = 0
        self.rotation_x = 15.0
        self.rotation_y = 45.0
        self.zoom = 15.0
        self.mouse_pressed = False
        self.last_pos = None
        
    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        
    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, width / height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Kamera
        glTranslatef(0, 0, -self.zoom)
        glRotatef(self.rotation_x, 1, 0, 0)
        glRotatef(self.rotation_y, 0, 1, 0)
        glTranslatef(-4.5, -4.5, -4.5)
        
        if self.points is not None and self.count > 0:
            # Rysuj punkty
            glPointSize(2.0)
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            
            glVertexPointer(3, GL_FLOAT, 0, self.points)
            glColorPointer(3, GL_FLOAT, 0, self.colors)
            glDrawArrays(GL_POINTS, 0, self.count)
            
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
        
        # Rysuj ramkę
        self.draw_box()
        
    def draw_box(self):
        glLineWidth(2.0)
        glColor3f(0.0, 1.0, 1.0)
        glBegin(GL_LINES)
        # Dolna płaszczyzna
        glVertex3f(0, 0, 0); glVertex3f(10, 0, 0)
        glVertex3f(10, 0, 0); glVertex3f(10, 0, 10)
        glVertex3f(10, 0, 10); glVertex3f(0, 0, 10)
        glVertex3f(0, 0, 10); glVertex3f(0, 0, 0)
        # Górna płaszczyzna
        glVertex3f(0, 10, 0); glVertex3f(10, 10, 0)
        glVertex3f(10, 10, 0); glVertex3f(10, 10, 10)
        glVertex3f(10, 10, 10); glVertex3f(0, 10, 10)
        glVertex3f(0, 10, 10); glVertex3f(0, 10, 0)
        # Pionowe krawędzie
        glVertex3f(0, 0, 0); glVertex3f(0, 10, 0)
        glVertex3f(10, 0, 0); glVertex3f(10, 10, 0)
        glVertex3f(10, 0, 10); glVertex3f(10, 10, 10)
        glVertex3f(0, 0, 10); glVertex3f(0, 10, 10)
        glEnd()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_pressed = True
            self.last_pos = event.position()
            
    def mouseMoveEvent(self, event):
        if self.mouse_pressed and self.last_pos:
            dx = event.position().x() - self.last_pos.x()
            dy = event.position().y() - self.last_pos.y()
            self.rotation_y += dx * 0.5
            self.rotation_x += dy * 0.5
            self.update()
            self.last_pos = event.position()
            
    def mouseReleaseEvent(self, event):
        self.mouse_pressed = False
        
    def wheelEvent(self, event):
        delta = event.angleDelta().y() / 120.0
        self.zoom = max(5.0, min(30.0, self.zoom - delta))
        self.update()
        
    def set_data(self, points, colors, count):
        self.points = points
        self.colors = colors
        self.count = count
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("π — Wizualizacja 3D (1B cyfr)")
        self.setGeometry(100, 100, 1400, 900)
        
        # Centralny widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QHBoxLayout(central_widget)
        
        # Panel kontrolny
        control_panel = QWidget()
        control_panel.setFixedWidth(250)
        control_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 200);
                border: 2px solid #0ff;
                border-radius: 5px;
            }
            QLabel {
                color: #0ff;
                font-family: monospace;
                font-size: 11px;
                padding: 5px;
            }
            QPushButton {
                background-color: #000;
                color: #0ff;
                border: 1px solid #0ff;
                border-radius: 3px;
                padding: 8px;
                font-family: monospace;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #0ff;
                color: #000;
            }
            QProgressBar {
                border: 1px solid #0ff;
                border-radius: 3px;
                text-align: center;
                color: #0ff;
            }
            QProgressBar::chunk {
                background-color: #0ff;
            }
        """)
        
        control_layout = QVBoxLayout(control_panel)
        
        # Info
        self.info_label = QLabel("π — 100 000 000 cyfr (TEST)\nXYZ = kolejne trójki\nPunkty: max 10M (próbkowanie)")
        self.status_label = QLabel("Ładowanie...")
        self.progress_label = QLabel("")
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        # Przyciski
        self.btn_reset = QPushButton("Chmura 3D")
        self.btn_density = QPushButton("Gęstość voxel")
        self.btn_proj_xy = QPushButton("Projekcja XY")
        self.btn_proj_xz = QPushButton("Projekcja XZ")
        self.btn_proj_yz = QPushButton("Projekcja YZ")
        self.btn_animate = QPushButton("Animacja okna")
        
        control_layout.addWidget(self.info_label)
        control_layout.addWidget(self.status_label)
        control_layout.addWidget(self.progress_label)
        control_layout.addWidget(self.progress_bar)
        control_layout.addStretch()
        control_layout.addWidget(self.btn_reset)
        control_layout.addWidget(self.btn_density)
        control_layout.addWidget(self.btn_proj_xy)
        control_layout.addWidget(self.btn_proj_xz)
        control_layout.addWidget(self.btn_proj_yz)
        control_layout.addWidget(self.btn_animate)
        
        # Wizualizacja 3D
        self.viz = PiVisualization3D()
        
        layout.addWidget(control_panel)
        layout.addWidget(self.viz, 1)
        
        # Dane
        self.digits = None
        self.points_pos = None
        self.points_col = None
        self.points_original = None
        self.count = 0
        
        # Połączenia
        self.btn_reset.clicked.connect(self.reset_view)
        self.btn_density.clicked.connect(self.show_density)
        self.btn_proj_xy.clicked.connect(lambda: self.set_projection('XY'))
        self.btn_proj_xz.clicked.connect(lambda: self.set_projection('XZ'))
        self.btn_proj_yz.clicked.connect(lambda: self.set_projection('YZ'))
        self.btn_animate.clicked.connect(self.toggle_animation)
        
        # Załaduj dane w wątku
        self.loader_thread = DataLoaderThread()
        self.loader_thread.progress_update.connect(self.update_progress)
        self.loader_thread.data_loaded.connect(self.on_data_loaded)
        self.loader_thread.start()
        
    def update_progress(self, file_idx, files_needed, status):
        """Aktualizuj pasek postępu"""
        self.progress_label.setText(f"Plik {file_idx}/{files_needed}: {status}")
        self.progress_bar.setValue(int((file_idx / files_needed) * 100))
        self.status_label.setText(status)
        
    def on_data_loaded(self, digits):
        """Wywoływane gdy dane są załadowane"""
        self.digits = digits
        self.status_label.setText(f"Wczytano {len(self.digits):,} cyfr")
        # Przetwórz na punkty w wątku
        self.processor_thread = DataProcessorThread(self.digits)
        self.processor_thread.progress_update.connect(self.update_progress)
        self.processor_thread.points_ready.connect(self.on_points_ready)
        self.processor_thread.start()
        
    def on_points_ready(self, pos, col, count):
        """Wywoływane gdy punkty są gotowe"""
        self.points_pos = pos
        self.points_col = col
        self.count = count
        # Zapisz oryginalne pozycje jako numpy array
        self.points_original = np.frombuffer(pos, dtype=np.float32).reshape(-1, 3).copy()
        self.viz.set_data(pos, col, count)
        self.status_label.setText(f"Gotowe! {count:,} punktów 3D")
        self.progress_label.setText("Wizualizacja gotowa!")
        self.progress_bar.setValue(100)
        
    def reset_view(self):
        """Reset do oryginalnych danych"""
        if self.points_original is not None:
            self.points_pos = self.points_original.tobytes()
            self.viz.set_data(self.points_pos, self.points_col, self.count)
            
    def show_density(self):
        """Pokaż gęstość voxel"""
        # TODO: implementacja gęstości
        pass
        
    def set_projection(self, mode):
        """Ustaw projekcję"""
        if self.points_original is None:
            return
            
        pos = self.points_original.copy()
        if mode == 'XY':
            pos[:, 2] = 0
        elif mode == 'XZ':
            pos[:, 1] = 0
        elif mode == 'YZ':
            pos[:, 0] = 0
            
        self.points_pos = pos.tobytes()
        self.viz.set_data(self.points_pos, self.points_col, self.count)
        
    def toggle_animation(self):
        """Animacja sliding window"""
        # TODO: implementacja animacji
        pass

class DataLoaderThread(QThread):
    progress_update = pyqtSignal(int, int, str)
    data_loaded = pyqtSignal(object)
    
    def run(self):
        """Wczytaj cyfry π w tle - zoptymalizowane"""
        # ZMIEŃ TUTAJ: zmniejsz dla testów (100M zamiast 1B)
        total_digits = 100_000_000  # 100M dla szybkiego testu
        digits = np.zeros(total_digits, dtype=np.uint8)
        digit_idx = 0
        
        chunk_size = 100_000_000
        files_needed = 1  # tylko pierwszy plik dla testów
        pi_dir = Path("/home/baver/hexstrike-ai/OMNIS-PI-ENGINE/pi_10b_parts")
        read_chunk_size = 50_000_000  # większe chunki = szybsze
        
        for file_idx in range(1, files_needed + 1):
            start_pos = (file_idx - 1) * chunk_size + 1
            end_pos = file_idx * chunk_size
            filename = f"{start_pos}-{end_pos}.txt"
            filepath = pi_dir / filename
            
            self.progress_update.emit(file_idx, files_needed, f"Wczytywanie {filename}...")
            
            if filepath.exists():
                # Użyj numpy do szybkiej konwersji
                with open(filepath, 'rb') as f:
                    content = f.read(total_digits * 2)  # czytaj więcej, potem filtruj
                    
                # Konwertuj bytes na numpy array i filtruj cyfry
                content_arr = np.frombuffer(content, dtype=np.uint8)
                # Filtruj tylko cyfry (48-57)
                mask = (content_arr >= 48) & (content_arr <= 57)
                digits_found = content_arr[mask] - 48
                
                # Wstaw do głównej tablicy
                count_to_add = min(len(digits_found), total_digits - digit_idx)
                digits[digit_idx:digit_idx + count_to_add] = digits_found[:count_to_add]
                digit_idx += count_to_add
                            
            if digit_idx >= total_digits:
                break
        
        self.data_loaded.emit(digits[:digit_idx])

class DataProcessorThread(QThread):
    progress_update = pyqtSignal(int, int, str)
    points_ready = pyqtSignal(bytes, bytes, int)
    
    def __init__(self, digits):
        super().__init__()
        self.digits = digits
        
    def run(self):
        """Przetwórz cyfry na punkty w tle - zoptymalizowane"""
        count = len(self.digits) // 3
        max_points = 10_000_000
        sample_rate = max(1, count // max_points)
        sampled_count = min(count // sample_rate, max_points)
        
        self.progress_update.emit(0, 100, f"Tworzenie {sampled_count:,} punktów...")
        
        # Użyj vectorized operations numpy dla szybkości
        indices = np.arange(0, min(count, sampled_count * sample_rate), sample_rate) * 3
        valid = indices + 2 < len(self.digits)
        indices = indices[valid]
        
        if len(indices) == 0:
            self.points_ready.emit(np.array([], dtype=np.float32).tobytes(), 
                               np.array([], dtype=np.float32).tobytes(), 0)
            return
        
        # Wyciągnij x, y, z dla wszystkich punktów naraz
        idx_matrix = indices[:, None] + np.arange(3)
        xyz = self.digits[idx_matrix].astype(np.float32)
        
        # Kolory - uproszczone (szybsze)
        x, y, z = xyz[:, 0], xyz[:, 1], xyz[:, 2]
        
        # Prosty gradient RGB zamiast HSV (szybsze)
        r = x / 9.0
        g = y / 9.0
        b = z / 9.0
        
        col = np.stack([r, g, b], axis=1).astype(np.float32)
        
        self.points_ready.emit(xyz.tobytes(), col.tobytes(), len(xyz))

    def reset_view(self):
        """Reset do oryginalnych danych"""
        if self.points_original is not None:
            self.points_pos = self.points_original.tobytes()
            self.viz.set_data(self.points_pos, self.points_col, self.count)
            
    def show_density(self):
        """Pokaż gęstość voxel"""
        # TODO: implementacja gęstości
        pass
        
    def set_projection(self, mode):
        """Ustaw projekcję"""
        if self.points_original is None:
            return
            
        pos = self.points_original.copy()
        if mode == 'XY':
            pos[:, 2] = 0
        elif mode == 'XZ':
            pos[:, 1] = 0
        elif mode == 'YZ':
            pos[:, 0] = 0
            
        self.points_pos = pos.tobytes()
        self.viz.set_data(self.points_pos, self.points_col, self.count)
        
    def toggle_animation(self):
        """Animacja sliding window"""
        # TODO: implementacja animacji
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


