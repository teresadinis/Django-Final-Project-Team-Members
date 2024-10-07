from django.urls import path
from . import views

urlpatterns = [ # tem como resultado o url http://127.0.0.1:8000/todo/
    path('', views.mostrar_tarefas, name='mostrar_tarefas'),
]