from django.shortcuts import render
from .models import Curso

def registroCursos(request):
    cursos=Curso.objects.all()
    return render(request, "registros/cursos.html", {'cursos':cursos})
