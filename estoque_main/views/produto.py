from rest_framework.viewsets import ModelViewSet
from estoque_main.models import Produto
from estoque_main.serializers.produto import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
