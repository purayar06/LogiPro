from django.db import models


# Create your models here.
class logiProItems(models.Model):
    user = models.CharField(max_length=100)
    
class RegItems(models.Model):
    sno= models.AutoField(primary_key=True)  
    venue=models.CharField(max_length=100)
    event_Date=models.DateField()
    micw=models.IntegerField()
    micwl=models.IntegerField()
    speakers=models.IntegerField()
    light=models.IntegerField()
    chair=models.IntegerField()
    Table=models.IntegerField()