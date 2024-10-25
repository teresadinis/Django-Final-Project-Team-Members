from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Membro(models.Model):

    ESTADOS = [
        ('ativo','ativo'),
        ('inativo', 'inativo')
    ]

    GRUPOS = [
        ('grupo1', 'grupo1'),
        ('grupo2', 'grupo2'),
        ('grupo3', 'grupo3'),
        ('grupo4', 'grupo3'),
    ]

    nome_completo = models.CharField(max_length=200)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ativo', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    grupo = models.CharField(max_length=10, choices=GRUPOS, blank=True, null=True)
    instituicao = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    orcid = models.URLField(blank=True, null=True)
    sci_vitae = models.URLField(blank=True, null=True)
    data_entrada = models.DateField(auto_now_add=True,blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True) # como adicionar manualmente?

    def __str__(self) -> str:
        return self.nome_completo
    
class Investigador(models.Model): # como relaciono com classe Membro?

    ESTADOS = [
    ('sim','sim'),
    ('não', 'não')
    ]

    integrado_FCT = models.CharField(max_length=10, choices=ESTADOS, default='sim', blank=True, null=True)
    data_contrato = models.DateField(blank=True, null=True) # como adicionar manualmente?

class Aluno(models.Model): # como relaciono com classe Membro?

    ESTADOS = [
    ('ativo','ativo'),
    ('inativo', 'inativo')
    ]

    num_mec = models.PositiveSmallIntegerField()
    matriculado = models.CharField(max_length=10, choices=ESTADOS, default='ativo', blank=True, null=True)
    data_matricula = models.DateField(blank=True, null=True) # como adicionar manualmente?

class Tese(models.Model): # como relaciono com classe Membro?
    titulo = models.CharField(max_length=200)
    main_orientador = models.CharField(max_length=200)
    data_defesa = models.DateField(blank=True, null=True) # como adicionar manualmente?

    def __str__(self) -> str:
        return self.titulo
