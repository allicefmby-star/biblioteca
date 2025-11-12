# biblioteca/catalogo/views.py

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy # ¡Importante para las redirecciones!

# --- Modelos con Alias ---
from .models import Libro
from .models import Categoria
from .models import editorial as EditorialModel
from .models import Autor as AutorModel

# --- Vistas de Lista (las que ya tenías) ---

class VistaCatalogo(TemplateView):
    template_name = 'catalogo/catalogo.html'

class libro(ListView):
    model = Libro
    template_name = 'catalogo/libro.html'
    context_object_name = 'libros'

class categoria(ListView):
    model = Categoria
    template_name = 'catalogo/categoria.html'
    context_object_name = 'categorias' # Nota: considera renombrar esto a 'categorias'

class editorial(ListView):  
    model = EditorialModel
    template_name = 'catalogo/editorial.html'
    context_object_name = 'editoriales'

class Autor(ListView):
    model = AutorModel
    template_name = 'catalogo/Autor.html'
    context_object_name= 'autores'

# --- Vistas de Creación (¡LO NUEVO!) ---

class AutorCreate(CreateView):
    model = AutorModel
    template_name = 'catalogo/autor_form.html' # Renombramos a _form.html
    fields = ['nombre', 'apellido', 'pais']
    # Redirige a la lista de autores cuando se crea uno nuevo
    success_url = reverse_lazy('Autor') 

class EditorialCreate(CreateView):
    model = EditorialModel
    template_name = 'catalogo/editorial_form.html'
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('editorial')

class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'catalogo/categoria_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('categoria')

class LibroCreate(CreateView):
    model = Libro
    template_name = 'catalogo/libro_form.html'
    # Django creará automáticamente los desplegables para editorial, autores y categorias
    fields = ['titulo', 'isbn', 'anio', 'editorial', 'autores', 'categorias']
    success_url = reverse_lazy('libro')

