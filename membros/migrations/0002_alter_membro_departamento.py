# Generated by Django 5.1.1 on 2024-10-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='departamento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
