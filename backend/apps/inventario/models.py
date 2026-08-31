from django.db import models

class Inventario(models.Model):
    CATEGORIA_CHOICES = [
        ('pintura', 'Pintura'),
        ('solvente', 'Solvente'),
        ('herramienta', 'Herramienta'),
        ('material', 'Material'),
        ('repuesto', 'Repuesto'),
        ('otro', 'Otro'),
    ]
    
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=5)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    unidad_medida = models.CharField(max_length=20, default='unidad')
    proveedor = models.CharField(max_length=255, blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='activo', choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('descontinuado', 'Descontinuado'),
    ])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Artículo de Inventario'
        verbose_name_plural = 'Artículos de Inventario'
    
    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
    @property
    def debe_reabastecer(self):
        return self.stock_actual <= self.stock_minimo


class MovimientoInventario(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ]
    
    articulo = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    cantidad = models.IntegerField()
    motivo = models.CharField(max_length=255)
    referencia = models.CharField(max_length=100, blank=True)
    stock_anterior = models.IntegerField()
    stock_nuevo = models.IntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-fecha_movimiento']
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
    
    def __str__(self):
        return f"{self.tipo} - {self.articulo.codigo} ({self.cantidad} unidades)"