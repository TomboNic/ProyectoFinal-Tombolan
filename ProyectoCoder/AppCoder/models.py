from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class FanFutbol(models.Model):
    Nombre = models.CharField(max_length=15)
    equipo = models.CharField(max_length=15)

    def __str__(self):
        return f"Hincha: {self.Nombre}"

class FanVoley(models.Model):
    Nombre = models.CharField(max_length=15)
    equipo = models.CharField(max_length=15)

    def __str__(self):
        return f"Hincha: {self.Nombre}"

class FanBasquet(models.Model):
    Nombre = models.CharField(max_length=15)
    equipo = models.CharField(max_length=15)

    def __str__(self):
        return f"Hincha: {self.Nombre}"

class FanFormula1(models.Model):
    Nombre = models.CharField(max_length=15)
    escuderia = models.CharField(max_length=15)

    def __str__(self):
        return f"Hincha: {self.Nombre}"