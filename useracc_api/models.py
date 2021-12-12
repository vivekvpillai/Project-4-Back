from django.db import models
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    user_foods = ArrayField(models.IntegerField(), default=list)
