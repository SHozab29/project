from django.db import models

# Create your models here.

class medicines:
    name : str
    img : str
    price : str


class item_in_cart:
    name : str
    price: int
    quantity = 0