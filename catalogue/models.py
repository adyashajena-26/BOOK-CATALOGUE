from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    pageCount = models.CharField(max_length=100)
    averageRating = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
