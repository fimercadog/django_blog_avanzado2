# Generated by Django 4.1.3 on 2022-11-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de Autor')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Appelidos del autor')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Github')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor Activo/NO Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada//Categoria no activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
