from django.db import models
from .categoria import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    quantidade = models.PositiveIntegerField(null=True, blank=True)
    numero_serie = models.CharField(max_length=100, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_cadastro = models.DateTimeField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')

    def __str__(self):
        return self.nome
