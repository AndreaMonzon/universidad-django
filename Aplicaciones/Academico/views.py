from email import message
from mailbox import NoSuchMailboxError
from django.shortcuts import render,redirect
from .models import Curso
from django.contrib import messages
# Create your views here.

def home(request):
    cursos_listados= Curso.objects.all()
    messages.success(request,'Cursos listados')
    return render(request,'gestionCursos.html',{'cursos':cursos_listados})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    credito=request.POST['numCredito']

    curso=Curso.objects.create(nombre=nombre,codigo=codigo,creditos=credito)
    messages.success(request,'Cursos registrado')
    return redirect('/')

def eliminarCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'Curso eliminado')
    return redirect('/')



def editarCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request,'editarCurso.html',{'curso':curso})

def edicionCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    credito=request.POST['numCredito']

    curso=Curso.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.credito=credito
    curso.save( )
    messages.success(request,'Curso actualizado')
    return redirect('/')
