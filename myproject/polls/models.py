
import datetime
from django.db import models
from django.utils import timezone

class Cryptid(models.Model):
    name            = models.CharField(max_length=200, unique=True)
    pub_date                = models.DateTimeField("date published")
    cryptid_other_name      = models.CharField(max_length=200, unique=True)
    description             = models.TextField()
    first_mentioned         = models.TextField()


    def __str__(self):
        return self.name

    @property
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Location(models.Model):
    cryptid = models.ForeignKey(Cryptid, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name 




