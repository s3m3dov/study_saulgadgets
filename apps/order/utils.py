import datetime
import os
from random import randint
from apps.cart.cart import Cart
from apps.order.models import Order, OrderItem

def checkout(request, first_name, last_name, email, phone, address, zipcode, place):
    order = Order(first_name=first_name, last_name=last_name,  email=email, phone=phone, address=address, zipcode=zipcode, place=place)
    # something happens if user is authenticated
    if request.user.is_authenticated:
        order.user = request.user
    # ----
    order.save()
    cart = Cart(request)
    # Add items to OrderItems
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    return order.id