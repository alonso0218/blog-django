from django.urls import path
from .views import *



urlpatterns = [
    path("",home,name='index'),
    path("nosotros/",nosotros,name='nosotros'),
    path("tegnologia/",tegnologia,name='tegnologia'),
    path("programacion/",programacion,name='programacion'),
    path("videojuegos/",video_juegos,name='videojuegos'),
    path("<slug:slug>/",detallePost,name='detalle_post')
]
