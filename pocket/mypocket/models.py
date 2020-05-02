from django.db import models

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=50)
    date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.description


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=12)

