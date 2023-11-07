from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from clientes.forms import UserCreateForm

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
