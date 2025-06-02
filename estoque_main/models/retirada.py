from django.db import models
from usuario.models import Usuario

class Retirada(models.Model):
    class StatusRetirada(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        CONFIRMADO = 3, "Confirmado"
        RETIRADO = 4, "Retirado"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="retiradas" )
    status = models.IntegerField(choices=StatusRetirada.choices, default=StatusRetirada.CARRINHO)