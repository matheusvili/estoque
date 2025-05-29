from rest_framework.viewsets import ModelViewSet
from estoque_main.models import Usuario
from estoque_main.serializers.usuario import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
