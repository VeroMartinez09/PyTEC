from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido a PyTec</h1>")

def temas(request):
    return render(request, 'paginas/temas.html')