from django.contrib import admin
from .models import Prestamo, Reserva, Multa

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Prestamo.
    """
    # Campos para mostrar en la vista de lista
    list_display = (
        'id', 
        'socio', 
        'ejemplar', 
        'fecha_prestamo', 
        'fecha_vencimiento', 
        'fecha_devolucion'
    )
    
    # Filtros que aparecerán en la barra lateral
    list_filter = (
        'fecha_prestamo', 
        'fecha_vencimiento', 
        'fecha_devolucion'
    )
    
    # Campos por los que se puede buscar
    # (Buscamos en el 'nombre' del 'socio' y el 'codigo_barras' del 'ejemplar')
    search_fields = (
        'socio__nombre', 
        'ejemplar__codigo_barras' 
    )


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Reserva.
    """
    # Campos para mostrar en la vista de lista
    list_display = (
        'id', 
        'socio', 
        'libro', 
        'estado', 
        'creada_en'
    )
    
    # 'estado' es un filtro perfecto
    list_filter = ('estado',)
    
    # Campos de búsqueda
    # (Buscamos en el 'nombre' del 'socio' y el 'titulo' del 'libro')
    search_fields = (
        'socio__nombre', 
        'libro__titulo'
    )


@admin.register(Multa)
class MultaAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Multa.
    """
    # Campos para mostrar en la vista de lista
    list_display = (
        'id', 
        'prestamo', 
        'monto', 
        'pagada', 
        'motivo'
    )
    
    # 'pagada' (un booleano) es un filtro excelente
    list_filter = ('pagada',)
    
    # Campos de búsqueda
    # (Buscamos la multa a través del nombre del socio en el préstamo)
    search_fields = ('prestamo__socio__nombre',)