from django.db import models

# Create your models here.
class Material(models.Model):
    Name = models.CharField(max_length=20)
    allow_stress = models.FloatField()
    elasticity = models.FloatField()

    def __str__(self):
        return self.title
