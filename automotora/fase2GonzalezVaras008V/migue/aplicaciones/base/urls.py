from django.urls import path
from .views import Inicio,Listado,FormularioContacto

urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('usados/',Listado.as_view(),{'nombre_categoria':'Usado'}, name = 'usado'),
    path('nuevos/',Listado.as_view(),{'nombre_categoria':'Nuevo'}, name = 'nuevo'),
    path('formulariocontacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),

]