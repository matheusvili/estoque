from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = None  # Desativa o campo padrão username
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    re = models.CharField(max_length=20, unique=True, verbose_name="RE")  # Usado como login
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )

    USERNAME_FIELD = "re"              # <- AUTENTICAÇÃO AGORA POR RE
    REQUIRED_FIELDS = []              # <- nenhum campo obrigatório além de senha e RE
    EMAIL_FIELD = "email"             # <- usado em reset de senha por e-mail (opcional)

    objects = CustomUserManager()

    def __str__(self):
        return self.re  # Exibe RE como representação do usuário

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
