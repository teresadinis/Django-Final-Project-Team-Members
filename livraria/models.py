from django.db import models
import datetime

# Create your models here.
class Editora(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome

class Livro(models.Model):

    FORMATOS = [
        ('ebook','ebook'),
        ('paperback','paperback'),
        ('30x30', 'Album 30x30'),
        ('100x100', 'Album 30x30'),
    ]

    nome = models.CharField(max_length=100)
    # decimal(5,2) permite colocar valores desde 0, 0.01, até 999.99
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)
    #ano = models.PositiveSmallIntegerField(default=2024)
    ano = models.PositiveSmallIntegerField(default=datetime.date.today().year)
    tipo = models.CharField(max_length=20, choices=FORMATOS, default='paperback')
    website_compra = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome