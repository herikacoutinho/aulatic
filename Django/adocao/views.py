from django.shortcuts import render
from django.views.generic import TemplateView

from .models import *
from django.urls import reverse_lazy #chama as urls pelo nome
from django.views.generic.edit import CreateView, UpdateView, DeleteView #importa as classes views para inserir, alterar e deletar

# CRIAR AS VIEWS.
class PaginaInicialView(TemplateView):
    template_name = "adocao/base.html"


class SobreView(TemplateView):
    template_name = "adocao/sobre.html"

class ContatoView(TemplateView):
    template_name = "adocao/contato.html"

class CurriculoView(TemplateView):
    template_name = "adocao/curriculo.html"


class CursosView(TemplateView):
    template_name = "adocao/cursos.html"



####################### INSERIR ######################
class EstadoCreate(CreateView):
    model = Estado
    fields = ["sigla", "nome"] # quais campos devem aparecer no formulário
    template_name = "adocao/formulario.html" # html que será utilizado
    success_url = reverse_lazy("index") # pra onde direcionar o usuario após inserir o registro

#class CidadeCreate(CreateView):
    #model = Cidade
    #fields = ["nome", "estado"]
    #template_name = "form.html"
    #success_url = reverse_lazy("index")
