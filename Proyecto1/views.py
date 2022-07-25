import datetime
from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("Hola alumnos esta es nuestra primera pagina don django")

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