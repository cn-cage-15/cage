import datetime
from django.db import models
from django.utils import timezone 

class Cryptid(models.Model):
    cryptid_text            = models.CharField(max_length=200, unique=True)
    pub_date                = models.DateTimeField("date published")
    cryptid_name            = models.TextField()
    cryptid_other_name      = models.TextField()
    description             = models.TextField()
    cryptid_location        = models.TextField()

    def __str__(self):
        return self.cryptid_text

    @property
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Location(models.Model):
    cryptid = models.ForeignKey(Cryptid, on_delete=models.CASCADE)
    location_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.location_text 


