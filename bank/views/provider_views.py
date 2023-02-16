from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ..serializer import ProviderSerializer
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Provider

@api_view(['GET'])
def Api(request):
    api_urls = {
        'Get All Providers': 'provider/',
        'Add': 'provider/create',
        'Update': 'provider/update/(pk)',
        'Delete': 'provider/item/(pk)/delete'
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_providers(request):
    provider = ProviderSerializer(data=request.data)
 
    if Provider.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if provider.is_valid():
        provider.save()
        return Response(provider.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_providers(request):
    providers = Provider.objects.all()
 
    if providers:
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_providers(request, pk):
    provider = Provider.objects.get(pk=pk)
    if not provider: 
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    data = ProviderSerializer(instance=provider, data=request.data, partial=True)
    
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        print(data.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_providers(request, pk):
    provider = get_object_or_404(Provider, pk=pk)
    provider.delete()
    return Response(status=status.HTTP_202_ACCEPTED)