from django.shortcuts import redirect, render
from .forms import PostForm
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