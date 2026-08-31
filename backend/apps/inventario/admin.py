from django.contrib import admin
from .models import Inventario, MovimientoInventario

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'categoria', 'stock_actual', 'stock_minimo', 'precio_unitario', 'estado')
    list_filter = ('categoria', 'estado', 'fecha_registro')
    search_fields = ('codigo', 'descripcion', 'proveedor')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    fieldsets = (
        ('Información del Artículo', {
            'fields': ('codigo', 'descripcion', 'categoria', 'unidad_medida')
        }),
        ('Stock', {
            'fields': ('stock_actual', 'stock_minimo')
        }),
        ('Precios', {
            'fields': ('precio_unitario', 'precio_venta')
        }),
        ('Proveedor y Fechas', {
            'fields': ('proveedor', 'fecha_ingreso', 'fecha_vencimiento')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Timestamps', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'tipo', 'cantidad', 'stock_nuevo', 'fecha_movimiento', 'motivo')
    list_filter = ('tipo', 'fecha_movimiento')
    search_fields = ('articulo__codigo', 'motivo', 'referencia')
    readonly_fields = ('fecha_movimiento', 'stock_anterior', 'stock_nuevo')
    fieldsets = (
        ('Movimiento', {
            'fields': ('articulo', 'tipo', 'cantidad')
        }),
        ('Stock', {
            'fields': ('stock_anterior', 'stock_nuevo'),
            'classes': ('collapse',)
        }),
        ('Detalles', {
            'fields': ('motivo', 'referencia', 'observaciones')
        }),
        ('Timestamp', {
            'fields': ('fecha_movimiento',),
            'classes': ('collapse',)
        }),
    )
