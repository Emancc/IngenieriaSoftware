from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            "nombre",
            "completada",
            "fecha_completada",
            "responsable",
            "etiquetas",
            "imagen",
        ]
