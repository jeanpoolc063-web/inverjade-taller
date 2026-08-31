from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count, Q, F
from django.utils import timezone
from datetime import timedelta
from apps.ordenes.models import OrdenTrabajo
from apps.clientes.models import Cliente
from apps.inventario.models import Inventario

class ReportesViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def resumen_general(self, request):
        """Resumen general del taller"""
        hoy = timezone.now().date()
        
        # Conteos
        total_clientes = Cliente.objects.count()
        total_ordenes = OrdenTrabajo.objects.count()
        ordenes_pendientes = OrdenTrabajo.objects.filter(estado='pendiente').count()
        ordenes_en_proceso = OrdenTrabajo.objects.filter(estado='en_proceso').count()
        
        # Ingresos
        ordenes_completadas = OrdenTrabajo.objects.filter(estado='completada')
        ingresos_totales = ordenes_completadas.aggregate(Sum('costo_final'))['costo_final__sum'] or 0
        
        # Últimas 30 días
        fecha_hace_30 = hoy - timedelta(days=30)
        ingresos_30_dias = ordenes_completadas.filter(
            fecha_completacion__gte=fecha_hace_30
        ).aggregate(Sum('costo_final'))['costo_final__sum'] or 0
        
        # Inventario
        articulos_bajo_stock = Inventario.objects.filter(
            stock_actual__lte=F('stock_minimo')
        ).count()
        
        return Response({
            'total_clientes': total_clientes,
            'total_ordenes': total_ordenes,
            'ordenes_pendientes': ordenes_pendientes,
            'ordenes_en_proceso': ordenes_en_proceso,
            'ingresos_totales': float(ingresos_totales),
            'ingresos_30_dias': float(ingresos_30_dias),
            'articulos_bajo_stock': articulos_bajo_stock,
        })
    
    @action(detail=False, methods=['get'])
    def ingresos_por_fecha(self, request):
        """Ingresos agrupados por fecha"""
        ordenes = OrdenTrabajo.objects.filter(
            estado='completada'
        ).values('fecha_completacion__date').annotate(
            total=Sum('costo_final'),
            cantidad=Count('id')
        ).order_by('fecha_completacion__date')
        
        return Response(list(ordenes))
    
    @action(detail=False, methods=['get'])
    def ordenes_por_cliente(self, request):
        """Órdenes completadas por cliente"""
        clientes = Cliente.objects.annotate(
            total_ordenes=Count('ordenes', filter=Q(ordenes__estado='completada')),
            ingreso_total=Sum('ordenes__costo_final', filter=Q(ordenes__estado='completada'))
        ).filter(total_ordenes__gt=0).order_by('-ingreso_total')
        
        datos = []
        for cliente in clientes:
            datos.append({
                'id': cliente.id,
                'nombre': cliente.nombre,
                'total_ordenes': cliente.total_ordenes,
                'ingreso_total': float(cliente.ingreso_total or 0),
            })
        
        return Response(datos)
    
    @action(detail=False, methods=['get'])
    def estado_ordenes(self, request):
        """Distribución de órdenes por estado"""
        estados = OrdenTrabajo.objects.values('estado').annotate(
            cantidad=Count('id')
        ).order_by('-cantidad')
        
        return Response(list(estados))