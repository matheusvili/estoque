from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0.0)
    numero_serie = models.CharField(max_length=100)
    # Set default to an integer primary key of an existing Categoria, e.g., 1D
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome
    

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    RE = models.CharField(max_length=10)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

