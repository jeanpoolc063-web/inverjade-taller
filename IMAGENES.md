# Funcionalidad de Imágenes en INVERJADE

## 📸 ¿CÓMO FUNCIONA?

### 1. Carga de Imágenes en Órdenes

Ahora puedes:
- **Subir foto ANTES del trabajo**
- **Subir foto DURANTE el trabajo**
- **Subir foto DESPUÉS del trabajo**
- **Agregar descripciones** a cada foto

### 2. Ubicaciones de Imágenes

Las imágenes se guardan organizadas en:
```
media/
├── clientes/
│   └── YYYY/MM/ (fotos de clientes)
├── vehiculos/
│   ├── YYYY/MM/ (fotos de vehículos)
│   └── daños/YYYY/MM/ (fotos de daños)
└── ordenes/
    ├── antes/YYYY/MM/ (fotos antes)
    ├── durante/YYYY/MM/ (fotos durante)
    ├── después/YYYY/MM/ (fotos después)
    └── galeria/YYYY/MM/DD/ (galería general)
```

### 3. APIs de Carga de Imágenes

#### Subir Foto de Orden
```bash
POST /api/ordenes/fotos/subir_foto/

Content-Type: multipart/form-data

{
  "orden_id": 1,
  "tipo": "después",
  "imagen": [archivo binario],
  "descripcion": "Trabajo completado exitosamente"
}
```

#### Obtener Fotos de una Orden
```bash
GET /api/ordenes/fotos/por_orden/?orden_id=1
```

#### Listar Todas las Fotos
```bash
GET /api/ordenes/fotos/
```

### 4. Campos de Imágenes en Modelos

**Cliente:**
- `foto` - Foto del cliente

**Vehículo:**
- `foto` - Foto general del vehículo
- `foto_daño` - Foto del daño o problema

**Orden de Trabajo:**
- `foto_antes` - Foto antes del trabajo
- `foto_después` - Foto después del trabajo

**Foto de Orden (modelo nuevo):**
- Tipos: antes, durante, después, otro
- Galería completa de fotos

## 🖼️ CÓMO USAR EN LA INTERFAZ

### En el Frontend:

1. Ve a **Órdenes**
2. Haz clic en **Galería** en cualquier orden
3. Se abre una ventana con:
   - Formulario para subir fotos
   - Galería de fotos guardadas
   - Fotos organizadas por tipo

### En el Admin Panel:

1. Ve a http://localhost:8000/admin
2. Entra a **Fotos de Órdenes**
3. Verás vista previa de las imágenes
4. Puedes filtrar por tipo y orden

## 📝 EJEMPLOS DE USO

### 1. Subir Foto con cURL

```bash
curl -X POST http://localhost:8000/api/ordenes/fotos/subir_foto/ \
  -F "orden_id=1" \
  -F "tipo=después" \
  -F "imagen=@/ruta/a/foto.jpg" \
  -F "descripcion=Trabajo completado"
```

### 2. Subir Foto con Python

```python
import requests

with open('foto.jpg', 'rb') as f:
    files = {'imagen': f}
    data = {
        'orden_id': 1,
        'tipo': 'después',
        'descripcion': 'Trabajo completado'
    }
    response = requests.post(
        'http://localhost:8000/api/ordenes/fotos/subir_foto/',
        files=files,
        data=data
    )
    print(response.json())
```

### 3. Obtener Fotos con JavaScript

```javascript
fetch('/api/ordenes/fotos/por_orden/?orden_id=1')
  .then(response => response.json())
  .then(data => {
    data.forEach(foto => {
      console.log(`${foto.tipo}: ${foto.imagen}`);
    });
  });
```

## ⚙️ CONFIGURACIÓN

### En settings.py (ya configurado):

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### En docker-compose.yml:

Las imágenes se guardan en un volumen llamado `media_data`

## 🔒 CONSIDERACIONES DE SEGURIDAD

- ✅ Solo se aceptan archivos de imagen (MIME types validados por Pillow)
- ✅ Las imágenes se guardan fuera de la raíz del servidor
- ✅ URLs de medios requieren acceso autenticado en producción
- ✅ Límite de tamaño recomendado: 5MB por imagen

## 📊 PRÓXIMOS PASOS

- [ ] Agregar compresión automática de imágenes
- [ ] Implementar galería con zoom
- [ ] Agregar anotaciones a fotos
- [ ] Exportar reportes con imágenes
- [ ] Sincronización de imágenes en app escritorio
- [ ] Almacenamiento en cloud (AWS S3, etc.)

## 🐛 TROUBLESHOOTING

### Error: "Permission denied" al crear carpeta media
```bash
# Verificar permisos
ls -la media/

# Si es necesario, cambiar permisos
chmod -R 755 media/
```

### Las imágenes no se muestran
```bash
# Verificar que Django sirva archivos estáticos en desarrollo
# (ya configurado en settings.py)

# En producción, configurar servidor web (Nginx, Apache)
```

### Imágenes no se guardan después de docker-compose
```bash
# Asegurar que el volumen persiste
docker-compose down  # SIN -v
docker-compose up -d
```

---

¡Ahora tu INVERJADE tiene capacidad completa de gestión de imágenes! 📸
