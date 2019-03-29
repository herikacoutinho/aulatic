from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),

]
