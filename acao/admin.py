from django.contrib import admin
from .models import Doacao, Solicitacao, Colaboracao

class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('titulo', 'conteudo',)

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_necessitado',)
    list_filter = ('nome_necessitado',)
    search_fields = ('nome_necessitado',)
class ColaboracaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)

admin.site.register(Doacao, DoacaoAdmin)
admin.site.register(Solicitacao, SolicitacaoAdmin)
admin.site.register(Colaboracao, ColaboracaoAdmin)