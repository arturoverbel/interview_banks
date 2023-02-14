from django.test import TestCase
from bank.models import Bank

class BankTestCase(TestCase):
    def setUp(self):
        Bank.objects.create(name="BBVA")
        Bank.objects.create(name="Scotiabank")

    def test_get_banks(self):
        banks = Bank.objects.all()
        self.assertEqual(len(banks), 2)

