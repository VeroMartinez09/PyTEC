from django.shortcuts import render
from django.http import HttpResponse
# Aquí se ponen las funciones ruteadoras para mostrar las vistas en el front

def bienvenida(request):
    return HttpResponse("<h1>Bienvenido a PyTec</h1>")

def inicio(request):
    return render(request, 'app/inicio.html')