# biblioteca/colecciones/views.py

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse # Usamos reverse en lugar de reverse_lazy
from .models import Categoria, Ubicacion, Etiqueta

# --- VISTAS DE LISTA (Las que ya tenías) ---

class VistaColecciones(TemplateView):
    template_name = 'colecciones/colecciones.html'

class VistaCategoria(ListView):
    model = Categoria
    template_name = 'colecciones/categoria.html'
    context_object_name = 'categorias'

class VistaEtiqueta(ListView):
    model = Etiqueta
    template_name = 'colecciones/etiqueta.html'
    context_object_name = 'etiquetas'

class VistaUbicacion(ListView):
    model = Ubicacion
    template_name = 'colecciones/ubicacion.html'
    context_object_name = 'ubicaciones'

# --- VISTAS DE CREACIÓN (¡LO NUEVO!) ---

class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'colecciones/categoria_form.html'
    # Solo pedimos el nombre, el 'slug' se autogenera
    fields = ['nombre'] 
    
    # Usamos get_success_url para evitar importaciones circulares
    def get_success_url(self):
        # Redirige a la URL llamada 'lista_categorias'
        return reverse('lista_categorias')

class EtiquetaCreate(CreateView):
    model = Etiqueta
    template_name = 'colecciones/etiqueta_form.html'
    fields = ['nombre']
    
    def get_success_url(self):
        return reverse('lista_etiquetas')

class UbicacionCreate(CreateView):
    model = Ubicacion
    template_name = 'colecciones/ubicacion_form.html'
    fields = ['sala', 'estante', 'nivel']
    
    def get_success_url(self):
        return reverse('lista_ubicaciones')