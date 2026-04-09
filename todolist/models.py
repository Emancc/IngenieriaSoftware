from django.contrib.auth.models import User
from django.db import models


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"Etiqueta {self.nombre}"


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completada = models.BooleanField(
        default=False,
        help_text="la tarea se ha completada o no",
        verbose_name="FINALIZADA",
    )
    fecha_completada = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    responsable = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="responsable",
        default=None,
        null=True,
        blank=True,
    )
    etiquetas = models.ManyToManyField(
        Etiqueta, default=None, blank=True, null=True, related_name="etiquetas"
    )

    def __str__(self):
        return f"Soy la tarea {self.nombre}"


# si creo o modifico un modelo, debo correr:
# python manage.py makemigrations
# python manage.py migrate
