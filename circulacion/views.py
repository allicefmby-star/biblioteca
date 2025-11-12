# biblioteca/circulacion/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# ¡Usamos 'reverse' porque lo llamaremos dentro de un método!
from django.urls import reverse 
from .models import Prestamo, Reserva, Multa

class circulacionView(TemplateView):
    template_name = 'circulacion.html'

# --- VISTAS DE LISTA (LISTVIEWS) ---
# (Corregidas para apuntar a las plantillas en el subdirectorio 'circulacion/')

class prestamos(ListView):
    model = Prestamo
    template_name = 'circulacion/prestamo_list.html' 
    context_object_name = 'prestamos'

class reserva(ListView):
    model = Reserva
    template_name = 'circulacion/reserva_list.html' 
    context_object_name = 'reservas'

class multa(ListView):
    model = Multa
    template_name = 'circulacion/multa_list.html' 
    context_object_name = 'multas'

# --- VISTAS DE CREACIÓN (¡LA SOLUCIÓN!) ---

class PrestamoCreate(CreateView):
    model = Prestamo
    template_name = 'circulacion/prestamo_form.html'
    fields = ['ejemplar', 'socio', 'empleado_entrega', 'fecha_prestamo', 'fecha_vencimiento']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('prestamos')

class ReservaCreate(CreateView):
    model = Reserva
    template_name = 'circulacion/reserva_form.html'
    fields = ['libro', 'socio', 'estado']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('reservas')

class MultaCreate(CreateView):
    model = Multa
    template_name = 'circulacion/multa_form.html'
    fields = ['prestamo', 'monto', 'motivo', 'pagada']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('multas')