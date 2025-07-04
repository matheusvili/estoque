from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from estoque_main.models import Retirada, Produto
from estoque_main.serializers import RetiradaSerializer
from rest_framework.response import Response
from rest_framework import status

class RetiradaViewSet(viewsets.ModelViewSet):
    queryset = Retirada.objects.all().prefetch_related('itens__produto', 'usuario')
    serializer_class = RetiradaSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Retirada.objects.none()
        return self.queryset.filter(usuario=user).order_by('-data')

    def perform_create(self, serializer):
        retirada = serializer.save()

        for item in self.request.data.get('itens', []):
            produto_id = item['produto']
            quantidade = item['quantidade']

            try:
                produto = Produto.objects.get(id=produto_id)
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    produto.save()
                else:
                    raise ValueError(f'Estoque insuficiente para {produto.nome}')
            except Produto.DoesNotExist:
                raise ValueError(f'Produto com ID {produto_id} não encontrado')
