from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehiculo
from .serializers import VehiculoSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cliente', 'tipo', 'estado']
    search_fields = ['placa', 'marca', 'modelo', 'vin']
    ordering_fields = ['fecha_registro', 'marca']
    ordering = ['-fecha_registro']