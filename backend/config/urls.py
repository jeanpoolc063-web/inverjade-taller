from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('clientes/', include('apps.clientes.urls')),
        path('vehiculos/', include('apps.vehiculos.urls')),
        path('ordenes/', include('apps.ordenes.urls')),
        path('inventario/', include('apps.inventario.urls')),
        path('empleados/', include('apps.empleados.urls')),
        path('reportes/', include('apps.reportes.urls')),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
