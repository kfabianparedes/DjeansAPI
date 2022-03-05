from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.usuarios.views.informacion_usuario import TipoDocumento
from apps.usuarios.views.usuario_view import UsuarioView

router = DefaultRouter()
router.register(r'', UsuarioView, basename='usuarios')

urlpatterns = [
    path('tipo-documento', TipoDocumento.as_view(), name='listarTiposDocumentos')
] + router.urls
