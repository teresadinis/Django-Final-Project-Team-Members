from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CompraForm, LivroForm, EditoraForm, UserForm
from .models import Compra, Livro, Editora
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    livros = Livro.objects.all()[:10]  #[:10] para mostrar apenas os primeiros 10registos
    # [:10] coloca LIMIT 10
    # [10:20] coloca LIMIT 10 OFFSET 10
    # livros = livros.values('id','nome','imagem')
    # livros = livros.values_list('id','nome','imagem')
    print("comando sql")
    print(livros.query)
    return render(request,'livraria/home.html',{'livros':livros})

@login_required(login_url="/livraria/")
def add(request):
    if ( not request.user.is_staff):
        return redirect("livraria:home")
    form = LivroForm()
    if request.method=="POST":
        form = LivroForm(request.POST,request.FILES)
        # nome = request.POST['nome']
        if form.is_valid():
            form.save()
            return redirect("livraria:home")
    return render(request,'livraria/add.html',{'form':form})

# http://127.0.0.1:8000/livraria/editora/1
def pesquisa_livros_por_editora(request,id):
    editora = Editora.objects.get(pk=id)  
    print("CODIGO SQL")
    print(editora)
    livros = Editora.objects.get(pk=id).livro_set.all()
    return render(request,'livraria/home.html',{'livros':livros, 'editora': editora, 'n':len(livros)})


class CreateEditoraView(CreateView):
    model = Editora    
    form_class = EditoraForm
    template_name = 'livraria/add_editora.html'
    success_url = reverse_lazy('livraria:editoras')
    
# from django.views.generic import CreateView, ListView

class ListEditoraView(ListView):
    model = Editora
    template_name = 'livraria/editoras.html'
    
'''   
def pesquisa(request):
    livros = []
    if request.method=="POST":
        campo = request.POST["campo"]
        # print("pesquisando por.."+campo)
        livros_com_nome = Livro.objects.filter(nome__icontains=campo) 
        livros_de_editora = Livro.objects.filter(editora__nome__icontains=campo)
        livros =  livros_com_nome | livros_de_editora
        print(livros.query)
    return render(request,"livraria/pesquisa.html",{'livros':livros})
'''
from django.db.models import Q

def pesquisa(request):
    livros = []
    if request.method=="POST":
        campo = request.POST["campo"]
        # print("pesquisando por.."+campo)
        livros = Livro.objects.filter( Q(nome__icontains=campo) | Q(editora__nome__icontains=campo))
        print("nova versão!")
        print(livros.query)
    return render(request,"livraria/pesquisa.html",{'livros':livros})



# from django.contrib.auth import login, logout, authenticate

def logout_user(request):
    logout(request)
    return redirect('livraria:home')

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def login_user(request):
    if request.method=="POST":
        username1 = request.POST.get('username')
        password1 = request.POST['password']
        utilizador = authenticate(username=username1,password=password1)
        if utilizador is not None:
            # print('login válido')
            login(request,utilizador)
            return redirect('livraria:home')
        else:
            messages.error(request,"credenciais incorretas! ")          
    return render(request,'livraria/login.html')

def compra(request):
    form = CompraForm()
    print(request.user.id)
    print(request.user.username)
    if request.method=="POST":
        form = CompraForm(request.POST)
        form.save()
        form.instance.utilizador = request.user 
        form.save()
    return render(request,'livraria/compra.html',{'form':form})


# from django.contrib.auth.models import User   

def criar_conta(request):
    form = UserForm()
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,email,password)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect("livraria:login_user")
    return render(request,'livraria/criar_conta.html',{'form':form})

# from django.contrib.auth.forms import UserCreationForm
# def criar_conta(request):
#     # form = UserForm()
#     form = UserCreationForm()
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password1']
#         # email = request.POST['email']
#         email =''
#         user = User.objects.create_user(username,email,password)
#         # user.first_name = request.POST['first_name']
#         # user.last_name = request.POST['last_name']
#         # user.save()
#         return redirect("livraria:login_user")
#     return render(request,'livraria/criar_conta.html',{'form':form})

@login_required(login_url="/livraria/")
def elimina_editora(request, id):
    editora = Editora.objects.filter(pk=id)
    # livros_da_editora =Editora.objects.get(pk=id).livro_set.all()
    # print(livros_da_editora)
    numero_livros_da_editora =Editora.objects.get(pk=id).livro_set.all().count()
    print(numero_livros_da_editora)
    if numero_livros_da_editora==0:
        editora.delete()
    else:
        return HttpResponse(
                            # "<h1>não é possível eliminar a editora!</h1>"
                            # "<h2>já temos livros associados a esta editora</h2>"
                            """<script>
                                     alert('não é possível eliminar a editora!');
                                     history.go(-1);
                                </script>
                            """
                            )
    return redirect("livraria:editoras")

def ver_perfil(request):
    return render(request,'livraria/perfil.html')

@login_required(login_url="/livraria/")
def compras(request):
    compras = Compra.objects.all().filter(utilizador_id=request.user.id)
    return render(request, 'livraria/compras.html',{'compras':compras})


def detalhes_livro(request,id):
    livro = Livro.objects.get(pk=id)
    print(livro)
    return render(request,'livraria/livro.html',{'livro':livro})

def elimina_livro(request, id):
    livro = Livro.objects.get(pk=id)
    livro.delete() 
    return redirect('livraria:home')