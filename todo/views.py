from django.shortcuts import redirect, render
from todo.forms import TarefaForm
from todo.models import Tarefa

# Create your views here.
def mostrar_tarefas(request):
    #obter as tarefas da base de dados
    tarefas = Tarefa.objects.all()
    #enviar para o template (home.html) as tarefas
    return render(request, "todo/home.html", {'tarefas':tarefas})

def inserir_tarefa(request):
    formulario = TarefaForm()
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        formulario.save()
        return redirect("todo:mostrar_tarefas") # após enviar tarefa redireciona para a lista de tarefas: path adicionar_tarefas
    return render(request, 'todo/inserir.html', {'formulario':formulario})

def alterar_tarefa(request,id):
    tarefa = Tarefa.objects.get(pk=id)
    formulario = TarefaForm(instance=tarefa)
    if request.method== "POST":
        formulario = TarefaForm(request.POST, instance= tarefa)
        formulario.save()
        return redirect('todo:mostrar_tarefas')

    return render(request, 'todo/alterar.html', {'formulario':formulario})

def eliminar_tarefa(request,id):
    #print('vamos eliminar a tarefa ', id)
    tarefa = Tarefa.objects.filter(pk=id) # pk = primary key
    tarefa.delete()
    return redirect("todo:mostrar_tarefas")