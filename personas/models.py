from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    telefono = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre


class Membresia(models.Model):
    BASICA = "BASICA"
    PREMIUM = "PREMIUM"
    TIPOS = [
        (BASICA, "Básica"),
        (PREMIUM, "Premium"),
    ]
    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE, related_name="membresias"
    )
    tipo = models.CharField(max_length=10, choices=TIPOS, default=BASICA)
    inicio = models.DateField()
    fin = models.DateField()
    class Meta:
        ordering = ["-fin"]
        constraints = [
            models.UniqueConstraint(
                fields=["socio", "inicio", "fin"], name="uniq_membresia_rango_por_socio"
            )
        ]
    def __str__(self):
        return f"{self.socio} · {self.tipo} ({self.inicio}–{self.fin})"



class Empleado(models.Model):
    BIBLIOTECARIO = "BIBLIOTECARIO"
    ADMIN = "ADMIN"
    ROLES = [
        (BIBLIOTECARIO, "Bibliotecario"),
        (ADMIN, "Administrador"),
    ]
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default=BIBLIOTECARIO)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return f"{self.nombre} ({self.rol})"
