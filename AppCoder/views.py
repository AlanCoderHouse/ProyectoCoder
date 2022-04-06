from django.http import HttpResponse
from django.shortcuts import render

from .models import Curso

# Create your views here.


def curso(request, nombre, camada):  #No olvidarse de importar
    mi_curso = Curso(nombre=nombre, camada=camada)
    mi_curso.save() #comando para que invoque y guarde en la BBDD.
    
    return HttpResponse(f'Se genero el curso de {mi_curso.nombre} con la camada {mi_curso.camada}')
