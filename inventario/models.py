from django.db import models
from catalogo.models import Libro
from colecciones.models import Ubicacion

ESTADO_EJEMPLAR = [
    ("DISPONIBLE", "Disponible"),
    ("PRESTADO", "Prestado"),
    ("DANADO", "Dañado"),
    ("PERDIDO", "Perdido"),
]
class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    rfc = models.CharField(max_length=20, blank=True)
    contacto = models.CharField(max_length=100, blank=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre
    

class IngresoInventario(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True, related_name="ingresos"
    )
    nota = models.TextField(blank=True)
    class Meta:
        ordering = ["-fecha"]
    def __str__(self):
        prov = self.proveedor.nombre if self.proveedor else "Sin proveedor"
        return f"Ingreso {self.fecha} · {prov}"



class Ejemplar(models.Model):
    libro = models.ForeignKey(
        Libro, on_delete=models.CASCADE, related_name="ejemplares"
    )
    codigo_barras = models.CharField(max_length=50, unique=True)
    estado = models.CharField(
        max_length=15, choices=ESTADO_EJEMPLAR, default="DISPONIBLE"
    )
    ubicacion = models.ForeignKey(
        Ubicacion, on_delete=models.SET_NULL, null=True, related_name="ejemplares"
    )
    ingreso = models.ForeignKey(
        IngresoInventario, on_delete=models.SET_NULL, null=True, blank=True, related_name="ejemplares"
    )
    class Meta:
        ordering = ["libro__titulo", "codigo_barras"]
    def __str__(self):
        return f"{self.libro.titulo} · {self.codigo_barras}"