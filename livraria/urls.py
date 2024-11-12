from django.urls import path
from . import views
# from .views import CreateEditoraView

app_name = 'livraria'

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('editora/add', views.CreateEditoraView.as_view() ,name='editora_add'),
    path('editora', views.ListEditoraView.as_view(), name='editoras' ),
    path('editora/<int:id>', views.pesquisa_livros_por_editora,name='pesquisa_livros_por_editora'),
    path('editora/del/<int:id>', views.elimina_editora,name='elimina_editora'),
    path('pesquisa', views.pesquisa, name='pesquisa'), 
    path('logout', views.logout_user, name='logout_user'),
    path('login',views.login_user, name='login_user'),
    path('compra',views.compra, name="compra"),
    path('criarconta', views.criar_conta, name='criar_conta'),    #signup
    path('perfil',views.ver_perfil, name='perfil'),
    path('compras',views.compras, name='compras'),
    path('livro/<int:id>', views.detalhes_livro,name="detalhes_livro"),
    path('livro/del/<int:id>', views.elimina_livro,name="elimina_livro"),
]