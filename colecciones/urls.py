# biblioteca/colecciones/urls.py

from django.urls import path
from . import views
from .views import (
    VistaColecciones,
    VistaCategoria,
    VistaEtiqueta,
    VistaUbicacion,
    # --- ¡Importa las nuevas vistas! ---
    CategoriaCreate,
    EtiquetaCreate,
    UbicacionCreate
)

urlpatterns = [
    # Vistas de Lista (las que ya tenías)
    path('', views.VistaColecciones.as_view(), name='colecciones'),
    path('categorias/', views.VistaCategoria.as_view(), name='lista_categorias'),
    path('etiquetas/', views.VistaEtiqueta.as_view(), name='lista_etiquetas'),
    path('ubicaciones/', views.VistaUbicacion.as_view(), name='lista_ubicaciones'),

    # Vistas de Creación (¡LO NUEVO!)
    path('categorias/nueva/', CategoriaCreate.as_view(), name='categoria_create'),
    path('etiquetas/nueva/', EtiquetaCreate.as_view(), name='etiqueta_create'),
    path('ubicaciones/nueva/', UbicacionCreate.as_view(), name='ubicacion_create'),
]