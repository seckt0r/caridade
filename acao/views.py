from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView


class dashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/dashboard.html')

class doacaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/doacao.html')

class solicitacaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/solicitacao.html')

class colaboracaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/colaboracao.html')