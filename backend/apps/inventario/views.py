from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Inventario, MovimientoInventario
from .serializers import InventarioSerializer, MovimientoInventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'estado']
    search_fields = ['codigo', 'descripcion', 'proveedor']
    ordering_fields = ['stock_actual', 'fecha_ingreso']
    ordering = ['-fecha_registro']
    
    @action(detail=True, methods=['post'])
    def registrar_movimiento(self, request, pk=None):
        articulo = self.get_object()
        tipo = request.data.get('tipo')
        cantidad = int(request.data.get('cantidad', 0))
        motivo = request.data.get('motivo', '')
        referencia = request.data.get('referencia', '')
        observaciones = request.data.get('observaciones', '')
        
        if tipo not in ['entrada', 'salida', 'ajuste']:
            return Response({'error': 'tipo de movimiento inválido'}, status=status.HTTP_400_BAD_REQUEST)
        
        stock_anterior = articulo.stock_actual
        
        if tipo == 'entrada':
            articulo.stock_actual += cantidad
        elif tipo == 'salida':
            if articulo.stock_actual < cantidad:
                return Response({'error': 'stock insuficiente'}, status=status.HTTP_400_BAD_REQUEST)
            articulo.stock_actual -= cantidad
        elif tipo == 'ajuste':
            articulo.stock_actual = cantidad
        
        articulo.save()
        
        movimiento = MovimientoInventario.objects.create(
            articulo=articulo,
            tipo=tipo,
            cantidad=cantidad,
            motivo=motivo,
            referencia=referencia,
            stock_anterior=stock_anterior,
            stock_nuevo=articulo.stock_actual,
            observaciones=observaciones
        )
        
        return Response(MovimientoInventarioSerializer(movimiento).data)
    
    @action(detail=False, methods=['get'])
    def bajo_stock(self, request):
        articulos = [art for art in self.queryset if art.debe_reabastecer]
        serializer = self.get_serializer(articulos, many=True)
        return Response(serializer.data)