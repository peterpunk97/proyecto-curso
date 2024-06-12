from django.db import models

class Alumnos(models.Model): #define la esctructura de la tabla
    matricula = models.CharField(max_length=12)#texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now=True) #Fecha y tiempo
    updated =  models.DateTimeField(auto_now=True)
