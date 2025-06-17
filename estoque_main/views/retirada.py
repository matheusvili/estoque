from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from estoque_main.models import Retirada
from estoque_main.serializers import RetiradaSerializer

class RetiradaViewSet(viewsets.ModelViewSet):
    queryset = Retirada.objects.all().prefetch_related('itens__produto', 'usuario')
    serializer_class = RetiradaSerializer
    permission_classes = [IsAuthenticated]

def get_queryset(self):
    user = self.request.user
    if not user.is_authenticated:
        return Retirada.objects.none()  # Nenhum resultado para anônimo
    return self.queryset.filter(usuario=user).order_by('-data')

