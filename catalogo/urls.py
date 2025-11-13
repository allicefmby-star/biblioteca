# biblioteca/catalogo/urls.py

from django.urls import path
from .views import (
    VistaCatalogo, 
    libro, categoria, editorial, Autor,
    
    # Vistas de Creación
    AutorCreate, EditorialCreate, CategoriaCreate, LibroCreate,
    
    # ¡Importa las nuevas vistas Update y Delete!
    AutorUpdate, AutorDelete,
    EditorialUpdate, EditorialDelete,
    CategoriaUpdate, CategoriaDelete,
    LibroUpdate, LibroDelete
)

urlpatterns = [
    # Vistas de Lista
    path('', VistaCatalogo.as_view(), name='catalogo'),
    path('libros/', libro.as_view(), name='libro'),
    path('categoria/', categoria.as_view(), name='categoria'),
    path('editoriales/', editorial.as_view(), name='editorial'),
    path('autores/', Autor.as_view(), name='Autor'),
    
    # Vistas de Creación
    path('autores/nuevo/', AutorCreate.as_view(), name='autor_create'),
    path('editoriales/nueva/', EditorialCreate.as_view(), name='editorial_create'),
    path('categoria/nueva/', CategoriaCreate.as_view(), name='categoria_create'),
    path('libros/nuevo/', LibroCreate.as_view(), name='libro_create'),

    # VISTAS DE EDICIÓN (¡LO NUEVO!)
    # Ej: /catalogo/autores/1/editar/
    path('autores/<int:pk>/editar/', AutorUpdate.as_view(), name='autor_update'),
    path('editoriales/<int:pk>/editar/', EditorialUpdate.as_view(), name='editorial_update'),
    path('categoria/<int:pk>/editar/', CategoriaUpdate.as_view(), name='categoria_update'),
    path('libros/<int:pk>/editar/', LibroUpdate.as_view(), name='libro_update'),

    # VISTAS DE BORRADO (¡LO NUEVO!)
    # Ej: /catalogo/autores/1/borrar/
    path('autores/<int:pk>/borrar/', AutorDelete.as_view(), name='autor_delete'),
    path('editoriales/<int:pk>/borrar/', EditorialDelete.as_view(), name='editorial_delete'),
    path('categoria/<int:pk>/borrar/', CategoriaDelete.as_view(), name='categoria_delete'),
    path('libros/<int:pk>/borrar/', LibroDelete.as_view(), name='libro_delete'),
]