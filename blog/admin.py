from django.contrib import admin
from .models import Artigo, Comentario

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'estado',)
    list_filter = ('estado',)
    search_fields = ('titulo', 'conteudo',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'conteudo',)


admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)