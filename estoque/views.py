from rest_framework import viewsets
from estoque.models import Categoria
from estoque.serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer