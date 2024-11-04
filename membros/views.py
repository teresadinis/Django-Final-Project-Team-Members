from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    opcoes = Menu.objects.all()
    return render(request,'membros/home.html',{'opcoes':opcoes})

@login_required(login_url="/membros/")
def add(request):
    form = MembroForm()
    if request.method=="POST":
        form = MembroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("membros:home")
    return render(request,'membros/add.html',{'form':form})


def list_details(request):
    membros = Membro.objects.all().order_by("nome_completo")
    return render(request,'membros/list_details.html',{'membros':membros})

def details(request,id):
    membros = Membro.objects.get(pk=id)
    return render(request,'membros/details.html',{'membros':membros})

def add(request):
    if request.method == "GET":
        form = MembroForm()
        return render(request,'membros/add.html',{'form':form})
    elif request.method == "POST":
        form = MembroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("membros:home")

def addcategory(request):
    form = CategoriaForm()
    if request.method=="POST":
        form = CategoriaForm(request.POST)
        form.save()
        return redirect ("membros:add")
    return render(request,'membros/addcategory.html',{"form":form})

def list_edit(request):
    membros = Membro.objects.all().order_by("nome_completo")
    return render(request,'membros/list_edit.html',{'membros':membros})

def edit(request,id):
    membro = Membro.objects.get(pk=id)
    if request.method=="GET":
        form = MembroForm(instance=membro)
        return render(request,'membros/edit.html',{"form":form})
    elif request.method=="POST":
        form = MembroForm(request.POST,request.FILES, instance=membro)
        form.save()
        return redirect("membros:details", id=id)

def list_del(request):
    membros = Membro.objects.all().order_by("nome_completo")
    return render(request,'membros/list_del.html',{'membros':membros})

def delete(request,id):
    membro = Membro.objects.filter(pk=id)
    membro.delete()
    return redirect("membros:list_del")

def search_details(request):
    membros = []
    if request.method == "POST":
        campo = request.POST.get("campo", "")
        
        # Filtrar pelo campo 'campo' em múltiplos atributos do modelo
        # Q() permite combinar filtros usando operadores | (OR) e & (AND)
        membros = Membro.objects.filter(
            Q(nome_completo__icontains=campo) |
            Q(email__icontains=campo) |
            Q(instituicao__icontains=campo) |
            Q(grupo__icontains=campo)|
            Q(categoria__nome__icontains=campo)
        )
        
    return render(request, "membros/search_details.html", {'membros': membros})

def search_edit(request):
    membros = []
    if request.method == "POST":
        campo = request.POST.get("campo", "")
        
        membros = Membro.objects.filter(
            Q(nome_completo__icontains=campo) |
            Q(email__icontains=campo) |
            Q(instituicao__icontains=campo) |
            Q(grupo__icontains=campo)|
            Q(categoria__nome__icontains=campo)
        )
        
    return render(request, "membros/search_edit.html", {'membros': membros})

def search_del(request):
    membros = []
    if request.method == "POST":
        campo = request.POST.get("campo", "")
        
        membros = Membro.objects.filter(
            Q(nome_completo__icontains=campo) |
            Q(email__icontains=campo) |
            Q(instituicao__icontains=campo) |
            Q(grupo__icontains=campo)|
            Q(categoria__nome__icontains=campo)
        )
        
    return render(request, "membros/search_del.html", {'membros': membros})

def logout_user(request):
    logout(request)
    return redirect('membros:home')

def login_user(request):
    if request.method=="POST":
        username1 = request.POST.get('username')
        password1 = request.POST['password']
        utilizador = authenticate(username=username1,password=password1)
        if utilizador is not None:
            login(request,utilizador)
            return redirect('membros:home')
        else:
            messages.error(request,"username e/ou password incorrectos! ")          
    return render(request,'membros/login.html')

