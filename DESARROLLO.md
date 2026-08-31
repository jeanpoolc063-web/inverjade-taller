# INVERJADE - Guía de Desarrollo Completa

## 📊 Estado del Proyecto (Actualizado)

✅ **Backend:** 90% completado
✅ **Frontend:** 70% completado  
⚙️ **Escritorio:** 20% completado

## 🚀 Inicio Rápido con Docker

### Opción 1: Linux/Mac
```bash
chmod +x start-dev.sh
./start-dev.sh
```

### Opción 2: Windows
```bash
start-dev.bat
```

### Opción 3: Manual
```bash
docker-compose build
docker-compose up -d
docker-compose exec backend python manage.py migrate
docker-compose exec -T backend python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@inverjade.local', 'admin123')"
```

## 🌐 Accesos después de Iniciar

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000/api
- **Admin Panel:** http://localhost:8000/admin
  - Usuario: `admin`
  - Contraseña: `admin123`

## 📁 Estructura del Repositorio

```
inverjade-taller/
├── backend/
│   ├── apps/
│   │   ├── clientes/       # Gestión de clientes
│   │   ├── vehiculos/      # Registro de vehículos
│   │   ├── ordenes/        # Órdenes de trabajo
│   │   ├── inventario/     # Control de inventario
│   │   ├── empleados/      # Gestión de empleados
│   │   └── reportes/       # Reportes y estadísticas
│   ├── config/             # Configuración Django
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/     # Componentes React
│   │   ├── pages/          # Páginas principales
│   │   ├── services/       # Servicios API
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── desktop/                # Aplicación PyQt6
├── docker-compose.yml
├── start-dev.sh
├── start-dev.bat
└── docs/
```

## 🔧 Funcionalidades Principales Implementadas

### Backend API
✅ CRUD completo para:
- Clientes
- Vehículos
- Órdenes de Trabajo
- Inventario (con movimientos)
- Empleados

✅ Sistema de Reportes:
- Resumen general
- Ingresos por fecha
- Órdenes por cliente
- Estado de órdenes

### Frontend Web
✅ Páginas completadas:
- Dashboard (con datos en tiempo real)
- Gestión de Clientes (CRUD)
- Gestión de Vehículos (CRUD)
- Órdenes de Trabajo (CRUD)
- Inventario (CRUD)

✅ Características:
- Interfaz responsive
- Carga de datos desde API
- Manejo de errores
- Formularios validados
- Estilos Tailwind CSS

## 📊 Endpoints API Disponibles

### Clientes
```
GET    /api/clientes/
POST   /api/clientes/
GET    /api/clientes/{id}/
PUT    /api/clientes/{id}/
DELETE /api/clientes/{id}/
POST   /api/clientes/{id}/cambiar_estado/
```

### Vehículos
```
GET    /api/vehiculos/
POST   /api/vehiculos/
GET    /api/vehiculos/{id}/
PUT    /api/vehiculos/{id}/
DELETE /api/vehiculos/{id}/
```

### Órdenes de Trabajo
```
GET    /api/ordenes/
POST   /api/ordenes/
GET    /api/ordenes/{id}/
PUT    /api/ordenes/{id}/
POST   /api/ordenes/{id}/cambiar_estado/
GET    /api/ordenes/pendientes/
GET    /api/ordenes/en_proceso/
```

### Inventario
```
GET    /api/inventario/
POST   /api/inventario/
GET    /api/inventario/{id}/
PUT    /api/inventario/{id}/
DELETE /api/inventario/{id}/
POST   /api/inventario/{id}/registrar_movimiento/
GET    /api/inventario/bajo_stock/
```

### Reportes
```
GET /api/reportes/resumen/
GET /api/reportes/ingresos-por-fecha/
GET /api/reportes/ordenes-por-cliente/
GET /api/reportes/estado-ordenes/
```

## 🧪 Crear Datos de Prueba

### 1. Acceder a Admin
- Ir a: http://localhost:8000/admin
- Ingresar: admin / admin123

### 2. Crear Cliente
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
    "ciudad": "Bogotá"
  }'
```

### 3. Crear Vehículo
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
    "tipo": "automovil"
  }'
```

### 4. Crear Orden
```bash
curl -X POST http://localhost:8000/api/ordenes/ \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": 1,
    "vehiculo": 1,
    "descripcion": "Reparación de guardafango y pintura",
    "costo_estimado": 150000,
    "estado": "pendiente"
  }'
```

## 🐛 Troubleshooting

### Puerto 8000 o 5173 en uso
```bash
# Cambiar puerto en docker-compose.yml y reiniciar
docker-compose down
docker-compose up -d
```

### Error de conexión a BD
```bash
# Reiniciar base de datos
docker-compose down -v
docker-compose up -d
docker-compose exec backend python manage.py migrate
```

### Limpiar todo y empezar de nuevo
```bash
docker-compose down -v
rm -rf backend/db.sqlite3
docker-compose up -d
```

## 📝 Próximas Tareas

- [ ] Autenticación JWT en frontend
- [ ] Sistema de usuarios y permisos
- [ ] Formularios de edición avanzados
- [ ] Gráficos de reportes (Chart.js)
- [ ] Exportación a PDF/Excel
- [ ] Sistema de notificaciones
- [ ] Aplicación Escritorio mejorada
- [ ] Pruebas unitarias
- [ ] Documentación Swagger API
- [ ] CI/CD con GitHub Actions

## 💡 Comandos Útiles

```bash
# Ver logs en tiempo real
docker-compose logs -f backend
docker-compose logs -f frontend

# Ejecutar comando en contenedor
docker-compose exec backend python manage.py shell

# Ver estado de servicios
docker-compose ps

# Detener servicios
docker-compose stop

# Reanudar servicios
docker-compose start

# Eliminar todo (base de datos incluida)
docker-compose down -v
```

## 📞 Soporte

Para reportar problemas o sugerencias, crea un issue en el repositorio.
