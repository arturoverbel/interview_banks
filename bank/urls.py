from django.urls import path

from . import views

urlpatterns = [
    path('', views.Api, name='api banks'),
    path('bank/', views.get_banks, name='get-banks'),
    path('bank/create/', views.add_banks, name='add-banks'),
    path('bank/update/<int:pk>/', views.update_banks, name='update-banks'),
    path('bank/delete/<int:pk>/', views.delete_banks, name='delete-items'),
]