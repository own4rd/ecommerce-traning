from django.db import models

class Categoria(models.Model):
    nome = models.CharField("categoria", max_length=50)

    def __str__(self) -> str:
        return self.nome