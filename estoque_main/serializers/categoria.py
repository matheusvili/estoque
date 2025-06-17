from rest_framework.serializers import ModelSerializer
from estoque_main.models import Categoria
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ('id',)  # Exemplo de campo somente leitura