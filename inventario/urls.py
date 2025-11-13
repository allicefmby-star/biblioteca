# biblioteca/inventario/urls.py

from django.urls import path
from . import views
from .views import (
    inventarioView, 
    ejemplares, 
    provedores,
    ingresos,
    
    # Vistas de Creación
    ProveedorCreate,
    IngresoInventarioCreate,
    EjemplarCreate,

    # ¡Importa las nuevas vistas Update y Delete!
    ProveedorUpdate, ProveedorDelete,
    IngresoInventarioUpdate, IngresoInventarioDelete,
    EjemplarUpdate, EjemplarDelete
)

urlpatterns = [
    # Vistas de Lista
    path('', inventarioView.as_view(), name='inventario'),
    path('ejemplares/', views.ejemplares.as_view(), name='ejemplares'),
    path('ingresos/', views.ingresos.as_view(), name='ingresos'),
    path('provedores/', views.provedores.as_view(), name='provedores'),

    # Vistas de Creación
    path('ejemplares/nuevo/', EjemplarCreate.as_view(), name='ejemplar_create'),
    path('provedores/nuevo/', ProveedorCreate.as_view(), name='proveedor_create'),
    path('ingresos/nuevo/', IngresoInventarioCreate.as_view(), name='ingreso_create'),

    # VISTAS DE EDICIÓN (¡LO NUEVO!)
    path('ejemplares/<int:pk>/editar/', EjemplarUpdate.as_view(), name='ejemplar_update'),
    path('provedores/<int:pk>/editar/', ProveedorUpdate.as_view(), name='proveedor_update'),
    path('ingresos/<int:pk>/editar/', IngresoInventarioUpdate.as_view(), name='ingreso_update'),

    # VISTAS DE BORRADO (¡LO NUEVO!)
    path('ejemplares/<int:pk>/borrar/', EjemplarDelete.as_view(), name='ejemplar_delete'),
    path('provedores/<int:pk>/borrar/', ProveedorDelete.as_view(), name='proveedor_delete'),
    path('ingresos/<int:pk>/borrar/', IngresoInventarioDelete.as_view(), name='ingreso_delete'),
]