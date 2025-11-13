# biblioteca/catalogo/views.py

# Importamos UpdateView y DeleteView
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# Usaremos 'reverse' para get_success_url
from django.urls import reverse_lazy, reverse 

# --- Modelos con Alias ---
from .models import Libro
from .models import Categoria
from .models import editorial as EditorialModel
from .models import Autor as AutorModel

# --- Vistas de Lista (ListView) ---

class VistaCatalogo(TemplateView):
    template_name = 'catalogo/catalogo.html'

class libro(ListView):
    model = Libro
    template_name = 'catalogo/libro.html'
    context_object_name = 'libros'

class categoria(ListView):
    model = Categoria
    template_name = 'catalogo/categoria.html'
    context_object_name = 'categorias'

class editorial(ListView):  
    model = EditorialModel
    template_name = 'catalogo/editorial.html'
    context_object_name = 'editoriales'

class Autor(ListView):
    model = AutorModel
    template_name = 'catalogo/Autor.html'
    context_object_name= 'autores'

# --- Vistas de Creación (CreateView) ---

class AutorCreate(CreateView):
    model = AutorModel
    template_name = 'catalogo/autor_form.html'
    fields = ['nombre', 'apellido', 'pais']
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
    fields = ['titulo', 'isbn', 'anio', 'editorial', 'autores', 'categorias']
    success_url = reverse_lazy('libro')

# --- VISTAS DE EDICIÓN (UPDATEVIEW) ¡LO NUEVO! ---

class AutorUpdate(UpdateView):
    model = AutorModel
    template_name = 'catalogo/autor_form.html' # Reutilizamos el formulario
    fields = ['nombre', 'apellido', 'pais']
    success_url = reverse_lazy('Autor') # Vuelve a la lista de autores

class EditorialUpdate(UpdateView):
    model = EditorialModel
    template_name = 'catalogo/editorial_form.html' # Reutilizamos el formulario
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('editorial')

class CategoriaUpdate(UpdateView):
    model = Categoria
    template_name = 'catalogo/categoria_form.html' # Reutilizamos el formulario
    fields = ['nombre']
    success_url = reverse_lazy('categoria')

class LibroUpdate(UpdateView):
    model = Libro
    template_name = 'catalogo/libro_form.html' # Reutilizamos el formulario
    fields = ['titulo', 'isbn', 'anio', 'editorial', 'autores', 'categorias']
    success_url = reverse_lazy('libro')

# --- VISTAS DE BORRADO (DELETEVIEW) ¡LO NUEVO! ---

class AutorDelete(DeleteView):
    model = AutorModel
    template_name = 'catalogo/autor_confirm_delete.html' # Plantilla de confirmación
    success_url = reverse_lazy('Autor') # Vuelve a la lista

class EditorialDelete(DeleteView):
    model = EditorialModel
    template_name = 'catalogo/editorial_confirm_delete.html'
    success_url = reverse_lazy('editorial')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'catalogo/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'catalogo/libro_confirm_delete.html'
    success_url = reverse_lazy('libro')