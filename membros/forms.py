from django import forms
from .models import *

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = "__all__"

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"