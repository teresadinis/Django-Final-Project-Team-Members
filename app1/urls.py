from django.urls import path
from . import views # . significa 'directório corrente'

urlpatterns = [ # tem como resultado o url http://127.0.0.1:8000/app1/
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
]