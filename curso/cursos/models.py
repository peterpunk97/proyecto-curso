from django.db import models
from ckeditor.fields import RichTextField

class Curso(models.Model):
    idCurso = models.CharField(max_length=10, verbose_name="ID Curso", primary_key=True)
    nombreCurso = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Añade una descripción")
    fechaInicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
        #el menos indica que se ordenara del más reciente al mas viejo

    def __str__(self):
        return self.nombreCurso


class Actividad(models.Model):
    claveActividad = models.CharField(max_length=20, verbose_name="Clave Actividad", primary_key=True)
    descripcion = RichTextField(verbose_name="Descripción")
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    nombreCurso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nombre del Curso")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-fechaCreacion"]

    def __str__(self):
        return self.claveActividad
