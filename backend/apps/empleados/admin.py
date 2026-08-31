from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'numero_documento', 'telefono', 'estado', 'fecha_contratacion')
    list_filter = ('rol', 'estado', 'fecha_contratacion')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'numero_documento')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    fieldsets = (
        ('Usuario', {
            'fields': ('usuario',)
        }),
        ('Información Personal', {
            'fields': ('numero_documento', 'rol', 'telefono', 'direccion')
        }),
        ('Contratación', {
            'fields': ('fecha_contratacion', 'salario')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Timestamps', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
