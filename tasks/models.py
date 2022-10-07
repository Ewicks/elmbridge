from django.db import models
from web import *


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.cat_name

    # @classmethod
    # def create_from_list(cls):
    #     values_list = my_function()
    #     for value in values_list:
    #         cls.objects.create(cat_name=value)
