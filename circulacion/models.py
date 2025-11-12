from django.db import models
from inventario.models import Ejemplar
from personas.models import Socio, Empleado
from catalogo.models import Libro
ESTADO_RESERVA = [
    ("PENDIENTE", "Pendiente"),
    ("ACTIVA", "Activa"),
    ("CANCELADA", "Cancelada"),
    ("CADUCADA", "Caducada"),
]


class Prestamo(models.Model):
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.PROTECT, related_name="prestamos")
    socio = models.ForeignKey(Socio, on_delete=models.PROTECT, related_name="prestamos")
    empleado_entrega = models.ForeignKey(
        Empleado, on_delete=models.PROTECT, related_name="prestamos_entregados"
    )
    fecha_prestamo = models.DateField()
    fecha_vencimiento = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["-fecha_prestamo"]
    def __str__(self):
        return f"Préstamo #{self.pk} · {self.ejemplar} → {self.socio}"


class Reserva(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="reservas")
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="reservas")
    estado = models.CharField(max_length=20, choices=ESTADO_RESERVA, default="PENDIENTE")
    creada_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-creada_en"]
    def __str__(self):
        return f"Reserva #{self.pk} · {self.libro} · {self.socio}"


class Multa(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="multas")
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    motivo = models.CharField(max_length=200)
    pagada = models.BooleanField(default=False)
    class Meta:
        ordering = ["-id"]
    def __str__(self):
        return f"Multa #{self.pk} · ${self.monto}"