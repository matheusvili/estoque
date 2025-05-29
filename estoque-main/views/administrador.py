from rest_framework.viewsets import ModelViewSet
from estoque.models import Administrador
from estoque.serializers.administrador import AdministradorSerializer

class AdministradorViewSet(ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer