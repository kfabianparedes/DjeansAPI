from django.urls import path
from apps.sucursales.views import SucursalAPIView

urlpatterns = [
    path('lista-sucursal/',SucursalAPIView.as_view(),name='listaTotalSucursal'),
    path('crear/',SucursalAPIView.as_view(),name='crearSucursal'),
    path('editar/<int:pk>/',SucursalAPIView.as_view(),name='editarSucursal'),
    path('eliminar/<int:pk>/',SucursalAPIView.as_view(),name='eliminarSucursal')
]