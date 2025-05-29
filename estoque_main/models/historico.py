from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from .produto import Produto
from .usuario import Usuario
from django.contrib import admin

class Historico(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    acao = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    detalhes = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.acao} - {self.produto.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"
    
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'acao', 'data')
    search_fields = ('produto__nome', 'usuario__nome', 'acao')
    list_filter = ('acao', 'data')

def clean(self):
    if self.data and not isinstance(self.data, datetime):
        raise ValidationError("Data invalida.")
