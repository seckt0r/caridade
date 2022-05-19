from tkinter.messagebox import ABORTRETRYIGNORE
from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView
from .models import artigo

class blogListView(ListView):
    model = artigo
    template = 'blog/artigo_list.html'
