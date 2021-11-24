from django.db import models

# Create your models here.
class Hinchas(models.Model):
    es_o_no = models.CharField(max_length=6)

class HinchasDeVelez(models.Model):
    Cant_hinchas = models.IntegerField()
    Equipo = models.CharField(max_length=15)

class HinchasDeBoca(models.Model):
    Cant_hinchas = models.IntegerField()
    Equipo = models.CharField(max_length=15)

class HinchasDeRiber(models.Model):
    Cant_hinchas = models.IntegerField()
    Equipo = models.CharField(max_length=15)