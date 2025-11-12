# biblioteca/catalogo/urls.py

from django.urls import path
from .views import (
    VistaCatalogo, 
    libro, categoria, editorial, Autor,
    AutorCreate, EditorialCreate, CategoriaCreate, LibroCreate # <-- ¡Importa las nuevas vistas!
)

urlpatterns = [
    # Vistas de Lista
    path('', VistaCatalogo.as_view(), name='catalogo'),
    path('libros/', libro.as_view(), name='libro'),
    path('categoria/', categoria.as_view(), name='categoria'),
    path('editoriales/', editorial.as_view(), name='editorial'),
    path('autores/', Autor.as_view(), name='Autor'), # Mantengo el name='Autor' que ya usabas
    
    # Vistas de Creación (¡LO NUEVO!)
    path('autores/nuevo/', AutorCreate.as_view(), name='autor_create'),
    path('editoriales/nueva/', EditorialCreate.as_view(), name='editorial_create'),
    path('categoria/nueva/', CategoriaCreate.as_view(), name='categoria_create'),
    path('libros/nuevo/', LibroCreate.as_view(), name='libro_create'),
]