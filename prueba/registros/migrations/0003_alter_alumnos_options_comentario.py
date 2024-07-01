# Generated by Django 5.0.6 on 2024-06-24 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_alter_alumnos_options_alumnos_imagen_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={},
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('created', models.DateField(auto_now=True, verbose_name='registrado')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.alumnos', verbose_name='Alumno')),
            ],
        ),
    ]