from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from ..models import Provider

def index(request):

    return render(request, "index.html")

def get_providers(request):

    providers = Provider.objects.all()
    context = {
        "providers": providers
    }

    return render(request, "providers.html", context)

def get_provider(request, pk):
    provider = Provider.objects.get(pk=pk)
    if not provider: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {
        "provider": provider
    }

    return render(request, "provider.html", context)