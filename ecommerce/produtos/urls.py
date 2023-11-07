from django.urls import path

from produtos.views.produtos_view import HomeView, ProdutoDetail

app_name = 'produtos'

urlpatterns = [
    path('', HomeView.as_view(), name="listar_produtos"),
    path('<int:id>/', ProdutoDetail.as_view(), name="detalhar_produto")
]
