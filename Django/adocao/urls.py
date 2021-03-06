from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo" ),
    path('cursos/', CursosView.as_view(), name="cursos" ),

    #URLS DE CADASTROS
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado" ),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado" ),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado" ),
    path('listar/estados/', EstadoList.as_view(), name="listar-estado"),

    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade" ),
    path('editar/cidade/<int:pk>/',CidadeUpdate.as_view(), name="editar-cidade" ),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade" ),



]
