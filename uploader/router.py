# uploader/router.py

from django.urls import path
from . import views

urlpatterns = [
    # defina suas rotas aqui, por exemplo:
    path('upload/', views.upload_file, name='upload_file'),
]

router = urlpatterns  # ou outro nome que você use
