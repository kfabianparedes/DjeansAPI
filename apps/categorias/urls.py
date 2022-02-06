from django.urls import path
from . import views

urlpatterns = [

    path('categoria-list/', views.ShowAll, name='categoria-list'),
    path('categoria-view/<int:pk>', views.ViewCategoria, name='categoria-view'),
    path('categoria-create/', views.CreateCategoria, name='categoria-create'),
    path('categoria-update/<int:pk>/', views.UpdateCategoria, name='categoria-update'),
    path('categoria-delete/<int:pk>/', views.DeleteCategoria, name='categoria-delete'),

]