# biblioteca/inventario/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Ejemplar, Proveedor, IngresoInventario

class inventarioView(TemplateView):
    template_name = 'inventario.html'

# --- VISTAS DE LISTA (LISTVIEWS) ---

class ejemplares(ListView):
    model = Ejemplar
    template_name = 'ejemplares.html' # Plantilla: inventario/templates/ejemplares.html
    context_object_name = 'ejemplares'

class provedores(ListView): # Nota: el nombre de la clase es 'provedores'
    model = Proveedor
    template_name = 'provedores.html' # Plantilla: inventario/templates/provedores.html
    context_object_name = 'proveedores' 

class ingresos(ListView):
    model = IngresoInventario
    # ¡CORREGIDO! Apunta al archivo correcto que subiste
    template_name = 'inventario/ingresoinventario_list.html' 
    context_object_name = 'ingresos'

# --- VISTAS DE CREACIÓN (¡LO NUEVO!) ---

class ProveedorCreate(CreateView):
    model = Proveedor
    template_name = 'inventario/proveedor_form.html' # Crearemos este archivo
    fields = ['nombre', 'rfc', 'contacto'] # Campos del modelo Proveedor
    success_url = reverse_lazy('provedores') # Redirige a la lista de proveedores

class IngresoInventarioCreate(CreateView):
    model = IngresoInventario
    template_name = 'inventario/ingreso_form.html' # Crearemos este archivo
    fields = ['fecha', 'proveedor', 'nota'] # Campos del modelo IngresoInventario
    success_url = reverse_lazy('ingresos') # Redirige a la lista de ingresos

class EjemplarCreate(CreateView):
    model = Ejemplar
    template_name = 'inventario/ejemplar_form.html' # Crearemos este archivo
    # Campos del modelo Ejemplar
    fields = ['libro', 'codigo_barras', 'estado', 'ubicacion', 'ingreso'] 
    success_url = reverse_lazy('ejemplares') # Redirige a la lista de ejemplares