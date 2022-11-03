from django.db import models
from .list import get_list

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Word(models.Model):
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name


class Date(models.Model):
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    
    # def __str__(self):
    #     return self.name


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.cat_name

    @classmethod
    def create_from_list(cls):
        values_list = get_list()
        for value in values_list:
            cls.objects.create(cat_name=value)
