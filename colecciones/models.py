from django.db import models
from django.utils.text import slugify # Importamos slugify para autogenerar el slug

# 1. Modelo Categoria
class Categoria(models.Model): 
    nombre = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField(max_length=100, unique=True, blank=True, 
                            help_text="Se genera automáticamente a partir del nombre.") 

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Genera automáticamente el slug a partir del nombre si está vacío
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

# 2. Modelo Etiqueta 
class Etiqueta(models.Model): 
    nombre = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nombre

# 3. Modelo Ubicacion 
class Ubicacion(models.Model): 
    sala = models.CharField(max_length=100) 
    estante = models.CharField(max_length=50) 
    nivel = models.CharField(max_length=50)

    def __str__(self):
        # Esto crea una descripción clara, ej: "Sala Principal - Estante: A-01, Nivel: 3"
        return f"{self.sala} - Estante: {self.estante}, Nivel: {self.nivel}"
