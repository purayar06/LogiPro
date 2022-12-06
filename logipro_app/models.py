from django.db import models


# Create your models here.
class basicDetailsItems(models.Model):
    sno= models.AutoField(primary_key=True)  
    dep = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    event_incharge = models.CharField(max_length=100)
    contact_num = models.IntegerField()
    mail = models.EmailField()
    event_Date=models.DateField()
    
class reqItems(models.Model):
    sno= models.AutoField(primary_key=True)  
    venue=models.CharField(max_length=100)
    micw=models.IntegerField()
    micwl=models.IntegerField()
    speakers=models.IntegerField()
    light=models.IntegerField()
    chair=models.IntegerField()
    Table=models.IntegerField()
    carpet=models.IntegerField()