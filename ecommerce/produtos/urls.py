from django.urls import path

from produtos.views.produtos_view import listar_produtos

app_name = 'produtos'

urlpatterns = [
    path('', listar_produtos, name="listar_produtos"),
]
