from django.db import models

from produtos.models.categoria import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome