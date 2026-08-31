from rest_framework import serializers
from .models import Inventario, MovimientoInventario

class MovimientoInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInventario
        fields = [
            'id', 'articulo', 'tipo', 'cantidad', 'motivo', 'referencia',
            'stock_anterior', 'stock_nuevo', 'fecha_movimiento', 'observaciones'
        ]
        read_only_fields = ['fecha_movimiento']

class InventarioSerializer(serializers.ModelSerializer):
    debe_reabastecer = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Inventario
        fields = [
            'id', 'codigo', 'descripcion', 'categoria', 'stock_actual',
            'stock_minimo', 'precio_unitario', 'precio_venta', 'unidad_medida',
            'proveedor', 'fecha_ingreso', 'fecha_vencimiento', 'estado',
            'debe_reabastecer', 'fecha_registro', 'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_registro', 'fecha_actualizacion']