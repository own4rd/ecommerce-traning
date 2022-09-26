from django.shortcuts import render

from django.contrib import messages

from produtos.models.produto import Produto

def listar_produtos(request):
    produtos = Produto.objects.all().order_by('-criado_em')[:4]
    return render(request, 'listar_produtos.html', {'produtos': produtos})