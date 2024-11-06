from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request): # home = página com o menu principal
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


def list_details(request): # pagina que lista os membros para consultar detalhes
    membros = Membro.objects.all().order_by("nome_completo")
    return render(request,'membros/list_details.html',{'membros':membros})

def details(request,id): # pagina de detalhes do membro
    membros = Membro.objects.get(pk=id)

    # Inicializa variáveis a none, caso existam dependendo da categoria do membro registado
    investigadores = None
    alunos = None
    teses = None

    # Verifica a categoria ativa as variáveis consoante a categoria escolhida
    if membros.categoria.nome == "Investigador":
        investigadores = Investigador.objects.filter(membro=membros).first()
    elif membros.categoria.nome == "Aluno":
        alunos = Aluno.objects.filter(membro=membros).first()
        if alunos:
            teses = Tese.objects.filter(aluno=alunos).first()

    return render(request, 'membros/details.html', {
        'membros': membros,
        'investigadores': investigadores,
        'alunos': alunos,
        'teses': teses,
    })

def add(request): # registo de um novo membro, depois ramificando para o form consoante a categoria (Investigador, Aluno)
    if request.method == "GET":
        form = MembroForm()
        return render(request,'membros/add.html',{'form':form})
    elif request.method == "POST":
        form = MembroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            if form.save().categoria.nome == "Investigador":
                return redirect("membros:addresearcher")  # Redireciona para 'addresearcher.html'
            elif form.save().categoria.nome == "Aluno":
                return redirect("membros:addstudent")  # Redireciona para 'addstudent.html'

def addcategory(request): # página dentro do registo de novo membro que permite adicionar uma nova categoria que não esteja na lista de opções
    form = CategoriaForm()
    if request.method=="POST":
        form = CategoriaForm(request.POST)
        form.save()
        return redirect ("membros:add")
    return render(request,'membros/addcategory.html',{"form":form})

def addresearcher(request): # página para forms de dados do Investigador, caso seja a categoria escolhida ao registar novo membro
    if request.method == "GET":
        form = InvestigadorForm()
        return render(request,'membros/addresearcher.html',{'form':form})
    elif request.method == "POST":
        form = InvestigadorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("membros:list_details")

def addstudent(request): # página para forms de dados do Aluno, caso seja a categoria escolhida ao registar novo membro
    if request.method == "GET":
        form = AlunoForm()
        return render(request,'membros/addstudent.html',{'form':form})
    elif request.method == "POST":
        form = AlunoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("membros:addthesis") # Redireciona para 'addthesis.html'

def addthesis(request): # página para forms de dados da Tese, caso seja a categoria escolhida ao registar novo membro seja Aluno
    if request.method == "GET":
        form = TeseForm()
        return render(request,'membros/addthesis.html',{'form':form})
    elif request.method == "POST":
        form = TeseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("membros:list_details")

def list_edit(request): # pagina que lista os membros para editar
    membros = Membro.objects.all().order_by("nome_completo")
    return render(request,'membros/list_edit.html',{'membros':membros})

def edit(request,id): # pagina que permite editar os forms do membro
    membro = Membro.objects.get(pk=id)
    if request.method=="GET":
        form = MembroForm(instance=membro)
        return render(request,'membros/edit.html',{"form":form})
    elif request.method=="POST":
        form = MembroForm(request.POST,request.FILES, instance=membro)
        membro_atual = form.save()
        if membro_atual.categoria.nome == "Investigador":
            return redirect("membros:edit_researcher",id=membro_atual.id)  # Redireciona para 'edit_researcher.html'
        elif membro_atual.categoria.nome == "Aluno":
            return redirect("membros:edit_student",id=membro_atual.id)  # Redireciona para 'edit_student.html'

def edit_researcher(request,id): # pagina que permite editar o forms de um membro em especifico com categoria = Investigador
    investigador = Investigador.objects.get(membro__id=id)
    if request.method=="GET":
        form = InvestigadorForm(instance=investigador)
        return render(request,'membros/edit_researcher.html',{"form":form})
    elif request.method=="POST":
        form = InvestigadorForm(request.POST,request.FILES, instance=investigador)
        form.save()
        return redirect("membros:details", id=investigador.membro.id)

def edit_student(request,id): # pagina que permite editar o forms de um membro em especifico com categoria = Aluno
    aluno = Aluno.objects.get(membro__id=id)
    if request.method=="GET":
        form = AlunoForm(instance=aluno)
        return render(request,'membros/edit_student.html',{"form":form})
    elif request.method=="POST":
        form = AlunoForm(request.POST,request.FILES, instance=aluno)
        aluno_atual = form.save()
        return redirect("membros:edit_thesis", id=aluno_atual.id) # Redireciona para 'edit_thesis.html'

def edit_thesis(request,id): # pagina que permite editar o forms da tese de um membro em especifico com categoria = Aluno
    tese = Tese.objects.get(aluno__id=id)
    if request.method=="GET":
        form = TeseForm(instance=tese)
        return render(request,'membros/edit_thesis.html',{"form":form})
    elif request.method=="POST":
        form = TeseForm(request.POST,request.FILES, instance=tese)
        form.save()
        return redirect("membros:details", id=tese.aluno.membro.id)

def list_del(request): # pagina que lista os membros para eliminar/excluir
    membros = Membro.objects.all().order_by("nome_completo")
    return render(request,'membros/list_del.html',{'membros':membros})

def delete(request,id):
    membro = Membro.objects.get(pk=id)

    # Excluir registos de membros relacionados com as classes Aluno e Investigador, se existir
    Aluno.objects.filter(membro=membro).delete()
    Investigador.objects.filter(membro=membro).delete()
    
    # Exclui Tese(s) associada(s) ao Aluno, se existir
    aluno = Aluno.objects.filter(membro=membro).first()
    if aluno:
        Tese.objects.filter(aluno=aluno).delete()  # Exclui as testes relacinadas com o aluno

    membro.delete()  # Exclui o registto inicial de membro
    return redirect("membros:list_del")

def search_details(request): # pesquisa avançada na pagina de consultar membros/detalhes
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

def search_edit(request): # pesquisa avançada na pagina de editar membros
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

def search_del(request): # pesquisa avançada na pagina de eliminar/excluir membros
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

