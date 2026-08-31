from django.db import models
from apps.ordenes.models import OrdenTrabajo

class FotoOrden(models.Model):
    TIPO_FOTO = [
        ('antes', 'Antes del trabajo'),
        ('durante', 'Durante el trabajo'),
        ('después', 'Después del trabajo'),
        ('otro', 'Otro'),
    ]
    
    orden = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='fotos')
    tipo = models.CharField(max_length=20, choices=TIPO_FOTO)
    imagen = models.ImageField(upload_to='ordenes/galeria/%Y/%m/%d/')
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_captura = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['fecha_captura']
        verbose_name = 'Foto de Orden'
        verbose_name_plural = 'Fotos de Órdenes'
    
    def __str__(self):
        return f"Foto {self.tipo} - Orden #{self.orden.numero_orden}"
