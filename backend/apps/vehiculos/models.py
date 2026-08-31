from django.db import models
from apps.clientes.models import Cliente

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    vin = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=50, blank=True)
    tipo = models.CharField(max_length=50, choices=[
        ('automovil', 'Automóvil'),
        ('camioneta', 'Camioneta'),
        ('moto', 'Moto'),
        ('camion', 'Camión'),
        ('otro', 'Otro'),
    ])
    foto = models.ImageField(upload_to='vehiculos/%Y/%m/', null=True, blank=True, help_text='Foto del vehículo')
    foto_daño = models.ImageField(upload_to='vehiculos/daños/%Y/%m/', null=True, blank=True, help_text='Foto del daño')
    estado = models.CharField(max_length=20, default='activo', choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"
