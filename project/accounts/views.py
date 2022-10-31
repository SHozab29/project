from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        medicalName = request.POST['medicalName']
        medicalEmail = request.POST['medicalEmail']
        medicalPhoneNo = request.POST['medicalPhoneNo']
        licenseNo = request.POST['licenseNo']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        termsAgreement = request.POST['termsAgreement']
        
        #user = User.objects.create_user()
        return render(request,'login.html')

    else:
        return render(request,'register.html')

def terms(request):
    return render(request,'terms.html')