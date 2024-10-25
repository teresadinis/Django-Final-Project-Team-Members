from django.shortcuts import redirect, render
from .forms import CategoriaForm, PostForm
from .models import Post

# Create your views here.
def home(request):
    #obter todos os posts, ordenados por data, por ordem decrescente
    # order by('data') por ordem crescente
    # order by('-data') por ordem decrescente
    posts = Post.objects.order_by('-data')
    return render(request,'posts/home.html', {'posts':posts})

def add(request):
    form = PostForm()
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        form.save()
        return redirect("posts:home")
    return render(request,'posts/add.html',{'form':form})

def delete(request, id):
    post = Post.objects.filter(pk=id)
    post.delete()
    return redirect("posts:home")

def edit(request,id):
    post = Post.objects.get(pk=id)
    if request.method=="GET":
        #obter dados antigos
        #get quando fazemos o edit
        form = PostForm(instance=post)
        return render(request,'posts/edit.html',{'form':form})
    elif request.method=="POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        form.save()
        return redirect("posts:home")

def details(request,id):
    # obter dados do post com primary key igual ao parâmetro id
    post = Post.objects.get(pk=id)
    return render(request,'posts/details.html',{'post':post})

def addcategory(request):
    form = CategoriaForm()
    if request.method=="POST":
        form = CategoriaForm(request.POST)
        form.save()
        return redirect ("posts:home")
    return render(request,'posts/addcategory.html',{"form":form})