from django.urls import path
from apps.usuarios.views.informacion_usuario import TipoDocumento

urlpatterns = [
    path('tipo-documento', TipoDocumento.as_view(), name='listarTiposDocumentos')
]
