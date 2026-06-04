from django.urls import path
from . import views

urlpatterns = [
    path("", views.tareas, name="tareas"),
    path("nueva/", views.crear_tarea, name="crear_tarea"),
    path("editar/<int:id>/", views.editar_tarea, name="editar_tarea"),
    path("eliminar/<int:id>/", views.eliminar_tarea, name="eliminar_tarea"),
    # ---------clase based views------:
    path("cbv/", views.GetTareas.as_view()),
    path("cbv/nueva/", views.CreateTarea.as_view()),
    path("cbv/editar/<int:pk>", views.UpdateTareas.as_view()),
    path("cbv/eliminar/<int:pk>", views.DeleteTarea.as_view()),
]
