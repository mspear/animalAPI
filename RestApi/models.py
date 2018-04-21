from django.db import models

# Create your models here.
class Animal(models.Model):
    commonName = models.CharField(max_length=30)
    scientificName = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    imageURL = models.URLField()
