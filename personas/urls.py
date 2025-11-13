# biblioteca/personas/urls.py

from django.urls import path
from . import views
from .views import (
    personasView, 
    empleados, 
    socios, 
    membresias,
    
    # Vistas de Creación
    EmpleadoCreate,
    SocioCreate,
    MembresiaCreate,

    # ¡Importa las nuevas vistas Update y Delete!
    EmpleadoUpdate, EmpleadoDelete,
    SocioUpdate, SocioDelete,
    MembresiaUpdate, MembresiaDelete
)

urlpatterns = [
    # Vistas de Lista
    path('', personasView.as_view(), name='personas'),
    path('empleados/', views.empleados.as_view(), name='empleados'),
    path('socios/', views.socios.as_view(), name='socios'),
    path('membresias/', views.membresias.as_view(), name='membresias'),

    # Vistas de Creación
    path('empleados/nuevo/', EmpleadoCreate.as_view(), name='empleado_create'),
    path('socios/nuevo/', SocioCreate.as_view(), name='socio_create'),
    path('membresias/nueva/', MembresiaCreate.as_view(), name='membresia_create'),

    # VISTAS DE EDICIÓN (¡LO NUEVO!)
    path('empleados/<int:pk>/editar/', EmpleadoUpdate.as_view(), name='empleado_update'),
    path('socios/<int:pk>/editar/', SocioUpdate.as_view(), name='socio_update'),
    path('membresias/<int:pk>/editar/', MembresiaUpdate.as_view(), name='membresia_update'),

    # VISTAS DE BORRADO (¡LO NUEVO!)
    path('empleados/<int:pk>/borrar/', EmpleadoDelete.as_view(), name='empleado_delete'),
    path('socios/<int:pk>/borrar/', SocioDelete.as_view(), name='socio_delete'),
    path('membresias/<int:pk>/borrar/', MembresiaDelete.as_view(), name='membresia_delete'),
]