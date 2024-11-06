from django.urls import path
from . import views

app_name = "membros"

urlpatterns = [
    path('', views.home, name='home'),
    path('list1/',views.list_details, name='list_details'),
    path('<int:id>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('addresearcher/', views.addresearcher, name='addresearcher'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('addthesis/', views.addthesis, name='addthesis'),
    path('list2/',views.list_edit, name='list_edit'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit2/<int:id>', views.edit_researcher, name='edit_researcher'),
    path('edit3/<int:id>', views.edit_student, name='edit_student'),
    path('edit4/<int:id>', views.edit_thesis, name='edit_thesis'),
    path('list3/',views.list_del, name='list_del'),
    path('del/<int:id>',views.delete, name='delete'),
    path('pesquisa1', views.search_details, name='search_details'),
    path('pesquisa2', views.search_edit, name='search_edit'),
    path('pesquisa3', views.search_del, name='search_del'),
    path('login',views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
]