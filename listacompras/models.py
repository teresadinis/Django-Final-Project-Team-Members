from django.db import models

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.nome.capitalize() + " - " + str(self.quantidade) + " unidade(s)"