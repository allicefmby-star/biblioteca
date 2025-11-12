# biblioteca/circulacion/urls.py

from django.urls import path
from . import views
from .views import (
    circulacionView, 
    prestamos, 
    reserva, 
    multa,
    # --- ¡Importa las nuevas vistas de creación! ---
    PrestamoCreate,
    ReservaCreate,
    MultaCreate
)

urlpatterns = [
    # Vistas de Lista
    path('', circulacionView.as_view(), name='circulacion'),
    path('prestamos/', views.prestamos.as_view(), name='prestamos'),
    path('reservas/', views.reserva.as_view(), name='reservas'),
    path('multas/', views.multa.as_view(), name='multas'),

    # Vistas de Creación (Formularios)
    path('prestamos/nuevo/', PrestamoCreate.as_view(), name='prestamo_create'),
    path('reservas/nueva/', ReservaCreate.as_view(), name='reserva_create'),
    path('multas/nueva/', MultaCreate.as_view(), name='multa_create'),
]