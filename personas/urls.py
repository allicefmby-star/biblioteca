# biblioteca/personas/urls.py

from django.urls import path
from . import views
from .views import (
    personasView, 
    empleados, 
    socios, 
    membresias,
    # --- ¡Importa las nuevas vistas! ---
    EmpleadoCreate,
    SocioCreate,
    MembresiaCreate
)

urlpatterns = [
    # Vistas de Lista (las que ya tenías)
    path('', personasView.as_view(), name='personas'),
    path('empleados/', views.empleados.as_view(), name='empleados'),
    path('socios/', views.socios.as_view(), name='socios'),
    path('membresias/', views.membresias.as_view(), name='membresias'),

    # Vistas de Creación (¡LO NUEVO!)
    path('empleados/nuevo/', EmpleadoCreate.as_view(), name='empleado_create'),
    path('socios/nuevo/', SocioCreate.as_view(), name='socio_create'),
    path('membresias/nueva/', MembresiaCreate.as_view(), name='membresia_create'),
]