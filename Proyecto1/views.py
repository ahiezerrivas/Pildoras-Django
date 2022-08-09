import datetime

from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


class Persona(object):
    
    def __init__(self,nombre,apellido) :
        self.nombre=nombre

        self.apellido=apellido


def saludo(request): #primera vista


    p1=Persona("Profesor Mani", "Diaz" ) 



    # nombre="Juan"

    # apellido="Ramiro"
    temasDelCurso=["Plantillas", "Modelos", "Formularios", "Vistas","Despliegue"]

    ahora=datetime.datetime.now()

    # doc_externo=open("C:/Users/ahiezer/Documents/pildoras informaticas/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    # plt = Template(doc_externo.read())

    # doc_externo.close()

    # doc_externo=loader.get_template

    # ctx= Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temasDelCurso})

    # doc_externo=loader.get_template('miplantilla.html')
    # documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temasDelCurso})
    return render(request, "miplantilla.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas": temasDelCurso} )

def despedida(request): #primera vista
    return HttpResponse("Hasta luegodjango")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()
    return HttpResponse(f'{fecha_actual}')

def calculaEdad(request,edad,ano):
    
    periodo=ano-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años</h2></body><html>" %(ano, edadFutura)

    return HttpResponse(documento)