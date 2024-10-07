from django.db import models

# Create your models here.
class Tarefa(models.Model):
    """titulo = models.TextField()
    realizado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_created=True)"""

    # Nova versão da classe que permite inserir tarefas
    titulo = models.CharField(max_length=100)
    realizado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo.capitalize()