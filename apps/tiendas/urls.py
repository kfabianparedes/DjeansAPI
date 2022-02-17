from django.urls import path
from apps.tiendas.views import TiendaAPIView

urlpatterns = [
    path('lista',TiendaAPIView.as_view(),name='listadoTienda'),
    path('crear/',TiendaAPIView.as_view(),name='crearTienda'),
    path('editar/<int:pk>/',TiendaAPIView.as_view(),name='editarTienda'),
    path('eliminar/<int:pk>/',TiendaAPIView.as_view(),name='eliminarTienda')
]