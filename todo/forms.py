from django import forms
from todo.models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        #fields = "__all__"
        fields = ('titulo',) # enumerar os campos a aparecer no formulário
        #exclude = ('realizado',)

        