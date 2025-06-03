from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    RE = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Armazena senha hash

    def __str__(self):
        return self.nome
class Meta:
    verbose_name = "Usuário"
    verbose_name_plural = "Usuários"
    ordering = ["nome"]