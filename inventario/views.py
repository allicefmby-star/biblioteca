# biblioteca/inventario/views.py

from django.shortcuts import render
# Importamos UpdateView, DeleteView y reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Ejemplar, Proveedor, IngresoInventario

class inventarioView(TemplateView):
    template_name = 'inventario.html'

# --- VISTAS DE LISTA (LISTVIEWS) ---

class ejemplares(ListView):
    model = Ejemplar
    template_name = 'ejemplares.html'
    context_object_name = 'ejemplares'

class provedores(ListView):
    model = Proveedor
    template_name = 'provedores.html'
    context_object_name = 'proveedores' 

class ingresos(ListView):
    model = IngresoInventario
    template_name = 'inventario/ingresoinventario_list.html' 
    context_object_name = 'ingresos'

# --- VISTAS DE CREACIÓN (CORREGIDAS) ---

class ProveedorCreate(CreateView):
    model = Proveedor
    template_name = 'inventario/proveedor_form.html'
    fields = ['nombre', 'rfc', 'contacto']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('provedores')

class IngresoInventarioCreate(CreateView):
    model = IngresoInventario
    template_name = 'inventario/ingreso_form.html'
    fields = ['fecha', 'proveedor', 'nota']
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('ingresos')

class EjemplarCreate(CreateView):
    model = Ejemplar
    template_name = 'inventario/ejemplar_form.html'
    fields = ['libro', 'codigo_barras', 'estado', 'ubicacion', 'ingreso'] 
    
    # ▼▼▼ SOLUCIÓN: Usamos un método en lugar de 'success_url' ▼▼▼
    def get_success_url(self):
        return reverse('ejemplares')

# --- VISTAS DE EDICIÓN (UPDATEVIEW) ¡LO NUEVO! ---

class ProveedorUpdate(UpdateView):
    model = Proveedor
    template_name = 'inventario/proveedor_form.html' # Reutilizamos formulario
    fields = ['nombre', 'rfc', 'contacto']
    
    def get_success_url(self):
        return reverse('provedores')

class IngresoInventarioUpdate(UpdateView):
    model = IngresoInventario
    template_name = 'inventario/ingreso_form.html' # Reutilizamos formulario
    fields = ['fecha', 'proveedor', 'nota']
    
    def get_success_url(self):
        return reverse('ingresos')

class EjemplarUpdate(UpdateView):
    model = Ejemplar
    template_name = 'inventario/ejemplar_form.html' # Reutilizamos formulario
    fields = ['libro', 'codigo_barras', 'estado', 'ubicacion', 'ingreso'] 
    
    def get_success_url(self):
        return reverse('ejemplares')

# --- VISTAS DE BORRADO (DELETEVIEW) ¡LO NUEVO! ---

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'inventario/proveedor_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('provedores')

class IngresoInventarioDelete(DeleteView):
    model = IngresoInventario
    template_name = 'inventario/ingreso_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('ingresos')

class EjemplarDelete(DeleteView):
    model = Ejemplar
    template_name = 'inventario/ejemplar_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('ejemplares')