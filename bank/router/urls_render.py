from django.urls import path

from ..views import renders_views
urlpatterns = [
    path('', renders_views.index, name='render-index'),
    path('dashboard/', renders_views.dashboard, name='get-dashboard'),
    path('providers/', renders_views.get_providers, name='get-render-providers'),
    path('provider/<int:pk>/', renders_views.get_provider, name='get-render-provider'),
]