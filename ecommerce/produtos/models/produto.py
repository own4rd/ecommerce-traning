from django.db import models

from produtos.models.categoria import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=10 ,decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.nome
    
    def discounted_price(self):
        discounted = self.preco - (self.preco * (self.discount / 100))
        return round(discounted, 2)
