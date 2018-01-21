from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)


class Direction(models.Model):
    step = models.TextField()


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/', default='static/images/missing.png')
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.ManyToManyField(Direction)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
