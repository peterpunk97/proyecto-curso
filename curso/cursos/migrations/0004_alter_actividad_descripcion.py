# Generated by Django 5.0.6 on 2024-06-25 18:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_curso_options_actividad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Descripción'),
        ),
    ]
