from django.shortcuts import render

from django.contrib import messages

from produtos.models.produto import Produto

def listar_produtos(request):
    produtos_recentes = Produto.objects.all().order_by('-criado_em')[:4]
    roupas = Produto.objects.filter(categoria__nome='Roupa')
    return render(request, 'listar_produtos.html', 
                  {'produtos_recentes': produtos_recentes,
                   'roupas': roupas})

def detalhar_produto(request, id):
    produto = Produto.objects.get(pk=id)
    return render(request, 'detalhar_produto.html', {'produto': produto})
