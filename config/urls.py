from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from estoque.views import CategoriaViewSet, ProdutoViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet  , basename='categoria')
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

