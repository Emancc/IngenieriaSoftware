# aplicacion holamundo
from django.shortcuts import render
from todolist.models import Tarea


def saludo(request):
    tareas = Tarea.objects.all()
    return render(request, "holamundo/index.html", dict(tareas=tareas))


def despedida(request):
    return render(
        request,
        "holamundo/despedida.html",
    )
