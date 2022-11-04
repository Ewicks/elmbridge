from django.db import models
from .list import get_list


class Word(models.Model):
    word = models.CharField(max_length=200)
   
    def __str__(self):
        return self.word


class Date(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    


