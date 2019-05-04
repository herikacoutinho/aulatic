from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('cadastro/', CadastroView.as_view(), name="cadastro"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo" ),
    path('cursos/', CursosView.as_view(), name="cursos" )

]
