from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

from produtos.models.produto import Produto

class HomeView(ListView):
    queryset = Produto.objects.all().order_by('-criado_em')[:4]
    context_object_name = 'produtos_recentes'
    template_name = 'listar_produtos.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['roupas'] = Produto.objects.filter(categoria__nome='Roupa')
        return context

class ProdutoDetail(DetailView):
    model = Produto
    template_name = 'detalhar_produto.html'
    context_object_name = 'produto'
    pk_url_kwarg = 'id'
