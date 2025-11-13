# biblioteca/personas/views.py

# Importamos UpdateView y DeleteView
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# ¡Importamos reverse!
from django.urls import reverse
from .models import Empleado, Socio, Membresia

class personasView(TemplateView):
    template_name = 'personas.html'

# --- VISTAS DE LISTA (LISTVIEWS) ---

class empleados(ListView):
    model = Empleado
    template_name = 'empleados.html'
    context_object_name = 'empleados'

class socios(ListView):
    model = Socio
    template_name = 'socios.html'
    context_object_name = 'socios'

class membresias(ListView):
    model = Membresia
    template_name = 'personas/membresia_list.html' 
    context_object_name = 'membresias'

# --- VISTAS DE CREACIÓN (CORREGIDAS) ---

class EmpleadoCreate(CreateView):
    model = Empleado
    template_name = 'empleado_form.html'
    fields = ['nombre', 'email', 'rol']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('empleados')

class SocioCreate(CreateView):
    model = Socio
    template_name = 'socio_form.html'
    fields = ['nombre', 'email', 'telefono', 'activo']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('socios')

class MembresiaCreate(CreateView):
    model = Membresia
    template_name = 'membresia_form.html'
    fields = ['socio', 'tipo', 'inicio', 'fin']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('membresias')

# --- VISTAS DE EDICIÓN (UPDATEVIEW) ¡LO NUEVO! ---

class EmpleadoUpdate(UpdateView):
    model = Empleado
    template_name = 'empleado_form.html' # Reutilizamos formulario
    fields = ['nombre', 'email', 'rol']
    
    def get_success_url(self):
        return reverse('empleados')

class SocioUpdate(UpdateView):
    model = Socio
    template_name = 'socio_form.html' # Reutilizamos formulario
    fields = ['nombre', 'email', 'telefono', 'activo']
    
    def get_success_url(self):
        return reverse('socios')

class MembresiaUpdate(UpdateView):
    model = Membresia
    template_name = 'membresia_form.html' # Reutilizamos formulario
    fields = ['socio', 'tipo', 'inicio', 'fin']
    
    def get_success_url(self):
        return reverse('membresias')

# --- VISTAS DE BORRADO (DELETEVIEW) ¡LO NUEVO! ---

class EmpleadoDelete(DeleteView):
    model = Empleado
    template_name = 'personas/empleado_confirm_delete.html' # Plantilla de confirmación
    
    def get_success_url(self):
        return reverse('empleados')

class SocioDelete(DeleteView):
    model = Socio
    template_name = 'personas/socio_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('socios')

class MembresiaDelete(DeleteView):
    model = Membresia
    template_name = 'personas/membresia_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('membresias')