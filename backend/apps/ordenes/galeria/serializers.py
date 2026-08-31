from rest_framework import serializers
from .models import FotoOrden

class FotoOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoOrden
        fields = ['id', 'orden', 'tipo', 'imagen', 'descripcion', 'fecha_captura']
        read_only_fields = ['fecha_captura']
