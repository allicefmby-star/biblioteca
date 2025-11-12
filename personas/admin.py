from django.contrib import admin
from .models import Membresia, Empleado, Socio

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    # Tus campos 'apellido', 'puesto', 'fecha_contratacion' NO existen.
    # Los campos reales son: 'nombre', 'email', 'rol'.
    list_display = ('nombre', 'email', 'rol')
    list_filter = ('rol',)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    # Tus campos 'apellido', 'fecha_nacimiento', 'fecha_afiliacion' NO existen.
    # Los campos reales son: 'nombre', 'email', 'telefono', 'activo'.
    list_display = ('nombre', 'email', 'telefono', 'activo')
    list_filter = ('activo',)

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    # Tus campos 'duracion_meses' y 'precio' NO existen.
    # Los campos reales son: 'socio', 'tipo', 'inicio', 'fin'.
    list_display = ('socio', 'tipo', 'inicio', 'fin')
    list_filter = ('tipo',)