# biblioteca/circulacion/views.py

from django.shortcuts import render
# Importamos UpdateView y DeleteView
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse 
from .models import Prestamo, Reserva, Multa

class circulacionView(TemplateView):
    template_name = 'circulacion.html'

# --- VISTAS DE LISTA (LISTVIEWS) ---

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

# --- VISTAS DE CREACIÓN (CREATEVIEW) ---

class PrestamoCreate(CreateView):
    model = Prestamo
    template_name = 'circulacion/prestamo_form.html'
    fields = ['ejemplar', 'socio', 'empleado_entrega', 'fecha_prestamo', 'fecha_vencimiento']
    
    def get_success_url(self):
        return reverse('prestamos')

class ReservaCreate(CreateView):
    model = Reserva
    template_name = 'circulacion/reserva_form.html'
    fields = ['libro', 'socio', 'estado']
    
    def get_success_url(self):
        return reverse('reservas')

class MultaCreate(CreateView):
    model = Multa
    template_name = 'circulacion/multa_form.html'
    fields = ['prestamo', 'monto', 'motivo', 'pagada']
    
    def get_success_url(self):
        return reverse('multas')

# --- VISTAS DE EDICIÓN (UPDATEVIEW) ¡LO NUEVO! ---

class PrestamoUpdate(UpdateView):
    model = Prestamo
    template_name = 'circulacion/prestamo_form.html' # Reutilizamos formulario
    # Permitimos editar la fecha de devolución
    fields = ['ejemplar', 'socio', 'empleado_entrega', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion']
    
    def get_success_url(self):
        return reverse('prestamos')

class ReservaUpdate(UpdateView):
    model = Reserva
    template_name = 'circulacion/reserva_form.html' # Reutilizamos formulario
    fields = ['libro', 'socio', 'estado'] # No dejamos editar 'creada_en'
    
    def get_success_url(self):
        return reverse('reservas')

class MultaUpdate(UpdateView):
    model = Multa
    template_name = 'circulacion/multa_form.html' # Reutilizamos formulario
    fields = ['prestamo', 'monto', 'motivo', 'pagada']
    
    def get_success_url(self):
        return reverse('multas')

# --- VISTAS DE BORRADO (DELETEVIEW) ¡LO NUEVO! ---

class PrestamoDelete(DeleteView):
    model = Prestamo
    template_name = 'circulacion/prestamo_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('prestamos')

class ReservaDelete(DeleteView):
    model = Reserva
    template_name = 'circulacion/reserva_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('reservas')

class MultaDelete(DeleteView):
    model = Multa
    template_name = 'circulacion/multa_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('multas')