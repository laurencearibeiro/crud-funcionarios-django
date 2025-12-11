from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Funcionario
from django.urls import reverse_lazy 

# Create your views here. - CRUD

# C - Create
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

# R - Read
class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"
    context_object_name = "funcionarios"

# U - Update
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ""__all__""
    template_name = "form_funcionario.html"
