from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .serializer import BankSerializer
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Bank

@api_view(['GET'])
def Api(request):
    api_urls = {
        'Get All Banks': 'bank/',
        'Add': 'bank/create',
        'Update': 'bank/update/(pk)',
        'Delete': 'bank/item/(pk)/delete'
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_banks(request):
    bank = BankSerializer(data=request.data)
 
    if Bank.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if bank.is_valid():
        bank.save()
        return Response(bank.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_banks(request):
    banks = Bank.objects.all()
 
    if banks:
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_banks(request, pk):
    bank = Bank.objects.get(pk=pk)
    data = BankSerializer(instance=bank, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_banks(request, pk):
    bank = get_object_or_404(Bank, pk=pk)
    bank.delete()
    return Response(status=status.HTTP_202_ACCEPTED)