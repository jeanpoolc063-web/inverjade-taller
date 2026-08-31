from rest_framework import serializers
from .models import OrdenTrabajo

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    vehiculo_info = serializers.CharField(source='vehiculo.__str__', read_only=True)
    empleado_nombre = serializers.CharField(source='empleado.usuario.get_full_name', read_only=True)
    
    class Meta:
        model = OrdenTrabajo
        fields = [
            'id', 'numero_orden', 'cliente', 'cliente_nombre', 'vehiculo',
            'vehiculo_info', 'empleado', 'empleado_nombre', 'descripcion',
            'estado', 'costo_estimado', 'costo_final', 'foto_antes', 'foto_después',
            'fecha_inicio', 'fecha_vencimiento', 'fecha_completacion', 'observaciones',
            'fecha_registro', 'fecha_actualizacion'
        ]
        read_only_fields = ['numero_orden', 'fecha_registro', 'fecha_actualizacion', 'fecha_inicio']
