from django.db import models

# Create your models here.
class ComputerScienceModel(models.Model):
    Name = models.CharField(max_length=25)
    Age = models.IntegerField()
    Email = models.EmailField()
    Mobile = models.BigIntegerField()

