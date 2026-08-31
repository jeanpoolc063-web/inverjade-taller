from django.contrib import admin
from .models import OrdenTrabajo

@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ('numero_orden', 'cliente', 'estado', 'costo_estimado', 'fecha_inicio', 'empleado')
    list_filter = ('estado', 'fecha_inicio', 'empleado')
    search_fields = ('numero_orden', 'cliente__nombre', 'descripcion')
    readonly_fields = ('numero_orden', 'fecha_registro', 'fecha_actualizacion', 'fecha_inicio')
    fieldsets = (
        ('Información de Orden', {
            'fields': ('numero_orden', 'cliente', 'vehiculo', 'descripcion')
        }),
        ('Asignación', {
            'fields': ('empleado',)
        }),
        ('Costos', {
            'fields': ('costo_estimado', 'costo_final')
        }),
        ('Fechas', {
            'fields': ('fecha_vencimiento', 'fecha_completacion')
        }),
        ('Estado', {
            'fields': ('estado', 'observaciones')
        }),
        ('Timestamps', {
            'fields': ('fecha_inicio', 'fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
