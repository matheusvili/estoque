from django.db import models
from usuario.models import Usuario
from .produto import Produto  

class Retirada(models.Model):
    class StatusRetirada(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        CONFIRMADO = 3, "Confirmado"
        RETIRADO = 4, "Retirado"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="retiradas")
    status = models.IntegerField(choices=StatusRetirada.choices, default=StatusRetirada.CARRINHO)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Retirada #{self.id} - {self.usuario.nome}"


class ItemRetirada(models.Model):
    retirada = models.ForeignKey(Retirada, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Retirada #{self.retirada.id})"
