from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ModeloAPIView.as_view(), name='list'),
    path('create/', views.ModeloAPIView.as_view(), name='create'),
    path('update/<int:pk>/', views.ModeloAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ModeloAPIView.as_view(), name='delete'),
]