from django.contrib import admin

from .models import Editora, Livro, Compra
# from .models import Membro, Categoria
# from .models import Membro, Aluno, Categoria, Investigador, Tese

# # Register your models here.
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Compra)
# # admin.site.register(Membro)
# # admin.site.register(Categoria)

# modelos = (Aluno, Categoria, Investigador, Tese, Membro)
# admin.site.register(modelos)