from django.db import models

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    beak_size = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
