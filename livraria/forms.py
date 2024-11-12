from django import forms
from .models import Compra, Livro, Editora
from django.contrib.auth.models import User 

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"
        
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'nome...'}),
            'preco': forms.NumberInput(attrs={'placeholder':'preço...','min':0,'class':'campopequeno'}),
            'ano':forms.NumberInput(attrs={'class':'campopequeno'}),
            # 'detalhes': forms.Textarea(attrs={'cols': 40, 'rows': 3,'placeholder':'detalhes...'}),
            # 'data': forms.TextInput(attrs={'type':'datetime-local'})
            'data': forms.TextInput(attrs={'type':'date'})   
        }
        
class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = "__all__"
        
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('quantidade','livro')
        # except = ('utilizador',)

# from django.contrib.auth.models import User     
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email')
        
        widgets = {
            'password': forms.PasswordInput(),
        }