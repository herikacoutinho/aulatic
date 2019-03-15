from django.shortcuts import render

from django.views.generic import TemplateView



# Create your views here.
class PaginaInicialView(TemplateView):
    template_name = "base.html"


class SobreView(TemplateView):
    template_name = "sobre.html"