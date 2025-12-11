from django.urls import path, include
from .views import Fun

urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view())
]