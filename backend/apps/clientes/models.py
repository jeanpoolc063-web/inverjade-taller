from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('NIT', 'NIT'),
        ('OTRO', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO, default='CC')
    numero_documento = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, default='activo', choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.nombre} ({self.numero_documento})"