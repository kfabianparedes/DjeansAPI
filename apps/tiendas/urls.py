from django.urls import path
from apps.tiendas.views import TiendaAPIView

urlpatterns = [
    path('lista',TiendaAPIView.as_view(),name='listadoTienda')
]