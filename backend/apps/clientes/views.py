from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['estado', 'ciudad']
    search_fields = ['nombre', 'numero_documento', 'telefono', 'email']
    ordering_fields = ['fecha_registro', 'nombre']
    ordering = ['-fecha_registro']
    
    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        cliente = self.get_object()
        nuevo_estado = request.data.get('estado')
        if nuevo_estado in ['activo', 'inactivo']:
            cliente.estado = nuevo_estado
            cliente.save()
            return Response({'estado': 'estado actualizado'})
        return Response({'error': 'estado inválido'}, status=status.HTTP_400_BAD_REQUEST)