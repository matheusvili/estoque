from rest_framework.viewsets import ModelViewSet
from estoque.models import Historico
from estoque.serializers.historico import HistoricoSerializer

class HistoricoViewSet(ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
