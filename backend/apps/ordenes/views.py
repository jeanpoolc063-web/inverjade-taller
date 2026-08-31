from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import OrdenTrabajo
from .serializers import OrdenTrabajoSerializer

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['estado', 'cliente', 'empleado']
    search_fields = ['numero_orden', 'cliente__nombre', 'descripcion']
    ordering_fields = ['fecha_inicio', 'fecha_vencimiento']
    ordering = ['-fecha_inicio']
    
    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        orden = self.get_object()
        nuevo_estado = request.data.get('estado')
        estados_validos = ['pendiente', 'en_proceso', 'pausada', 'completada', 'cancelada']
        
        if nuevo_estado in estados_validos:
            orden.estado = nuevo_estado
            if nuevo_estado == 'completada':
                orden.fecha_completacion = timezone.now()
                orden.costo_final = request.data.get('costo_final', orden.costo_estimado)
            orden.save()
            return Response({'estado': 'estado actualizado', 'nueva_orden': OrdenTrabajoSerializer(orden).data})
        return Response({'error': 'estado inválido'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def pendientes(self, request):
        ordenes = self.queryset.filter(estado='pendiente')
        serializer = self.get_serializer(ordenes, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def en_proceso(self, request):
        ordenes = self.queryset.filter(estado='en_proceso')
        serializer = self.get_serializer(ordenes, many=True)
        return Response(serializer.data)