from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class FanFutbol(models.Model):
    Nombre = models.CharField(max_length=15)
    es_o_no =  BooleanField()
    equipo = models.CharField(max_length=15)

class FanVoley(models.Model):
    Nombre = models.CharField(max_length=15)
    es_o_no = BooleanField()
    Equipo = models.CharField(max_length=15)

class FanBasquet(models.Model):
    Nombre = models.CharField(max_length=15)
    es_o_no = BooleanField()
    Equipo = models.CharField(max_length=15)

class FanFormula1(models.Model):
    Nombre = models.CharField(max_length=15)
    es_o_no = BooleanField()
    Escuderia = models.CharField(max_length=15)