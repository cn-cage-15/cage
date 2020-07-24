
import datetime
from django.db import models
from django.utils import timezone

class Cryptid(models.Model):
    name                    = models.CharField(max_length=200, unique=True)
    discovery_date          = models.DateField("date discovered")
    cryptid_other_name      = models.CharField(max_length=200, unique=True)
    description             = models.TextField()
    first_mentioned         = models.TextField()


    def __str__(self):
        return self.name

class Location(models.Model):
    cryptid = models.ForeignKey(Cryptid, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name 


