from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bienvenida(request):
    return HttpResponse("<h1>Bienvenido a PyTec</h1>")

def inicio(request):
    return render(request, 'app/inicio.html')