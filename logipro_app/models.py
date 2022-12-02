from django.db import models


# Create your models here.
class logiProItems(models.Model):
    user = models.CharField(max_length=100)
    