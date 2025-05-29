from rest_framework.viewsets import ModelViewSet
from estoque.models import Categoria
from estoque.serializers.categoria import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
