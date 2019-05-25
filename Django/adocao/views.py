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

    def get_context_data(self, *args, **kwargs): #metodo utilizado p/ enviar dados ao template
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs) #chama o "pai" para q semper tenha comportamento padrão

        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        return context #devolve/envia o context p/ seu comportamento padrão

class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome", "estado", "descricao"] # quais campos devem aparecer no formulário
    template_name = "adocao/formulariocid.html" # html que será utilizado
    success_url = reverse_lazy("index") # pra onde direcionar o usuario após inserir o registro

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        return context

####################### EDITAR ######################
class EstadoUpdate(UpdateView):
    model = Estado
    fields = ["sigla", "nome"] # quais campos devem aparecer no formulário
    template_name = "adocao/formulario.html" # html que será utilizado
    success_url = reverse_lazy("index") # pra onde direcionar o usuario após inserir o registro

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Estado"
        context['botao'] = "Editar"
        return context

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ["nome", "estado", "descricao"] # quais campos devem aparecer no formulário
    template_name = "adocao/formulariocid.html" # html que será utilizado
    success_url = reverse_lazy("index") # pra onde direcionar o usuario após inserir o registro

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cidade"
        context['botao'] = "Editar"
        return context
