from django import forms
from .models import *

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = "__all__"
        widgets = {
            'orcid': forms.TextInput(attrs={'placeholder':'url...'}),
            'sci_vitae': forms.TextInput(attrs={'placeholder':'url...'}),
            'data_entrada': forms.TextInput(attrs={'type':'date'}),
            'data_saida': forms.TextInput(attrs={'type':'date'})
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class InvestigadorForm(forms.ModelForm):
    class Meta:
        model = Investigador
        fields = "__all__"
        widgets = {
            'data_contrato': forms.TextInput(attrs={'type':'date'})
        }

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
        widgets = {
            'num_mec': forms.NumberInput(attrs={'placeholder':'número mecanográfico...','min':0,'class':'campopequeno'}),
            'data_matricula': forms.TextInput(attrs={'type':'date'})
        }

class TeseForm(forms.ModelForm):
    class Meta:
        model = Tese
        fields = "__all__"
        widgets = {
            'main_orientador': forms.TextInput(attrs={'placeholder':'nome1; nome2;...'}),
            'data_defesa': forms.TextInput(attrs={'type':'date'})
        }