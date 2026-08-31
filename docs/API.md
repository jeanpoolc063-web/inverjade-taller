# Documentación API - INVERJADE

## Autenticación

La API utiliza JWT (JSON Web Tokens) para autenticación.

### Obtener Token

```
POST /api/token/

{
  "username": "usuario",
  "password": "contraseña"
}

Respuesta:
{
  "access": "token_de_acceso",
  "refresh": "token_de_refresco"
}
```

## Endpoints Principales

### Clientes

#### Listar Clientes
```
GET /api/clientes/
```

#### Crear Cliente
```
POST /api/clientes/

{
  "nombre": "Juan Pérez",
  "telefono": "3001234567",
  "email": "juan@email.com",
  "direccion": "Calle 123 #45",
  "ciudad": "Bogotá"
}
```

#### Obtener Cliente
```
GET /api/clientes/{id}/
```

#### Actualizar Cliente
```
PUT /api/clientes/{id}/
```

#### Eliminar Cliente
```
DELETE /api/clientes/{id}/
```

### Vehículos

#### Listar Vehículos
```
GET /api/vehiculos/
```

#### Crear Vehículo
```
POST /api/vehiculos/

{
  "cliente_id": 1,
  "placa": "ABC123",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2020,
  "vin": "VIN123456789"
}
```

### Órdenes de Trabajo

#### Listar Órdenes
```
GET /api/ordenes/
```

#### Crear Orden
```
POST /api/ordenes/

{
  "cliente_id": 1,
  "vehiculo_id": 1,
  "descripcion": "Reparación de guardafango",
  "estado": "pendiente",
  "empleado_id": 1,
  "costo_estimado": 50000
}
```

#### Actualizar Estado de Orden
```
PATCH /api/ordenes/{id}/

{
  "estado": "completado",
  "costo_final": 50000
}
```

### Inventario

#### Listar Artículos
```
GET /api/inventario/
```

#### Crear Artículo
```
POST /api/inventario/

{
  "codigo": "PIN001",
  "descripcion": "Pintura roja metalizada",
  "categoria": "Pintura",
  "stock": 10,
  "precio_unitario": 15000,
  "proveedor": "Proveedor X"
}
```

#### Registrar Entrada/Salida
```
POST /api/inventario/{id}/movimiento/

{
  "tipo": "entrada",  // o "salida"
  "cantidad": 5,
  "motivo": "Compra a proveedor",
  "referencia": "Orden de compra #123"
}
```

## Códigos de Respuesta

- `200 OK`: Solicitud exitosa
- `201 Created`: Recurso creado exitosamente
- `400 Bad Request`: Datos inválidos
- `401 Unauthorized`: No autenticado
- `403 Forbidden`: No autorizado
- `404 Not Found`: Recurso no encontrado
- `500 Internal Server Error`: Error del servidor

## Filtrado y Búsqueda

### Ejemplo de filtrado
```
GET /api/clientes/?ciudad=Bogotá
GET /api/ordenes/?estado=pendiente
GET /api/inventario/?categoria=Pintura
```

### Búsqueda
```
GET /api/clientes/?search=Juan
```

## Paginación

Las listas están paginadas con 20 elementos por página.

```
GET /api/clientes/?page=2
```
