from django.contrib import admin
from .models import *
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class CategoriaResoruce(resources.ModelResource):


    class Meta:
        model= Categoria





class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):#recibe 2 herencias esta clase 
    search_fields=["nombre"]
    list_display=('nombre','estado','fecha_creacion',)#con esto campos modificamos la admin django
    resource_class=CategoriaResoruce


class AutorResource(resources.ModelResource):

    class Meta:
        model= Autor

class AutorAdmin(admin.ModelAdmin):
    search_fields=["nombres","apellidos","correo",]
    list_display=('nombres','apellidos','correo','estado','fecha_creacion',)




admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post)