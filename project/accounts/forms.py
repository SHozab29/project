from django import forms
from django.forms import forms


class medical(models.Model):
    medicalName = forms.CharField(label='medicalName',max_length=100)
    medicalEmail: str
    medicalPhoneNo: int64
    licenseNo: str
    password: str
    confirmPassword: str
    termsAgreement: bool