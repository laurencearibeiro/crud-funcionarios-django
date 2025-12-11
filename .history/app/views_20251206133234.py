from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Funcionario
from django.urls import reverse_lazy 

# Create your views here. - CRUD

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"
    context_object_name = "funcionarios"

