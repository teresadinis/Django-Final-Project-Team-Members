# Generated by Django 5.1.1 on 2024-10-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0006_alter_membro_data_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='data_entrada',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='data_saida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
