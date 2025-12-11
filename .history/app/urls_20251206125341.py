from django.urls import path, include
from .views import FuncionarioCreateView

urlpatterns = [
    path("form_funcionario/", FuncionarioCreateView.as_view(), name="form_funcionario"),
    path("lista_funcionarios")
]