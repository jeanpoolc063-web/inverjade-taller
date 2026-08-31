from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FotoOrden
from .serializers import FotoOrdenSerializer

class FotoOrdenViewSet(viewsets.ModelViewSet):
    queryset = FotoOrden.objects.all()
    serializer_class = FotoOrdenSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    @action(detail=False, methods=['post'])
    def subir_foto(self, request):
        """Subir foto de una orden de trabajo"""
        orden_id = request.data.get('orden_id')
        tipo = request.data.get('tipo')
        imagen = request.FILES.get('imagen')
        descripcion = request.data.get('descripcion', '')
        
        if not orden_id or not tipo or not imagen:
            return Response(
                {'error': 'Faltan parámetros requeridos: orden_id, tipo, imagen'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        foto = FotoOrden.objects.create(
            orden_id=orden_id,
            tipo=tipo,
            imagen=imagen,
            descripcion=descripcion
        )
        
        return Response(FotoOrdenSerializer(foto).data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def por_orden(self, request):
        """Obtener todas las fotos de una orden"""
        orden_id = request.query_params.get('orden_id')
        if not orden_id:
            return Response({'error': 'Falta parámetro: orden_id'}, status=status.HTTP_400_BAD_REQUEST)
        
        fotos = self.queryset.filter(orden_id=orden_id)
        serializer = self.get_serializer(fotos, many=True)
        return Response(serializer.data)
