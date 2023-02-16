from django.db import models
from django.core.validators import RegexValidator


validate_nit = RegexValidator(r'(^[0-9]{9}-{1}[0-9]{1})', 'Just NIT format is allowed')


class Bank(models.Model):
    
    name = models.CharField(
        max_length=50,
        help_text="Nombre del Banco",
    )

    def __str__(self) -> str:
        return self.name

class Provider(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Nombre del Proveedor",
        null=False,
        blank=False
    )

    nit = models.CharField(
        max_length=11,
        help_text="NIT",
        validators=[validate_nit],
        null=False,
        blank=False
    )

    contact_name = models.CharField(
        max_length=50,
        help_text="Nombre del contacto",
        null=False,
        blank=False
    )

    contact_phone = models.CharField(
        max_length=10,
        help_text="Movil del contacto",
        blank=True, 
        default=''
    )

    bank = models.CharField(
        max_length=15,
        help_text="Nombre del Banco",
        blank=True, 
        default=''
    )

    account_bank = models.CharField(
        max_length=15,
        help_text="Numero de cuenta bancaria",
        blank=True, 
        default=''
    )

    def __str__(self) -> str:
        return self.name