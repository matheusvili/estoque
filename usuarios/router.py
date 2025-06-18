from rest_framework.routers import DefaultRouter

from usuario import views

app_name = "usuarios"

router = DefaultRouter()
router.register("usuarios", views.UsuarioViewSet)
