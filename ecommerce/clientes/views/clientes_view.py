from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from clientes.forms import UserCreateForm
from clientes.models import User
from django.http import Http404

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, "Usuário e senha inválidos")
        return super().form_invalid(form)


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'criar_cliente.html'
    success_url = '/'
    success_message = "Usuário Criado!"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['email']
    template_name = 'atualizar_cliente.html'
    success_url = '/'    

    def get_object(self, *args, **kwargs):
        user = super().get_object(*args, **kwargs)
        if not user.pk == self.request.user.pk:
            raise Http404
        return user
