from rest_framework.serializers import ModelSerializer
from estoque_main.models import Administrador 

class AdministradorSerializer(ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'
        read_only_fields = ('id',)  # Exemplo de campo somente leitura