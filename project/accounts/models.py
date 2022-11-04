from django.db import models


# Create your models here.

class medical(models.Model):
        medicalName = models.CharField(max_length=50)
        medicalEmail= models.EmailField()
        medicalPhoneNo= models.BigIntegerField()
        licenseNo = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
    

class handler(models.Model):
        username = models.CharField(max_length=10)
        password = models.CharField(max_length=16)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50) 
        email = models.EmailField()

        