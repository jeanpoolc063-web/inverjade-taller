# 🚀 Guía de Desarrollo - INVERJADE

## Estado del Proyecto

✅ **Backend:** 80% completado
- Modelos de base de datos creados
- APIs REST funcionales
- Autenticación JWT implementada
- Sistema de reportes listo

⚙️ **Frontend:** 30% completado
- Estructura React configurada
- Componentes base creados
- Sistema de rutas establecido

⚙️ **Escritorio:** 20% completado
- Estructura básica de PyQt6
- Cliente API integrado

## Pasos para Iniciar Desarrollo

### 1. Configuración Base de Datos PostgreSQL

```bash
# Acceder a PostgreSQL
psql -U postgres

# Crear base de datos
CREATE DATABASE inverjade;

# Crear usuario
CREATE USER inverjade_user WITH PASSWORD 'inverjade123';

# Asignar permisos
ALTER ROLE inverjade_user SET client_encoding TO 'utf8';
ALTER ROLE inverjade_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE inverjade_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE inverjade TO inverjade_user;

# Salir
\q
```

### 2. Configurar Backend

```bash
# Navegar a backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
cp ../.env.example .env

# Editar .env con tus credenciales de BD
# NOTA: Cambiar contraseña en .env si es necesario

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
# Username: admin
# Email: admin@inverjade.local
# Password: (elige una contraseña segura)

# Iniciar servidor
python manage.py runserver
```

**El API estará en:** http://localhost:8000
**Admin panel:** http://localhost:8000/admin

### 3. Configurar Frontend

```bash
# Navegar a frontend
cd frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

**Frontend estará en:** http://localhost:5173

### 4. Configurar Aplicación Escritorio

```bash
# Navegar a desktop
cd desktop

# Crear entorno virtual
python -m venv venv

# Activar entorno
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python src/main.py
```

## Acceso Inicial

### Admin de Django
- URL: http://localhost:8000/admin
- Usuario: admin
- Contraseña: (la que configuraste)

### Crear datos de prueba

#### 1. Crear Cliente (vía Admin o API)
```bash
curl -X POST http://localhost:8000/api/clientes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Pérez",
    "tipo_documento": "CC",
    "numero_documento": "1234567890",
    "telefono": "3001234567",
    "email": "juan@example.com",
    "direccion": "Calle 123 #45",
    "ciudad": "Bogotá",
    "estado": "activo"
  }'
```

#### 2. Crear Vehículo
```bash
curl -X POST http://localhost:8000/api/vehiculos/ \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": 1,
    "placa": "ABC123",
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2020,
    "vin": "VIN123456789",
    "color": "Blanco",
    "tipo": "automovil",
    "estado": "activo"
  }'
```

#### 3. Crear Orden de Trabajo
```bash
curl -X POST http://localhost:8000/api/ordenes/ \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": 1,
    "vehiculo": 1,
    "descripcion": "Reparación de guardafango y pintura",
    "estado": "pendiente",
    "costo_estimado": 150000,
    "fecha_vencimiento": "2024-09-15"
  }'
```

## Estructura de Desarrollo

```
inverjade-taller/
├── backend/                    # Django API
│   ├── apps/                  # Aplicaciones Django
│   │   ├── clientes/
│   │   ├── vehiculos/
│   │   ├── ordenes/
│   │   ├── inventario/
│   │   ├── empleados/
│   │   └── reportes/
│   ├── config/                # Configuración de Django
│   ├── manage.py
│   └── requirements.txt
├── frontend/                  # React App
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
├── desktop/                   # PyQt6 App
│   ├── src/
│   │   ├── ui/
│   │   ├── controllers/
│   │   └── main.py
│   └── requirements.txt
└── docs/
```

## Endpoints Principales API

### Clientes
- `GET /api/clientes/` - Listar clientes
- `POST /api/clientes/` - Crear cliente
- `GET /api/clientes/{id}/` - Obtener cliente
- `PUT /api/clientes/{id}/` - Actualizar cliente
- `DELETE /api/clientes/{id}/` - Eliminar cliente

### Órdenes de Trabajo
- `GET /api/ordenes/` - Listar órdenes
- `POST /api/ordenes/` - Crear orden
- `POST /api/ordenes/{id}/cambiar_estado/` - Cambiar estado
- `GET /api/ordenes/pendientes/` - Órdenes pendientes
- `GET /api/ordenes/en_proceso/` - Órdenes en proceso

### Inventario
- `GET /api/inventario/` - Listar artículos
- `POST /api/inventario/` - Crear artículo
- `POST /api/inventario/{id}/registrar_movimiento/` - Registrar movimiento
- `GET /api/inventario/bajo_stock/` - Artículos bajo stock

### Reportes
- `GET /api/reportes/resumen/` - Resumen general
- `GET /api/reportes/ingresos-por-fecha/` - Ingresos por fecha
- `GET /api/reportes/ordenes-por-cliente/` - Órdenes por cliente
- `GET /api/reportes/estado-ordenes/` - Distribución por estado

## Próximas Tareas

- [ ] Completar interfaz web (React)
- [ ] Implementar autenticación en frontend
- [ ] Mejorar aplicación escritorio
- [ ] Agregar sistema de facturas
- [ ] Implementar notificaciones
- [ ] Agregar pruebas unitarias
- [ ] Documentar API con Swagger
- [ ] Configurar CI/CD

## Troubleshooting

### Error: "No se puede conectar a PostgreSQL"
- Asegurate que PostgreSQL está corriendo
- Verifica las credenciales en `.env`
- Confirma que la base de datos fue creada

### Error: "ModuleNotFoundError"
- Activa el entorno virtual
- Ejecuta `pip install -r requirements.txt`

### Error: Puerto en uso
- Django: `python manage.py runserver 8001`
- React: `npm run dev -- --port 5174`

## Contacto y Soporte

Para dudas o sugerencias, contacta al equipo de desarrollo.
