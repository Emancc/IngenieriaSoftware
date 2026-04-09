from django.contrib import admin
from .models import Tarea, Etiqueta

# Register your models here.


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "completada",
        "fecha_completada",
        "fecha_creacion",
        "responsable",
    )

    list_filter = ("completada", "fecha_completada", "fecha_creacion")
    search_fields = ("nombre",)
    readonly_fields = ("completada",)


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "color")
    search_fields = ("nombre",)
