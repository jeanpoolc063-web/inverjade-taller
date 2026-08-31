import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class InverjadeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('INVERJADE - Gestión de Taller de Latonería y Pintura')
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Header
        header = QLabel('INVERJADE - Sistema de Gestión')
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        header.setFont(font)
        layout.addWidget(header)
        
        # Botones de navegación
        button_layout = QHBoxLayout()
        buttons = [
            ('Dashboard', self.show_dashboard),
            ('Clientes', self.show_clientes),
            ('Vehículos', self.show_vehiculos),
            ('Órdenes', self.show_ordenes),
            ('Inventario', self.show_inventario),
        ]
        
        for text, callback in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(callback)
            button_layout.addWidget(btn)
        
        layout.addLayout(button_layout)
        
        # Área de contenido
        self.content_label = QLabel('Selecciona una opción del menú')
        layout.addWidget(self.content_label)
        
        central_widget.setLayout(layout)

    def show_dashboard(self):
        self.content_label.setText('Dashboard')

    def show_clientes(self):
        self.content_label.setText('Gestión de Clientes')

    def show_vehiculos(self):
        self.content_label.setText('Gestión de Vehículos')

    def show_ordenes(self):
        self.content_label.setText('Órdenes de Trabajo')

    def show_inventario(self):
        self.content_label.setText('Gestión de Inventario')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InverjadeApp()
    window.show()
    sys.exit(app.exec())
