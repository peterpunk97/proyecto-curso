from django.db import models

class Alumnos(models.Model): #define la esctructura de la tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat")#texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    created = models.DateTimeField(auto_now=True) #Fecha y tiempo
    updated =  models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo

    def __str__(self):
        return self.nombre
        #indica que se mostrará el nombre cuyo valor 
