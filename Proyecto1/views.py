from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("Hola alumnos esta es nuestra primera pagina don django")