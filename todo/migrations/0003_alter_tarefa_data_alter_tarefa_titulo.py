# Generated by Django 5.1.1 on 2024-10-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_tarefa_data_alter_tarefa_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='título'),
        ),
    ]
