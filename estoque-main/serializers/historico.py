from rest_framework.serializers import ModelSerializer
from estoque.models import Historico
class HistoricoSerializer(ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'
        read_only_fields = ('id',)  # Exemplo de campo somente leitura