from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where RE is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, re, password=None, **extra_fields):
        """
        Cria e salva um usuário com o RE e senha fornecidos.
        """
        if not re:
            raise ValueError(_("O campo RE deve ser preenchido."))
        user = self.model(re=re, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, re, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o RE e senha fornecidos.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("O superusuário precisa ter is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("O superusuário precisa ter is_superuser=True."))

        return self.create_user(re, password, **extra_fields)
