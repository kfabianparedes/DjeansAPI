from django.urls import path
from apps.sucursales.views import SucursalAPIView

urlpatterns = [
    path('lista-sucursal',SucursalAPIView.as_view(),name='listaTotalSucursal')
]