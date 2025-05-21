from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from estoque.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet  , basename='categoria')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]