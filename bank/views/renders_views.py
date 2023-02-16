from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from ..models import Provider, Bank
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, "banks/index.html")

@login_required
def get_providers(request):

    providers = Provider.objects.all()
    context = {
        "providers": providers
    }

    return render(request, "banks/providers.html", context)

@login_required
def get_provider(request, pk):
    provider = Provider.objects.get(pk=pk)
    if not provider: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {
        "provider": provider
    }

    return render(request, "banks/provider.html", context)

@login_required
def dashboard(request):
    len_provider = len(Provider.objects.all())
    len_bank = len(Bank.objects.all())

    context = {
        "len_provider": len_provider,
        "len_bank": len_bank
    }

    return render(request, "banks/dashboard.html", context)
