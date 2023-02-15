from django.test import TestCase
from bank.models import Bank
import json
from rest_framework.test import APIRequestFactory

from rest_framework.test import APIClient
from rest_framework import status

class BankTestCase(TestCase):
    def setUp(self):
        Bank.objects.create(name="BBVA")
        Bank.objects.create(name="Scotiabank")

    def test_get_banks(self):
        banks = Bank.objects.all()
        self.assertEqual(len(banks), 2)

class BankAPITestCase(TestCase):

    def setUp(self):

        Bank(name='myBank').save()
        Bank(name='otherBank').save()

    def test_create_bank(self):

        client = APIClient()
        newNameBank = 'newBank'

        response = client.post(
            '/api/bank/create/',
            { 'name': newNameBank },
            format='json'
        )

        result = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['name'], newNameBank)

    def test_get_bank(self):

        client = APIClient()

        response = client.get('/api/bank/')

        result = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

    def test_update_bank(self):

        client = APIClient()
        newName = 'ThisIsTheNewName'

        response = client.put(
            '/api/bank/update/1/', 
            { 'name': newName },
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['name'], newName)
    
    def test_delete_bank(self):

        client = APIClient()

        response = client.delete(
            '/api/bank/delete/1/', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        bank_exists = Bank.objects.filter(pk=1)
        self.assertFalse(bank_exists)