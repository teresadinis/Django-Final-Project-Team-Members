from django.urls import path

from . import views

app_name = 'listacompras'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('incrementa/<int:id>', views.incrementa, name = 'incrementa'),
    path('decrementa/<int:id>', views.decrementa, name = 'decrementa'),
    path('elimina/<int:id>', views.elimina, name = 'elimina'),
]