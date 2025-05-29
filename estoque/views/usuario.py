from rest_framework.viewsets import ModelViewSet
from estoque.models import Usuario
from estoque.serializers.usuario import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
