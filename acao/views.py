from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView


class dashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/dashboard.html')

class colaboradoresView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/colaboradores.html')