# Guía de Instalación - INVERJADE

## Requisitos Previos

- Python 3.9 o superior
- Node.js 16 o superior
- PostgreSQL 12 o superior
- Git
- pip (administrador de paquetes de Python)
- npm (administrador de paquetes de Node.js)

## Instalación por Componente

### 1. Backend (API REST - Django)

```bash
# Navega a la carpeta backend
cd backend

# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Crea las migraciones de base de datos
python manage.py makemigrations
python manage.py migrate

# Crea un superusuario (administrador)
python manage.py createsuperuser

# Inicia el servidor
python manage.py runserver
```

El API estará disponible en: http://localhost:8000

### 2. Frontend (Interfaz Web - React)

```bash
# Navega a la carpeta frontend
cd frontend

# Instala las dependencias
npm install

# Inicia el servidor de desarrollo
npm run dev
```

La interfaz web estará disponible en: http://localhost:5173

### 3. Aplicación Escritorio (PyQt6)

```bash
# Navega a la carpeta desktop
cd desktop

# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python src/main.py
```

## Configuración de Base de Datos

### PostgreSQL

```bash
# Accede a PostgreSQL
psql -U postgres

# Crea la base de datos
CREATE DATABASE inverjade;

# Crea un usuario
CREATE USER inverjade_user WITH PASSWORD 'tu_contraseña';

# Asigna permisos
ALTER ROLE inverjade_user SET client_encoding TO 'utf8';
ALTER ROLE inverjade_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE inverjade_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE inverjade TO inverjade_user;
```

### Variables de Entorno

Crea un archivo `.env` en la carpeta `backend`:

```env
DEBUG=True
SECRET_KEY=tu_clave_secreta_aqui

DB_NAME=inverjade
DB_USER=inverjade_user
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

## Verificación de Instalación

### Backend
```bash
cd backend
python manage.py check
```

### Frontend
```bash
cd frontend
npm run build
```

## Solución de Problemas

### Error de conexión a PostgreSQL
- Asegúrate de que PostgreSQL está ejecutándose
- Verifica las credenciales en el archivo `.env`
- Comprueba que la base de datos fue creada correctamente

### Error de puerto en uso
- Django: Ejecuta `python manage.py runserver 8001` para usar otro puerto
- React: Usa `npm run dev -- --port 5174`

### Módulos no encontrados en Python
- Asegúrate de haber activado el entorno virtual
- Reinstala las dependencias: `pip install -r requirements.txt`

## Acceso Inicial

- Admin: http://localhost:8000/admin (con credenciales de superusuario)
- Frontend: http://localhost:5173
- API: http://localhost:8000/api
