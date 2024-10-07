from django.shortcuts import render
from todo.models import Tarefa

# Create your views here.
def mostrar_tarefas(request):
    #obter as tarefas da base de dados
    tarefas = Tarefa.objects.all()
    #enviar para o template (home.html) as tarefas
    return render(request, "todo/home.html", {'tarefas':tarefas})