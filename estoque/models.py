from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

def __str__(self):
    return self.descricao


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField()
    numero_serie = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateField()



    def __str__(self):
        return self.nome
    

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    RE = models.CharField(max_length=10)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

