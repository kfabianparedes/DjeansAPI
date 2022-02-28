from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ColorAPIView.as_view(), name='list'),
    path('create/', views.ColorAPIView.as_view(), name='create'),
    path('update/<int:pk>/', views.ColorAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ColorAPIView.as_view(), name='delete'),
]