import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Editora(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome
    
class Livro(models.Model):
    
    FORMATOS = [
        ('P','Paperback'),
        ('H','Hardcover'),
        ('E','Ebook'),
    ]
    
    nome = models.CharField(max_length=100)
    # decimal(5,2) permite colocar valores desde 0, 0.01, até 999.99
    preco = models.DecimalField('preço',max_digits=5, decimal_places=2, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)
    #site = models.URLField( blank=True, null=True)
    ano = models.PositiveSmallIntegerField(default=datetime.date.today().year)
    tipo = models.CharField(max_length=20, choices=FORMATOS, default='P')
    # detalhes = models.CharField(max_length=300, blank=True, null=True)
    # data = models.DateField("data")
    data = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome

#from django.contrib.auth.models import User
  
class Compra(models.Model):
    quantidade = models.PositiveSmallIntegerField(default=1)
    data = models.DateTimeField(auto_now_add=True)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    utilizador = models.ForeignKey(User, on_delete=models.PROTECT, null=False,blank=True)
    
    def __str__(self) -> str:
        return "compra "+ str(self.quantidade) + " unidade(s)  do livro: "+ self.livro.nome.upper()