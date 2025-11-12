from django.contrib import admin
from .models import Proveedor, IngresoInventario, Ejemplar

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rfc', 'contacto')

@admin.register(IngresoInventario)
class IngresoInventarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'proveedor', 'nota')
    list_filter = ('fecha', 'proveedor')

@admin.register(Ejemplar)
class EjemplarAdmin(admin.ModelAdmin):  
    list_display = ('libro', 'codigo_barras', 'estado', 'ubicacion', 'ingreso')
    list_filter = ('estado', 'ubicacion')
   
