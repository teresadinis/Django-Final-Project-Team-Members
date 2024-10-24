from django import forms
from .models import Post, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
