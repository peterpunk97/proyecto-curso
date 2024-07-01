from django.shortcuts import render
from.models import Alumnos
from.forms import ComentarioContactoForm
from .models import ComentarioContacto


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son corectos 
            form.save()#inserta
            return render(request, 'registros/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos 
    return render(request, 'registros/contacto.html', {'form': form})

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html",{'alumnos':alumnos})
    ##all recupera todos los objetos del modelo (registros de la tabla alumnos)


def contacto(request):
    return render(request,"registros/contacto.html")

def comentarios(request):
    return render(request,"registros/comentarios.html")


def comentarios(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request, "registros/comentarios.html",{'comentarios':comentarios})
    ##all recupera todos los objetos del modelo (registros de la tabla alumnos)




