# from django.urls import path
# from apps.tiendas.views import TiendaAPIView

# urlpatterns = [
#     path('lista',TiendaAPIView.as_view(),name='listadoTienda'),
#     path('crear/',TiendaAPIView.as_view(),name='crearTienda'),
#     path('editar/<int:pk>/',TiendaAPIView.as_view(),name='editarTienda'),
#     path('eliminar/<int:pk>/',TiendaAPIView.as_view(),name='eliminarTienda')
# ]

from rest_framework.routers import DefaultRouter
from .views.tienda_view import TiendaView

router = DefaultRouter()
router.register(r'', TiendaView, basename='tiendas')

urlpatterns = router.urls