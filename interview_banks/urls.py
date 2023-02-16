from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('bank.router.urls_render')),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('bank.router.urls_api')),
]
