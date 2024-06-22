from django.shortcuts import render
from.models import Alumnos

def registros(request):
    return render(request, "registros/principal.html")
#Indicamos el lugar donde se renderizara el resultado de esta vista
