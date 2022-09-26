from django.contrib import admin

from produtos.models.categoria import Categoria
from produtos.models.produto import Produto

admin.site.register(Categoria)
admin.site.register(Produto)