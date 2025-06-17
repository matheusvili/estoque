from rest_framework import serializers
from estoque_main.models import ItemRetirada
from estoque_main.models import Produto

class ItemRetiradaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source="produto.nome", read_only=True)

    class Meta:
        model = ItemRetirada
        fields = ['id', 'produto', 'produto_nome', 'quantidade']
