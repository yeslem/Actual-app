from django.db import models
from django import forms

# Create your models here.
class Material(models.Model):
    Name = models.CharField(max_length=20)
    allow_stress = models.FloatField(default=0)
    elasticity = models.FloatField(default=0)

    def __str__(self):
        return self.Name

class Head(models.Model):
    Name = models.CharField(max_length=20)
    Constant = models.FloatField(default=0)

    def __str__(self):
        return self.Name
