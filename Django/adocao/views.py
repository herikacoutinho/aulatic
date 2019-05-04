from django.shortcuts import render

from django.views.generic import TemplateView



# Create your views here.
class PaginaInicialView(TemplateView):
    template_name = "base.html"


class SobreView(TemplateView):
    template_name = "sobre.html"

class ContatoView(TemplateView):
    template_name = "contato.html"

class CadastroView(TemplateView):
    template_name = "cadastro.html"

class CurriculoView(TemplateView):
    template_name = "curriculo.html"


class CursosView(TemplateView):
    template_name = "cursos.html"
