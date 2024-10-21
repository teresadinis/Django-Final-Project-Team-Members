from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nome


class Post(models.Model):
    titulo = models.CharField('título', max_length=200)
    imagem = models.ImageField(upload_to="images/")
    data = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)

    def __str__(self) -> str:
        return self.titulo + " - " + self.imagem.url
        #return self.titulo
