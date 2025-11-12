# biblioteca/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Apps principales
    path('', include('generales.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('colecciones/', include('colecciones.urls')),
    path('circulacion/', include('circulacion.urls')),
    path('inventario/', include('inventario.urls')),
    path('personas/', include('personas.urls')),
    
    # ▼▼▼ ELIMINA TODAS ESTAS LÍNEAS REDUNDANTES ▼▼▼
    # path('catalogo/libros/', include('catalogo.urls')),     <-- BORRAR
    # path('catalogo/categoria/', include('catalogo.urls')),  <-- BORRAR
    # path('catalogo/editoriales/', include('catalogo.urls')), <-- BORRAR
    # path('categorias', include('colecciones.urls')),      <-- BORRAR
    # path('editoriales', include('colecciones.urls')),     <-- BORRAR
    # path('ubicaciones', include('colecciones.urls')),     <-- BORRAR
]