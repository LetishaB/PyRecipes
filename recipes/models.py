from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Direction(models.Model):
    step = models.TextField()

    def __str__(self):
        return self.step


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/images/', default='static/images/missing.png')
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.ManyToManyField(Direction)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
