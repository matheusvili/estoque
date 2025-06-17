from rest_framework.serializers import ModelSerializer
from estoque_main.models import Produto
class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        read_only_fields = ('id',)  # Exemplo de campo somente leitura