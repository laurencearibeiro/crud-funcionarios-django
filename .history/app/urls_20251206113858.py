from django.urls import path, include


urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view())
]