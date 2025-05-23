from rest_framework import viewsets
from estoque.models import Categoria, Produto, Usuario, Adiministrador
from estoque.serializers import CategoriaSerializer, ProdutoSerializer, UsuarioSerializer, AdiministradorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AdiministradorViewSet(viewsets.ModelViewSet):
    queryset = Adiministrador.objects.all()
    serializer_class = AdiministradorSerializer