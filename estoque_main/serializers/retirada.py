from rest_framework import serializers
from estoque_main.models import Retirada, ItemRetirada
from usuarios.models import Usuario
from estoque_main.serializers.itemRetirada import ItemRetiradaSerializer

class RetiradaSerializer(serializers.ModelSerializer):
    itens = ItemRetiradaSerializer(many=True)  # nested write
    usuario_nome = serializers.CharField(source="usuario.nome", read_only=True)

    class Meta:
        model = Retirada
        fields = '__all__'

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        retirada = Retirada.objects.create(**validated_data)
        for item_data in itens_data:
            ItemRetirada.objects.create(retirada=retirada, **item_data)
        return retirada

    def update(self, instance, validated_data):
        itens_data = validated_data.pop('itens', None)

        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if itens_data is not None:
            instance.itens.all().delete()
            for item_data in itens_data:
                ItemRetirada.objects.create(retirada=instance, **item_data)

        return instance
