from django.contrib import admin
from .models import Artigo

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'estado',)
    list_filter = ('estado',)
    search_fields = ('titulo', 'conteudo',)

admin.site.register(Artigo, ArtigoAdmin)