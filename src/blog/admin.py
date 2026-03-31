from django.contrib import admin

# Register your models here.
from blog import models

# admin.site.register(models.Cliente)
# admin.site.register(models.Experiencia)

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre",)

@admin.register(models.Experiencia)
class Experiencia(admin.ModelAdmin):
    list_display = ("cliente", "titulo", "contenido", "fecha_publicacion")
    list_filter = ("cliente", "fecha_publicacion")
    date_hierarchy = "fecha_publicacion"