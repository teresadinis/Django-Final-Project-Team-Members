from django.shortcuts import redirect, render
from .forms import LivroForm
from .models import Livro


# Create your views here.
def home(request):
    livros = Livro.objects.all()
    return render(request,'livraria/home.html',{'livros':livros})

def add(request):
    form = LivroForm()
    if request.method=="POST":
        form = LivroForm(request.POST,request.FILES) #vai "chamar", a partir do forms.py, todos os campos da base de dados tabela livro (models)
        if form.is_valid(): #caso os campos estejam correctamante prenchidos não redireciona grava e redireciona
            form.save()
            return redirect("livraria:home")
    return render(request,'livraria/add.html', {'form':form})
