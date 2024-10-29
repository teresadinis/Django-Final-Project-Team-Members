from django.db import models

# Create your models here.
class Menu(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens_menu/', blank=True, null=True)

    def __str__(self) -> str:
        return self.nome.upper()

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome.capitalize()

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
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ativo')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    grupo = models.CharField(max_length=10, choices=GRUPOS)
    instituicao = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    orcid = models.URLField(blank=True, null=True)
    sci_vitae = models.URLField(blank=True, null=True)
    data_entrada = models.DateTimeField(blank=True, null=True)
    data_saida = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome_completo.capitalize()
    
class Investigador(models.Model):

    ESTADOS = [
    ('sim','sim'),
    ('não', 'não')
    ]

    integrado_FCT = models.CharField(max_length=10, choices=ESTADOS, default='sim', blank=True, null=True)
    data_contrato = models.DateTimeField(blank=True, null=True)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.membro.nome_completo.capitalize()

class Aluno(models.Model):

    ESTADOS = [
    ('ativo','ativo'),
    ('inativo', 'inativo')
    ]

    num_mec = models.PositiveSmallIntegerField(unique=True)
    matriculado = models.CharField(max_length=10, choices=ESTADOS, default='ativo', blank=True, null=True)
    data_matricula = models.DateTimeField(blank=True, null=True)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.membro.nome_completo.capitalize()

class Tese(models.Model):
    titulo = models.CharField(max_length=200)
    main_orientador = models.CharField(max_length=200)
    data_defesa = models.DateTimeField(blank=True, null=True)
    aluno = models.ForeignKey(Aluno, models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo
