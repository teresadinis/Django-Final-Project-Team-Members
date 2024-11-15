# Generated by Django 5.1.1 on 2024-11-12 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='preço')),
                ('isbn', models.CharField(blank=True, max_length=20, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='livros/')),
                ('ano', models.PositiveSmallIntegerField(default=2024)),
                ('tipo', models.CharField(choices=[('P', 'Paperback'), ('H', 'Hardcover'), ('E', 'Ebook')], default='P', max_length=20)),
                ('data', models.DateField(blank=True, null=True)),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livraria.editora')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('utilizador', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livraria.livro')),
            ],
        ),
    ]
