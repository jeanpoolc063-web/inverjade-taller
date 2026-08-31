from django.urls import path
from .views import ReportesViewSet

urlpatterns = [
    path('resumen/', ReportesViewSet.as_view({'get': 'resumen_general'}), name='resumen_general'),
    path('ingresos-por-fecha/', ReportesViewSet.as_view({'get': 'ingresos_por_fecha'}), name='ingresos_por_fecha'),
    path('ordenes-por-cliente/', ReportesViewSet.as_view({'get': 'ordenes_por_cliente'}), name='ordenes_por_cliente'),
    path('estado-ordenes/', ReportesViewSet.as_view({'get': 'estado_ordenes'}), name='estado_ordenes'),
]