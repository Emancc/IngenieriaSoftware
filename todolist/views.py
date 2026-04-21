from django.shortcuts import render, redirect
from datetime import date
from .models import Tarea
from .forms import TareaForm


# Create your views here.
def tareas(request):

    tareas = Tarea.objects.all().order_by("-id")  # lo trae desde el ultimo al primero
    return render(request, "todolist/index.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "POST":
        # logica de agregar a la base de datos
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
        form = TareaForm()
    return render(request, "todolist/crear_tarea.html", {"form": form})

    """
    # LOOKUPS -Obtencion de datos desde la orm
    # excluciones
    tareas = Tarea.objects.exclude(nombre__icontains="bugfix")
    #get by id
    tareas = Tarea.objects.get(id=1)
    # str
    tareas = Tarea.objects.filter(nombre__icontains="platos")
    # filtros de int y floats
    posteos = Posteos.object.filter(likes__gt=10)
    posteos = Posteos.object.filter(likes__gte=10)
    posteos = Posteos.object.filter(likes__lt=100)
    posteos = Posteos.object.filter(likes__lte=100)
    posteos = Posteos.object.filter(likes__range=(10, 100))

    # filtro de listas
    tareas = Tarea.objects.filter(etiquetas__in=["Urgente", 2025])

    # filtro de fechas
    tareas = Tarea.objects.filter(fecha_completado__year=2025)
    tareas.filter(fecha_completado__month=8)

    # saber si es nulo
    tareas = Tarea.objects.filter(responsable__isnull=False)
    # campos relacionables
    tareas = Tarea.objects.filter(responsable__username="Eman")
    """
