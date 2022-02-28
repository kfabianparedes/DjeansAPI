from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CategoriaAPIView.as_view(), name='list'),
    path('create/', views.CategoriaAPIView.as_view(), name='create'),
    path('update/<int:pk>/', views.CategoriaAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CategoriaAPIView.as_view(), name='delete'),
]