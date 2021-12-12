from django.http import HttpResponse
from django.shortcuts import render

def hola(request):
    return HttpResponse("Hola mundo")

# Funciones de Internacionalizacion
def index(request):
    return render(request, "index.html",{})

def about_us(request):
    return render(request, "about.html",)
    
def contact_us(request):
    return render(request, "contact.html",)

def pregunta_frecuente(request):
    return render(request, "frecuente.html",)