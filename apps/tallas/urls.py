from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TallaAPIView.as_view(), name='list'),
    path('create/', views.TallaAPIView.as_view(), name='create'),
    path('update/<int:pk>/', views.TallaAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TallaAPIView.as_view(), name='delete'),
]