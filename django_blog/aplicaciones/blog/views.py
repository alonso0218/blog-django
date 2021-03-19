from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def home (request):
    queryset= request.GET.get ("buscar")
    posts= Post.objects.filter(estado=True)
    if queryset:
        posts=Post.objects.filter(
              Q(titulo__icontains = queryset) |
              Q(descripcion__icontains = queryset)
        ).distinct()
   
    paginator=Paginator(posts,2) 
    page=request.GET.get("page")
    posts=paginator.get_page(page)

    return render(request,'index.html',{'posts':posts})


def detallePost(request,slug):
    post=get_object_or_404 (Post,slug=slug)
    return render(request,"post.html",{'detalle_post':post})

def nosotros(request):
    queryset = request.GET.get("buscar")
    posts= Post.objects.filter(
        estado=True,
        Categoria=Categoria.objects.get(nombre__iexatc='nosotros')
    )
    if queryset:
       posts= Post.objects.filter( 
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
              estado=True,
              categoria=Categoria.objects.get(nombre__iexatc="nosotros"),
        ).distinct()

    paginator=Paginator(posts,2) 
    page=request.GET.get("page")
    posts=paginator.get_page(page)

    return render(request,"nosotros.html",{'posts':posts})
    

def programacion(request):
    queryset = request.GET.get("buscar")
    posts= Post.objects.filter(
      estado=True ,
      Categoria=Categoria.objects.get(nombre='programacion')
    )
    if queryset:
       posts= Post.objects.filter( 
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
              estado=True,
              categoria=Categoria.objects.get(nombre__iexatc="programacion"),
        ).distinct()
    paginator=Paginator(posts,2) 
    page=request.GET.get("page")
    posts=paginator.get_page(page)

    return render(request,"programacion.html",{'posts':posts})
    

def tegnologia(request):
    queryset = request.GET.get("buscar")
    posts= Post.objects.filter(
      estado=True ,
      Categoria=Categoria.objects.get(nombre='tegnologia')
    )
    if queryset:
       posts= Post.objects.filter( 
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
              estado=True,
              categoria=Categoria.objects.get(nombre__iexatc="tegnologia"),
        ).distinct()
    paginator=Paginator(posts,2) 
    page=request.GET.get("page")
    posts=paginator.get_page(page)

    return render(request,"tegnologia.html",{'posts':posts})
    

def video_juegos(request):
    queryset=request.GET.get("buscar")
    posts= Post.objects.filter(
      estado=True ,
      Categoria=Categoria.objects.get(nombre='video juegos')
    )
    if queryset:
       posts= Post.objects.filter( 
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
              estado=True,
              categoria=Categoria.objects.get(nombre__iexatc="video juegos"),
        ).distinct()
    paginator=Paginator(posts,2) 
    page=request.GET.get("page")
    posts=paginator.get_page(page)

    return render(request,"videojuegos.html",{'posts':posts})
 