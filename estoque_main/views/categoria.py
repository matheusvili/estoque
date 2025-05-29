from rest_framework.viewsets import ModelViewSet
from estoque_main.models import Categoria
from estoque_main.serializers.categoria import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
