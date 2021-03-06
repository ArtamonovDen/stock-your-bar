from django.db import models

# Create your models here.


class Cocktail(models.Model):
    name = models.CharField(max_length=255)
