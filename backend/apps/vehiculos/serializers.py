from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    
    class Meta:
        model = Vehiculo
        fields = [
            'id', 'cliente', 'cliente_nombre', 'placa', 'marca',
            'modelo', 'ano', 'vin', 'color', 'tipo', 'foto', 'foto_daño',
            'estado', 'fecha_registro', 'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_registro', 'fecha_actualizacion']
