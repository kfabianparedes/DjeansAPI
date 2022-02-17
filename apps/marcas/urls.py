from django.urls import path

from apps.marcas.views import MarcaAPIView

urlpatterns = [
    path('lista/',MarcaAPIView.as_view(),name='listaTotalMarca'),
    path('crear/',MarcaAPIView.as_view(),name='crearMarca'),
    path('editar/<int:pk>/',MarcaAPIView.as_view(),name='editarMarca'),
    path('eliminar/<int:pk>/',MarcaAPIView.as_view(),name='eliminarMarca')
]