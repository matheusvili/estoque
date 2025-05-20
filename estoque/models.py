from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

def __str__(self):
    return self.descricao


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    RE = models.CharField(max_length=10)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

