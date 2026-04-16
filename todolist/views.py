from django.shortcuts import render
from datetime import date
from .models import Tarea


# Create your views here.
def tareas(request):
    tareas = Tarea.objects.filter(nombre__icontains="platos")

    # filtros de int y floats
    posteos = Posteos.object.filter(likes__gt=10)
    posteos = Posteos.object.filter(likes__gte=10)
    posteos = Posteos.object.filter(likes__lt=100)
    posteos = Posteos.object.filter(likes__lte=100)
    posteos = Posteos.object.filter(likes__range=(10, 100))

    # filtro de fechas
    tareas = Tarea.objects.filter(fecha_completado__year=2026)
    tareas.filter(fecha_completado__month=8)

    return render(request, "todolist/index.html", {"tareas": tareas})
