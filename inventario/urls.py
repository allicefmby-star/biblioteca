# biblioteca/inventario/urls.py

from django.urls import path
from . import views
from .views import (
    inventarioView, 
    ejemplares, 
    provedores,  # El nombre de tu vista es 'provedores'
    ingresos,
    # --- ¡Importa las nuevas vistas! ---
    ProveedorCreate,
    IngresoInventarioCreate,
    EjemplarCreate
)

urlpatterns = [
    # Vistas de Lista
    path('', inventarioView.as_view(), name='inventario'),
    path('ejemplares/', views.ejemplares.as_view(), name='ejemplares'),
    path('ingresos/', views.ingresos.as_view(), name='ingresos'),
    path('provedores/', views.provedores.as_view(), name='provedores'), # Ruta para la vista 'provedores'

    # Vistas de Creación (¡LO NUEVO!)
    path('ejemplares/nuevo/', EjemplarCreate.as_view(), name='ejemplar_create'),
    path('provedores/nuevo/', ProveedorCreate.as_view(), name='proveedor_create'),
    path('ingresos/nuevo/', IngresoInventarioCreate.as_view(), name='ingreso_create'),
]