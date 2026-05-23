from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Tarea
from .forms import TareaForm


# creacion de registros
def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("tareas")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


# Create your views here.
@login_required
def tareas(request):

    tareas = Tarea.objects.filter(activo=True)
    # .orderby(-id) lo trae desde el ultimo al primero
    return render(request, "todolist/index.html", {"tareas": tareas})


@login_required
def crear_tarea(request):
    if request.method == "POST":
        # logica de agregar a la base de datos
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
        form = TareaForm()
    return render(request, "todolist/crear_tarea.html", {"form": form})


# Parametro Ruta: url.com/tarea/5
# Query Param: url.com/tarea?clave=valor&clave_dos=valor&clave_tres=valor
@login_required
def editar_tarea(request, id):

    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        form = TareaForm(request.POST, request.FILES, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:

        form = TareaForm(instance=tarea)
    return render(request, "todolist/editar_tarea.html", {"form": form})


@login_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        # tarea.delete()  # esto es un borrado definitivo lo saca de la base de datos
        tarea.activo = False
        tarea.save()
        return redirect("tareas")
    return render(request, "todolist/eliminar_tarea.html", {"tarea": tarea})
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
