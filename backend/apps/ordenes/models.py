from django.db import models
from apps.clientes.models import Cliente
from apps.vehiculos.models import Vehiculo
from apps.empleados.models import Empleado

class OrdenTrabajo(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('pausada', 'Pausada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    numero_orden = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordenes')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='ordenes')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordenes')
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    costo_estimado = models.DecimalField(max_digits=12, decimal_places=2)
    costo_final = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    foto_antes = models.ImageField(upload_to='ordenes/antes/%Y/%m/', null=True, blank=True, help_text='Foto del vehículo antes del trabajo')
    foto_después = models.ImageField(upload_to='ordenes/después/%Y/%m/', null=True, blank=True, help_text='Foto del vehículo después del trabajo')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_completacion = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Orden de Trabajo'
        verbose_name_plural = 'Órdenes de Trabajo'
    
    def __str__(self):
        return f"Orden #{self.numero_orden} - {self.cliente.nombre}"
    
    def save(self, *args, **kwargs):
        if not self.numero_orden:
            from django.utils import timezone
            year = timezone.now().year
            month = timezone.now().month
            count = OrdenTrabajo.objects.filter(fecha_registro__year=year, fecha_registro__month=month).count() + 1
            self.numero_orden = f"ORD-{year}{month:02d}-{count:04d}"
        super().save(*args, **kwargs)
