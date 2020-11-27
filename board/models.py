from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    writer = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.title