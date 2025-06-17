from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UploadFileView

router = DefaultRouter()

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
]
