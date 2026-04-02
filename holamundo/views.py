from django.shortcuts import render

# Create your views here.
contexto ={
        'nombre': 'Emanzh',
        'edad': 25,
        'mascota': ['Perro', 'Gato', 'Pez'],
    }

def saludo(request):
    return render(request, 'holamundo/index.html', contexto)

def despedida(request):
    return render(request, 'holamundo/despedida.html', contexto)