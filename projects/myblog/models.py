from datetime import datetime
from django.db import models

# Create your models here.


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.CharField(max_length=100000)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)
