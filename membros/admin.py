from django.contrib import admin
from .models import Aluno, Categoria, Investigador, Membro, Tese

# Register your models here.
#admin.site.register(Membro)
#admin.site.register(Categoria)

modelos = (Aluno, Categoria, Investigador, Tese, Membro)
admin.site.register(modelos)