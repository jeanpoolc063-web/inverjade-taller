from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id', 'nombre', 'tipo_documento', 'numero_documento',
            'telefono', 'email', 'direccion', 'ciudad', 'estado',
            'fecha_registro', 'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_registro', 'fecha_actualizacion']