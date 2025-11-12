from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True)

def __str__(self):
        return f"{self.nombre} {self.apellido}"


class editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True)


def __str__(self):
        return self.nombre 


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model): 
    titulo = models.CharField(max_length=200) 
    isbn = models.CharField(max_length=20, unique=True) 
    anio = models.PositiveIntegerField(null=True, blank=True) 
    editorial = models.ForeignKey(editorial, on_delete=models.PROTECT, 
        related_name="libros") 
    autores = models.ManyToManyField(Autor, related_name="libros", blank=True) 
    categorias = models.ManyToManyField(Categoria, related_name="libros", blank=True)