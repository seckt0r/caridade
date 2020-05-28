from django.shortcuts import render
from django.views.generic import View


class dashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'acao/dashboard.html')
