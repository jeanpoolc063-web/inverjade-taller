from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Empleado

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']

class EmpleadoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Empleado
        fields = [
            'id', 'usuario', 'usuario_id', 'numero_documento', 'rol',
            'telefono', 'direccion', 'fecha_contratacion', 'salario',
            'estado', 'fecha_registro', 'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_registro', 'fecha_actualizacion']