# from django.urls import path
# from apps.sucursales.views import SucursalAPIView
from rest_framework.routers import DefaultRouter
from .views.sucursal_view import SucursalView

router = DefaultRouter()
router.register(r'', SucursalView, basename='sucursales')

urlpatterns = router.urls

# urlpatterns = [
#     path('lista-sucursal/',SucursalAPIView.as_view(),name='listaTotalSucursal'),
#     path('crear/',SucursalAPIView.as_view(),name='crearSucursal'),
#     path('editar/<int:pk>/',SucursalAPIView.as_view(),name='editarSucursal'),
#     path('eliminar/<int:pk>/',SucursalAPIView.as_view(),name='eliminarSucursal')
# ]