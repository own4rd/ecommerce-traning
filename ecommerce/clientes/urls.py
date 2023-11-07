from django.urls import path
from django.contrib.auth.views import LogoutView

from clientes.views.clientes_view import UserCreateView, UserLoginView


app_name = 'clientes'

urlpatterns = [
    path('cadastrar/', UserCreateView.as_view(), name="criar_cliente"),
    path('entrar/', UserLoginView.as_view(), name="login"),
    path('sair/', LogoutView.as_view(next_page='/'), name="logout"),
]
