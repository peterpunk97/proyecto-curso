from django.shortcuts import render
from.models import Alumnos

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html",{'alumnos':alumnos})
    ##all recupera todos los objetos del modelo (registros de la tabla alumnos)
#Indicamos el lugar donde se renderizará el resultado de esta vista