from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('temas', views.temas, name='temas'),
]