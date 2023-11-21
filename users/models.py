from django.db import models

# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=125, null=False)
    l_name = models.CharField(max_length=125, default='')
    cpf = models.CharField(max_length=11, null=False)
    cep = models.CharField(max_length=8, default='')
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    