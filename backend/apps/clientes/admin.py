from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_documento', 'telefono', 'ciudad', 'estado', 'fecha_registro')
    list_filter = ('estado', 'ciudad', 'fecha_registro')
    search_fields = ('nombre', 'numero_documento', 'telefono', 'email')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'tipo_documento', 'numero_documento', 'email', 'telefono')
        }),
        ('Ubicación', {
            'fields': ('direccion', 'ciudad')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Timestamps', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
