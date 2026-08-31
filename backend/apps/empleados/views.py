from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rol', 'estado']
    search_fields = ['usuario__first_name', 'usuario__last_name', 'numero_documento']
    ordering_fields = ['fecha_contratacion', 'usuario__first_name']
    ordering = ['-fecha_registro']