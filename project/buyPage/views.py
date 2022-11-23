from django.shortcuts import render,redirect
from .models import medicines,item_in_cart
# Create your views here.
from index import views


def home(request):
    medicine = medicines()
    medicine.name = "Dolo"
    medicine.price = 400


    if request.method == 'POST':
        quantity = 0
        #item = item_in_cart()

        quantity = quantity + 1

        print(quantity)

        return render(request, 'buyPage.html',{'medicine' : medicine})
    else:
        username = 'shozab'
        return render(request, 'buyPage.html',{'username' : username})

def contact(request):
    return redirect('/#contact')

def index(request):
    return redirect('/#page-top')


#def add_to_cart(request):
   