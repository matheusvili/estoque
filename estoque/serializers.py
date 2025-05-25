from rest_framework.serializers import ModelSerializer
from estoque.models import Categoria, Produto, Usuario, Adiministrador

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
class AdiministradorSerializer(ModelSerializer):
    class Meta:
        model = Adiministrador
        fields = '__all__'