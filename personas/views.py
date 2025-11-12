# biblioteca/personas/views.py

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Empleado, Socio, Membresia # <-- ¡Importaciones aquí!

class personasView(TemplateView):
    template_name = 'personas.html'

# --- VISTAS DE LISTA (LISTVIEWS) ---

class empleados(ListView):
    model = Empleado
    template_name = 'empleados.html' # Este archivo debe estar en personas/templates/
    context_object_name = 'empleados'

class socios(ListView):
    model = Socio
    template_name = 'socios.html' # Este archivo debe estar en personas/templates/
    context_object_name = 'socios'

class membresias(ListView):
    model = Membresia
    # Corregido para apuntar a tu archivo en el subdirectorio 'personas/'
    template_name = 'personas/membresia_list.html' 
    context_object_name = 'membresias'

# --- VISTAS DE CREACIÓN (¡LO NUEVO!) ---

class EmpleadoCreate(CreateView):
    model = Empleado
    template_name = 'empleado_form.html' # Crearemos este archivo
    fields = ['nombre', 'email', 'rol']  # Campos del modelo Empleado
    success_url = reverse_lazy('empleados') # Redirige a la lista de empleados

class SocioCreate(CreateView):
    model = Socio
    template_name = 'socio_form.html' # Crearemos este archivo
    fields = ['nombre', 'email', 'telefono', 'activo'] # Campos del modelo Socio
    success_url = reverse_lazy('socios') # Redirige a la lista de socios

class MembresiaCreate(CreateView):
    model = Membresia
    template_name = 'membresia_form.html' # Crearemos este archivo
    fields = ['socio', 'tipo', 'inicio', 'fin'] # Campos del modelo Membresia
    success_url = reverse_lazy('membresias') # Redirige a la lista de membresías