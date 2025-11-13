# biblioteca/colecciones/urls.py

from django.urls import path
from . import views
from .views import (
    VistaColecciones,
    VistaCategoria,
    VistaEtiqueta,
    VistaUbicacion,
    
    # Vistas de Creación
    CategoriaCreate,
    EtiquetaCreate,
    UbicacionCreate,

    # ¡Importa las nuevas vistas Update y Delete!
    CategoriaUpdate, CategoriaDelete,
    EtiquetaUpdate, EtiquetaDelete,
    UbicacionUpdate, UbicacionDelete
)

urlpatterns = [
    # Vistas de Lista
    path('', views.VistaColecciones.as_view(), name='colecciones'),
    path('categorias/', views.VistaCategoria.as_view(), name='lista_categorias'),
    path('etiquetas/', views.VistaEtiqueta.as_view(), name='lista_etiquetas'),
    path('ubicaciones/', views.VistaUbicacion.as_view(), name='lista_ubicaciones'),

    # Vistas de Creación
    path('categorias/nueva/', CategoriaCreate.as_view(), name='categoria_create'),
    path('etiquetas/nueva/', EtiquetaCreate.as_view(), name='etiqueta_create'),
    path('ubicaciones/nueva/', UbicacionCreate.as_view(), name='ubicacion_create'),

    # VISTAS DE EDICIÓN (¡LO NUEVO!)
    path('categorias/<int:pk>/editar/', CategoriaUpdate.as_view(), name='categoria_update'),
    path('etiquetas/<int:pk>/editar/', EtiquetaUpdate.as_view(), name='etiqueta_update'),
    path('ubicaciones/<int:pk>/editar/', UbicacionUpdate.as_view(), name='ubicacion_update'),

    # VISTAS DE BORRADO (¡LO NUEVO!)
    path('categorias/<int:pk>/borrar/', CategoriaDelete.as_view(), name='categoria_delete'),
    path('etiquetas/<int:pk>/borrar/', EtiquetaDelete.as_view(), name='etiqueta_delete'),
    path('ubicaciones/<int:pk>/borrar/', UbicacionDelete.as_view(), name='ubicacion_delete'),
]