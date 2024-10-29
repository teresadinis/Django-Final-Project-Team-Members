from django.urls import path
from . import views

app_name = "membros"

urlpatterns = [
    path('', views.home, name='home'),
    path('list1/',views.list_details, name='list_details'),
    path('<int:id>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('list2/',views.list_edit, name='list_edit'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('list3/',views.list_del, name='list_del'),
    path('del/<int:id>',views.delete, name='delete'),
]