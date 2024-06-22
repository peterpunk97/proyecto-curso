from django.db import models

class Curso(models.Model):
    idCurso = models.CharField(max_length=10, verbose_name="ID Curso", primary_key=True)
    nombreCurso = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Añade una descripción")
    fechaInicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
    imagen = models.ImageField(null=True, upload_to="Imagen", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Meta:
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"
    ordering = ["created"]
    #el menos indica que se ordenara del más reciente al mas viejo

def __str__(self):
    return self.nombreCurso

