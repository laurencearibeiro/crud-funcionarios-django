from django.urls import path, include
from .views import 

urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view())
]