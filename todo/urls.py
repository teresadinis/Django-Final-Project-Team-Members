from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [ # tem como resultado o url http://127.0.0.1:8000/todo/
    path('', views.mostrar_tarefas, name='mostrar_tarefas'),
    path('inserir/', views.inserir_tarefa, name='inserir_tarefa'),
]