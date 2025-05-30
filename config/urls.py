from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

from estoque.views import CategoriaViewSet, ProdutoViewSet, UsuarioViewSet, AdiministradorViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet  , basename='categoria')
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'admin', AdiministradorViewSet, basename='admin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

