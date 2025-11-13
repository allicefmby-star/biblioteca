# biblioteca/circulacion/urls.py

from django.urls import path
from . import views
from .views import (
    circulacionView, 
    prestamos, 
    reserva, 
    multa,
    
    # Vistas de Creación
    PrestamoCreate,
    ReservaCreate,
    MultaCreate,

    # ¡Importa las nuevas vistas Update y Delete!
    PrestamoUpdate, PrestamoDelete,
    ReservaUpdate, ReservaDelete,
    MultaUpdate, MultaDelete
)

urlpatterns = [
    # Vistas de Lista
    path('', circulacionView.as_view(), name='circulacion'),
    path('prestamos/', views.prestamos.as_view(), name='prestamos'),
    path('reservas/', views.reserva.as_view(), name='reservas'),
    path('multas/', views.multa.as_view(), name='multas'),

    # Vistas de Creación
    path('prestamos/nuevo/', PrestamoCreate.as_view(), name='prestamo_create'),
    path('reservas/nueva/', ReservaCreate.as_view(), name='reserva_create'),
    path('multas/nueva/', MultaCreate.as_view(), name='multa_create'),

    # VISTAS DE EDICIÓN (¡LO NUEVO!)
    path('prestamos/<int:pk>/editar/', PrestamoUpdate.as_view(), name='prestamo_update'),
    path('reservas/<int:pk>/editar/', ReservaUpdate.as_view(), name='reserva_update'),
    path('multas/<int:pk>/editar/', MultaUpdate.as_view(), name='multa_update'),

    # VISTAS DE BORRADO (¡LO NUEVO!)
    path('prestamos/<int:pk>/borrar/', PrestamoDelete.as_view(), name='prestamo_delete'),
    path('reservas/<int:pk>/borrar/', ReservaDelete.as_view(), name='reserva_delete'),
    path('multas/<int:pk>/borrar/', MultaDelete.as_view(), name='multa_delete'),
]