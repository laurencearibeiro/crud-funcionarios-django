from django.urls import path, include
from .views import FuncionarioCreateView, FuncionarioListView, FuncionarioUpdateView

urlpatterns = [
    path("form_funcionario/", FuncionarioCreateView.as_view(), name="form_funcionario"),
    path("lista_funcionarios", FuncionarioListView.as_view(), name="lista_funcionarios"),
    path("form_funcionario", FuncionarioUpdateView.as_view(), name="editar_funcionario"),
]