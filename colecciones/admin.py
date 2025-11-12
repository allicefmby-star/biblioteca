# colecciones/admin.py

from django.contrib import admin
from .models import Categoria, Etiqueta, Ubicacion

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Esto te mostrará el nombre y el slug en la lista de categorías
    list_display = ('nombre', 'slug')
    
    # Esto autocompletará el campo 'slug' mientras escribes el 'nombre'
    # (¡Mucho mejor que el método save() para el admin!)
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    # Muestra los campos en la lista
    list_display = ('sala', 'estante', 'nivel')
    # Añade un filtro útil
    list_filter = ('sala',)

# Para Etiqueta, el registro simple está bien
admin.site.register(Etiqueta)