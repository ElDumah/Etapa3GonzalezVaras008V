import random
from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.paginator import Paginator
from .models import Post,Categoria,RedesSociales,Web
from .utils import *
from .forms import ContactoForm


class Inicio(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        try:
            post_usado = Post.objects.filter(
                         estado = True,
                         publicado = True,
                         categoria = Categoria.objects.get(nombre = 'Usado')
                         ).latest('fecha_publicacion')
        except:
            post_usado = None
        
        try:
            post_nuevo = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'Nuevo')
                            ).latest('fecha_publicacion')
        except:
            post_nuevo = None
        
        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_usado': post_usado,
            'post_nuevo': post_nuevo,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),

        }

        return render(request,'index.html',contexto)

class Listado(ListView):

 def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'categoria.html',contexto)

class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,

        }
        return render (request,'contacto.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:index')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto)     

