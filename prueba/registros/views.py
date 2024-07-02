from django.shortcuts import render
from.models import Alumnos
from.forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son corectos 
            form.save()#inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios':comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos 
    return render(request, 'registros/comentarios.html', {'form': form})


def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/comentarios.html", {'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save()
        comentarios= ComentarioContacto.objects.all()
        return render(request, "registros/comentarios.html", {'comentarios':comentarios})
        #Si el formulario no es valido nos regresa al formulario para verificar
        #datos
    return render(request, "registros/formEditarComentario.html", {'comentario':comentario})    



def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request, "registros/formEditarComentario.html", {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.


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


