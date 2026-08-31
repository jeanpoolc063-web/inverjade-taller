import os
from pathlib import Path

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = os.path.join(BASE_DIR, 'inverjade.db')

# Configuración de API
API_BASE_URL = 'http://localhost:8000/api'
API_TIMEOUT = 30

# Configuración de UI
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_TITLE = 'INVERJADE - Gestión de Taller de Latonería y Pintura'

# Base de datos local
DATABASE_CONFIG = {
    'driver': 'sqlite',
    'path': DATABASE_PATH,
}

# Temas
THEME = 'light'  # 'light' o 'dark'
