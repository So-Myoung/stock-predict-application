from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self):
        return self.title

