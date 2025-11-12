from django.contrib import admin

# Register your models here.

from .models import Autor, editorial, Categoria, Libro
admin.site.register(Autor)
admin.site.register(editorial)
admin.site.register(Categoria)
admin.site.register(Libro)

