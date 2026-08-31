# INVERJADE - Sistema de Gestión de Taller de Latonería y Pintura

## 📋 Descripción
Sistema integral de gestión para el taller de latonería y pintura **INVERJADE**. Aplicación híbrida con:
- **Web**: Acceso remoto desde cualquier navegador
- **Escritorio**: Aplicación independiente con funcionalidades offline

## 🎯 Funcionalidades Principales

### Gestión de Clientes
- Registro y perfil de clientes
- Historial de trabajos
- Datos de contacto y dirección

### Gestión de Vehículos
- Registro de vehículos por cliente
- Marcas, modelos, años
- Placa y número de identificación

### Órdenes de Trabajo
- Creación de órdenes de servicio
- Asignación a empleados
- Seguimiento de estado (pendiente, en proceso, completado)
- Descripción de trabajos a realizar

### Gestión de Inventario
- Control de materiales (pintura, solventes, etc.)
- Stock de piezas
- Alertas de bajo inventario
- Registro de entrada y salida

### Presupuestos y Facturación
- Generación de presupuestos
- Cálculo automático de costos
- Facturas y recibos
- Reportes de ingresos

### Gestión de Empleados
- Registro de empleados
- Asignación de tareas
- Control de productividad

### Reportes
- Reportes de trabajos realizados
- Análisis de ingresos
- Estadísticas de clientes
- Reportes de inventario

## 📁 Estructura del Proyecto

```
inverjade-taller/
├── backend/                 # API REST (Django)
│   ├── config/
│   ├── apps/
│   │   ├── clientes/
│   │   ├── vehiculos/
│   │   ├── ordenes/
│   │   ├── inventario/
│   │   ├── empleados/
│   │   └── reportes/
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/                # Aplicación Web (React)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
│
├── desktop/                 # Aplicación Escritorio (Python)
│   ├── src/
│   │   ├── ui/
│   │   ├── controllers/
│   │   ├── models/
│   │   └── main.py
│   ├── requirements.txt
│   └── build.py
│
├── database/                # Scripts de BD
│   ├── migrations/
│   └── schema.sql
│
├── docs/                    # Documentación
│   ├── API.md
│   ├── INSTALACION.md
│   └── GUIA_USUARIO.md
│
└── .gitignore
```

## 🚀 Inicio Rápido

### Requisitos
- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Git

### Instalación Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Instalación Frontend
```bash
cd frontend
npm install
npm run dev
```

### Instalación Escritorio
```bash
cd desktop
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## 🛠 Tecnologías Utilizadas

### Backend
- Django 4.x
- Django REST Framework
- PostgreSQL
- Celery (para tareas asincrónicas)

### Frontend
- React 18
- Vite
- Axios
- React Router
- Tailwind CSS

### Escritorio
- Python 3.9+
- PyQt6 o Tkinter
- SQLite/PostgreSQL

## 📊 Base de Datos
Utiliza PostgreSQL para sincronización entre aplicaciones web y escritorio.

## 🔐 Seguridad
- Autenticación JWT
- Control de permisos por roles
- Validación de datos
- Encriptación de contraseñas

## 📝 Licencia
MIT

## 👥 Autor
jeanpoolc063-web

## 📧 Contacto
Para más información sobre el proyecto, contacta al equipo de desarrollo.
