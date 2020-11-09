from django.urls import path
from .views import Inicio,Listado,FormularioContacto

urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('usados/',Listado.as_view(),{'nombre_categoria':'Usado'}, name = 'usado'),
    path('nuevos/',Listado.as_view(),{'nombre_categoria':'Nuevo'}, name = 'nuevo'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
 ##   path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
]