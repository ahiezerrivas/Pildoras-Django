import datetime

from django.http import HttpResponse
from django.template import Template, Context


class Persona(object):
    
    def __init__(self,nombre,apellido) :
        self.nombre=nombre

        self.apellido=apellido


def saludo(request): #primera vista


    p1=Persona(" Profesor Juan", "Diaz" ) 



    # nombre="Juan"

    # apellido="Ramiro"

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/ahiezer/Documents/pildoras informaticas/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx= Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora})

    documento=plt.render(ctx)
    return HttpResponse(documento)

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