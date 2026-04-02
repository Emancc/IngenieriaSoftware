from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo, name='saludo'),
    path('despedida/', views.despedida, name='despedida'),
]