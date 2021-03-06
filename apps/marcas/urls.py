from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.marcas.views.marca_view import MarcaView

router = DefaultRouter()
router.register(r'', MarcaView, basename='marcas')

urlpatterns = router.urls
