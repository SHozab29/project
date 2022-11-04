from django.db import models


# Create your models here.

class medical(models.Model):
        medicalName = models.CharField(max_length=50)
        medicalEmail= models.EmailField
        medicalPhoneNo= models.BigIntegerField
        licenseNo = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        termsAgreement = models.BooleanField(default=False)
    
