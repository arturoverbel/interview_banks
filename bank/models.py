from django.db import models

class Bank(models.Model):
    
    name = models.CharField(
        max_length=50,
        help_text="Nombre del Banco",
    )

    def __str__(self) -> str:
        return self.name