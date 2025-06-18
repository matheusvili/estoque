from django.contrib.auth.backends import ModelBackend
from .models import Usuario  # Ajuste se estiver em outro app

class REBackend(ModelBackend):
    def authenticate(self, request, re=None, password=None, **kwargs):
        if re is None or password is None:
            return None

        try:
            user = Usuario.objects.get(re=re)
        except Usuario.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
