from django.contrib import admin
from .models import FotoOrden

@admin.register(FotoOrden)
class FotoOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'tipo', 'fecha_captura')
    list_filter = ('tipo', 'fecha_captura')
    search_fields = ('orden__numero_orden', 'descripcion')
    readonly_fields = ('fecha_captura', 'imagen_preview')
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="200" height="auto" />'
        return 'Sin imagen'
    imagen_preview.allow_tags = True
    imagen_preview.short_description = 'Vista previa'
