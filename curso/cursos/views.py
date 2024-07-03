from django.shortcuts import render
from .models import Curso
from datetime import date


def registroCursos(request):
    cursos=Curso.objects.all()
    return render(request, "registros/cursos.html", {'cursos':cursos})


def consultar1(request):
    cursos=Curso.objects.filter(nombreCurso="Sistemas operativos")
    return render(request, "registros/consultas.html", {'cursos':cursos})


def consultar2(request):
    cursos = Curso.objects.filter(nombreCurso__endswith="1")
    return render(request, "registros/consultas.html", {'cursos':cursos})

def consultar3(request):
    cursos = Curso.objects.filter(nombreCurso__startswith="D")
    return render(request, "registros/consultas.html", {'cursos':cursos})

def consultar4(request):
    fechaInicio = date(2024, 9, 9)
    fechaFin = date(2024, 9, 10)  
    cursos = Curso.objects.filter(fechaInicio__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'cursos': cursos})

def consultar5(request):
    cursos = Curso.objects.filter(actividad__descripcion__icontains="realizar")
    return render(request, "registros/consultas.html", {'cursos': cursos})

