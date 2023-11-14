from django.db import models
from produtos.models import Produto
from clientes.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Order(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    
    quantity = models.IntegerField()
