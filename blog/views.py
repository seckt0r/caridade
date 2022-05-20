from tkinter.messagebox import ABORTRETRYIGNORE
from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView, DetailView
from .models import Artigo

class blogListView(ListView):
    model = Artigo
    queryset = Artigo.objects.filter(estado=1).order_by('-criado_em')
    template = 'blog/artigo_list.html'

class blogDetailView(DetailView):
    model = Artigo
    template_name='blog/artigo_detail.html'