from django.urls import path

from ..views import bank_views, provider_views

urlpatterns = [
    path('', bank_views.Api, name='api banks'),
    path('bank/', bank_views.get_banks, name='get-banks'),
    path('bank/create/', bank_views.add_banks, name='add-banks'),
    path('bank/update/<int:pk>/', bank_views.update_banks, name='update-banks'),
    path('bank/delete/<int:pk>/', bank_views.delete_banks, name='delete-items'),

    path('provider/', provider_views.get_providers, name='get-providers'),
    path('provider/create/', provider_views.add_providers, name='add-providers'),
    path('provider/update/<int:pk>/', provider_views.update_providers, name='update-providers'),
    path('provider/delete/<int:pk>/', provider_views.delete_providers, name='delete-items'),
]