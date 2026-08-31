from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano', 'cliente', 'tipo', 'estado')
    list_filter = ('tipo', 'estado', 'marca', 'ano')
    search_fields = ('placa', 'vin', 'marca', 'modelo')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    fieldsets = (
        ('Información del Vehículo', {
            'fields': ('cliente', 'placa', 'vin', 'marca', 'modelo', 'ano', 'color', 'tipo')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Timestamps', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
