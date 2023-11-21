from django.db import models

# Create your models here.

RECYCLING_TYPE_CHOICES = (
    ('Papel', 'Papel'),
    ('Plastico', 'Plastico'),
    ('Vidro', 'Vidro'),
    ('Metal', 'Metal'),
    ('Organico', 'Organico')
)

class Recycle(models.Model):
    quantity = models.CharField(max_length=20, null=False)
    type = models.CharField(max_length=13, choices=RECYCLING_TYPE_CHOICES, null=False)
    ecopoint = models.CharField(max_length=5, null=False)