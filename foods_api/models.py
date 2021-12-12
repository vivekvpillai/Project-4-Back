from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=32)
    calories = models.FloatField()
    image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linked_users = ArrayField(models.IntegerField(), blank=True, default=list)
