from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.

def home(request):
    opcoes = Menu.objects.all()
    return render(request,'membros/home.html',{'opcoes':opcoes})

def list_details(request):
    membros = Membro.objects.all()
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
    membros = Membro.objects.all()
    return render(request,'membros/list_edit.html',{'membros':membros})

def edit(request,id):
    membro = Membro.objects.get(pk=id)
    if request.method=="GET":
        form = MembroForm(instance=membro)
        return render(request,'membros/edit.html',{'form':form})
    elif request.method=="POST":
        form = MembroForm(request.POST,request.FILES, instance=membro)
        form.save()
        return redirect("membros:details", id=id)

def list_del(request):
    membros = Membro.objects.all()
    return render(request,'membros/list_del.html',{'membros':membros})

def delete(request,id):
    membro = Membro.objects.filter(pk=id)
    membro.delete()
    return redirect("membros:list_del")