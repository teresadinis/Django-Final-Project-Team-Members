from django.shortcuts import redirect, render
from .forms import ItemForm
from .models import Item

# Create your views here.
def home(request):
    if request.method=="GET":
        #obter da base de dados
        itens = Item.objects.all()
        # criar um formulário em branco para poder adicionar itens
        formulario = ItemForm()
    elif request.method=="POST":
        formulario = ItemForm(request.POST)
        formulario.save()
        return redirect('listacompras:home')
    return render(request, 'listacompras/home.html', {"itens":itens,"formulario":formulario})

def incrementa(request,id):
    # incrementar a quantidade daquele item
    item = Item.objects.get(pk=id)
    item.quantidade += 1
    item.save()
    # redirecionar para a página home
    return redirect('listacompras:home')

def decrementa(request,id):
    # decrementar a quantidade daquele item
    item = Item.objects.get(pk=id)
    if item.quantidade > 1:
        item.quantidade -= 1
    item.save()
    return redirect('listacompras:home')

def elimina(request,id):
    item = Item.objects.filter(pk=id)
    item.delete()
    return redirect('listacompras:home')
