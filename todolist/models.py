from django.db import models
from django.conf import settings


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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="responsable",
        default=None,
        null=True,
        blank=True,
    )
    etiquetas = models.ManyToManyField(
        Etiqueta, default=None, blank=True, null=True, related_name="etiquetas"
    )
    activo = models.BooleanField(
        default=True, help_text="Verdadero si NO esta archivada la tarea "
    )
    imagen = models.ImageField(upload_to="card_image/", null=True, blank=True)

    def nombre_mayuscula(self):
        return f"{self.nombre.upper()}"

    def __str__(self):
        return f"Soy la tarea {self.nombre}"

    class Meta:
        verbose_name = "Tareas de proyecto"
        verbose_name_plural = "Tareas de los proyectos"
        ordering = ["-id"]


# si creo o modifico un modelo, debo correr:
# python manage.py makemigrations
# python manage.py migrate
