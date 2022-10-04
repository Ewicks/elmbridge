from django.db import models


class Person(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    age = models.IntegerField(max_length=3)
    email = models.EmailField()

    def __str__(self):
        return self.fname

