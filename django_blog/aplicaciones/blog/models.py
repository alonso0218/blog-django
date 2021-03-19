from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Categoria(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField("nombre de la categoria", max_length=100,null=False,blank=False)
    estado = models.BooleanField("Categori activa /Categoria no activia,",default=True)
    fecha_creacion=models.DateField("fecha de creacion",auto_now_add=True)

    def __str__(self):
        return self.nombre
    

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"


class Autor(models.Model):
    id=models.AutoField(primary_key=True)
    nombres=models.CharField("nombres de autor",max_length=200,null=False,blank=False)
    apellidos=models.CharField("apellidos de autor",max_length=200,null=False,blank=False)
    facebook=models.URLField("facebook",null=True,blank=True)
    instagram=models.URLField("instagram",null=True,blank=True)
    twiter=models.URLField("twiter",null=True,blank=True)
    correo=models.EmailField("correo electronico",null=False,blank=False)
    estado=models.BooleanField("autor activo/no activo",default=True)
    fecha_creacion= models.DateField("fecha de creacion", auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{0},{1}".format (self.apellidos,self.nombres)
    

    class Meta:
        verbose_name="autor"
        verbose_name_plural="autores"




class Post(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField("Titulo", max_length=90,blank=False,null=False)
    slug=models.CharField("Slug", max_length=100,blank=False,null=False)
    descripcion=models.CharField("Descripcion",max_length=120,blank=False,null=False)
    contenido=RichTextField("contenido del post")
    imagen=models.URLField(max_length=255,blank=False,null=False)#lo hacemos con url para poder renderizar las imagenes desde internet por que las subimos a   heroku  y no podemos almacenar imagenes 
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    Categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado=models.BooleanField("publicado/no publicado",default=True)
    fecha_creacion=models.DateField("fecha de creacion ",auto_now=False ,auto_now_add=True)


    class Meta:

        verbose_name="post"
        verbose_name_plural="posts"
        
    def __str__(self):
        return self.titulo
    