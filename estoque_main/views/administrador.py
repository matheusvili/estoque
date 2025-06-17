from rest_framework.viewsets import ModelViewSet
from estoque_main.models import Administrador
from estoque_main.serializers.administrador import AdministradorSerializer

class AdministradorViewSet(ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer