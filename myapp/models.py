from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class tasklist (models.Model):
    taskname =models.TextField()
    description = models.TextField()
    priority = models.CharField(max_length=20)
    label = models.CharField(max_length=20)
