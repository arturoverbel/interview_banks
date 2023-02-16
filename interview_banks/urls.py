from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('bank.router.urls_render')),
    path('admin/', admin.site.urls),
    path('api/', include('bank.router.urls_api')),
]
