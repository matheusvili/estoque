from django.db import models
from .usuario import Usuario

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    RE = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # armazenar senha hasheada, mas aqui campo direto

    def __str__(self):
        return self.nome

class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = ["nome"]