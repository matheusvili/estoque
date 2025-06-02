from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from estoque_main.views import AdministradorViewSet, CategoriaViewSet, ProdutoViewSet, UsuarioViewSet, HistoricoViewSet

router = DefaultRouter()
router.register(r'admin', AdministradorViewSet, basename='admin')
router.register(r'categorias', CategoriaViewSet  , basename='categoria')
router.register(r'historicos', HistoricoViewSet, basename='historico')
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/media/', include('uploader.router')),
    path("api/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)