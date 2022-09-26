from django.urls import path

from clientes.views.clientes_view import criar_cliente, login_user, logout_user

app_name = 'clientes'

urlpatterns = [
    path('cadastrar/', criar_cliente, name="criar_cliente"),
    path('entrar/', login_user, name="login"),
    path('sair/', logout_user, name="logout"),
]
