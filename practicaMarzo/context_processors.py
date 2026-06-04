from datetime import datetime
from todolist.models import Etiqueta
from django.core.cache import cache


def year_context(request):
    year = datetime.now().year
    return {"year": year}


def bienvenido_context(request):
    if request.user.is_authenticated:
        mensaje = f"Bienvenido, {request.user.username}!"
    else:
        mensaje = "Bienvenido a mi sitio web! Logeate!!"
    return {"mensaje_bienvenida": mensaje}


def etiquetas_context(request):
    etiquetas = cache.get("todolist_etiquetas")
    if etiquetas is None:
        etiquetas = Etiqueta.objects.all()
        cache.set("todolist_etiquetas", etiquetas, 3600)  # cache por una hora
        # print("nueva cache seteada")
    return {"etiquetas_populares": etiquetas}
