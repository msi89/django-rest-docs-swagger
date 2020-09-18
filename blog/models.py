from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=30)
    picture = models.URLField(null=True)
    created = models.DateTimeField(
        auto_now=True, blank=True, auto_created=True)
