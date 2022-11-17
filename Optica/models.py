from django.db import models

# Create your models here.
class Marcos(models.Model):
    nombre =models.CharField(max_length=50)
    marca =models.CharField(max_length=50)
    precio =models.IntegerField()

class Cristales(models.Model):
    nombre =models.CharField(max_length=50)
    precio =models.IntegerField()

class Liquidos(models.Model):
    nombre =models.CharField(max_length=50)
    marca =models.CharField(max_length=50)
    precio =models.IntegerField()