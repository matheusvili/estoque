from rest_framework.serializers import ModelSerializer
from estoque_main.models import Usuario
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id',)  # Exemplo de campo somente leitura