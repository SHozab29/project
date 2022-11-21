from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from buyPage.views import home

from .models import medical
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

        #if (termsAgreement==True):
        medicalUser = medical.objects.create(medicalName=medicalName,medicalEmail=medicalEmail,medicalPhoneNo=medicalPhoneNo,licenseNo=licenseNo,password=password)

        
        print("Name: " + medicalName)
        print("Email: " + medicalEmail)
        print("PhoneNo.: " + medicalPhoneNo)
        print("LicenseNo.: " + licenseNo)
       
        
        return redirect('/')

    else:
        return render(request,'register.html')

def terms(request):
    return render(request,'terms.html')

def userRegister(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        termsAgreement = request.POST['termsAgreement']

        #if (termsAgreement==True):
        print(username)
        print(first_name)
        print(last_name)

        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        return redirect('/')
    else:
        return render(request,'userRegister.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

