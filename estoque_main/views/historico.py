from rest_framework.viewsets import ModelViewSet
from estoque_main.models import Historico
from estoque_main.serializers.historico import HistoricoSerializer

class HistoricoViewSet(ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
