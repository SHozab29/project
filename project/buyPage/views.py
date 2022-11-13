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
        return render(request, 'buyPage.html',{'medicine' : medicine})

def contact(request):
    return redirect('/#contact')


#def add_to_cart(request):
   