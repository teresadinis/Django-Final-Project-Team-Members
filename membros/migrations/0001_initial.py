# Generated by Django 5.1.1 on 2024-10-25 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('ativo', 'ativo'), ('inativo', 'inativo')], default='ativo', max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('grupo', models.CharField(choices=[('grupo1', 'grupo1'), ('grupo2', 'grupo2'), ('grupo3', 'grupo3'), ('grupo4', 'grupo3')], max_length=10)),
                ('instituicao', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento', models.CharField(max_length=50)),
                ('orcid', models.URLField(blank=True, null=True)),
                ('sci_vitae', models.URLField(blank=True, null=True)),
                ('data_entrada', models.DateField(auto_now_add=True, null=True)),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='membros.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Investigador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integrado_FCT', models.CharField(blank=True, choices=[('sim', 'sim'), ('não', 'não')], default='sim', max_length=10, null=True)),
                ('data_contrato', models.DateField(blank=True, null=True)),
                ('membro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membros.membro')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_mec', models.PositiveSmallIntegerField(unique=True)),
                ('matriculado', models.CharField(blank=True, choices=[('ativo', 'ativo'), ('inativo', 'inativo')], default='ativo', max_length=10, null=True)),
                ('data_matricula', models.DateField(blank=True, null=True)),
                ('membro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membros.membro')),
            ],
        ),
        migrations.CreateModel(
            name='Tese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('main_orientador', models.CharField(max_length=200)),
                ('data_defesa', models.DateField(blank=True, null=True)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membros.aluno')),
            ],
        ),
    ]
