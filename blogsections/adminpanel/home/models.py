from django.db import models

# Create your models here.

class Home(models.Model):
    header = models.CharField(max_length=50)
    name = models.TextField(max_length=500)
