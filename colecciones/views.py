# biblioteca/colecciones/views.py

# Importamos UpdateView y DeleteView
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Categoria, Ubicacion, Etiqueta

# --- VISTAS DE LISTA (ListView) ---

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

# --- VISTAS DE CREACIÓN (CreateView) ---

class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'colecciones/categoria_form.html'
    fields = ['nombre'] # El slug se genera solo
    
    def get_success_url(self):
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

# --- VISTAS DE EDICIÓN (UPDATEVIEW) ¡LO NUEVO! ---

class CategoriaUpdate(UpdateView):
    model = Categoria
    template_name = 'colecciones/categoria_form.html' # Reutilizamos formulario
    fields = ['nombre'] # El slug se autogenerará si cambia el nombre
    
    def get_success_url(self):
        return reverse('lista_categorias')

class EtiquetaUpdate(UpdateView):
    model = Etiqueta
    template_name = 'colecciones/etiqueta_form.html' # Reutilizamos formulario
    fields = ['nombre']
    
    def get_success_url(self):
        return reverse('lista_etiquetas')

class UbicacionUpdate(UpdateView):
    model = Ubicacion
    template_name = 'colecciones/ubicacion_form.html' # Reutilizamos formulario
    fields = ['sala', 'estante', 'nivel']
    
    def get_success_url(self):
        return reverse('lista_ubicaciones')

# --- VISTAS DE BORRADO (DELETEVIEW) ¡LO NUEVO! ---

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'colecciones/categoria_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('lista_categorias')

class EtiquetaDelete(DeleteView):
    model = Etiqueta
    template_name = 'colecciones/etiqueta_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('lista_etiquetas')

class UbicacionDelete(DeleteView):
    model = Ubicacion
    template_name = 'colecciones/ubicacion_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('lista_ubicaciones')