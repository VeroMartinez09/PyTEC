from django.urls import path
from . import views
# paths para ruteo de la APLICACIÓN

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('inicio', views.inicio, name='inicio'),
]