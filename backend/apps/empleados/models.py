from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    ROL_CHOICES = [
        ('mecanico', 'Mecánico'),
        ('pintor', 'Pintor'),
        ('soldador', 'Soldador'),
        ('administrador', 'Administrador'),
        ('gerente', 'Gerente'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado')
    numero_documento = models.CharField(max_length=50, unique=True)
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='activo', choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('licencia', 'Licencia'),
    ])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.rol})"