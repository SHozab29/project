from django.shortcuts import render,redirect

# Create your views here.
from index import views

def home(request):
    return render(request, 'buyPage.html',{'price' : 700})

def contact(request):
    return redirect('/#contact')