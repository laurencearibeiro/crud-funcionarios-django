from django.urls import path, include
from .views 

urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view())
]