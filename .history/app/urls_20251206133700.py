from django.urls import path, include
from .views import FuncionarioCreateView, FuncionarioListView, Funcio

urlpatterns = [
    path("form_funcionario/", FuncionarioCreateView.as_view(), name="form_funcionario"),
    path("lista_funcionarios", FuncionarioListView.as_view(), name="lista_funcionarios"),
]