from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [ # tem como resultado o url http://127.0.0.1:8000/todo/
    path('', views.mostrar_tarefas, name='mostrar_tarefas'),
    path('inserir/', views.inserir_tarefa, name='inserir_tarefa'),
    path('eliminar/<int:id>', views.eliminar_tarefa, name='eliminar_tarefa'),
    path('alterar/<int:id>', views.alterar_tarefa, name='alterar_tarefa'),
]