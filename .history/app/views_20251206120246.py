from django.shortcuts import render
from django.views.generic import CreateView
from .models import Funcionario

# Create your views here.

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reserve