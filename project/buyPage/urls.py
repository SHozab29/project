from django.urls import path
from . import views

urlpatterns =[
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('index',views.index,name='index'),
    path('profile',views.profile,name='profile'),
    #path('',views.add_to_cart,name='add_to_cart')
]