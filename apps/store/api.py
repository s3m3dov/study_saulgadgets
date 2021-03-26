import json, stripe
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect

from apps.cart.cart import Cart
from apps.order.utils import checkout
from .models import Product
from apps.order.models import Order
from apps.coupon.models import Coupon

def create_checkout_session(request):
    data = json.loads(request.body)
    # Coupon
    coupon_code = data['coupon_code']
    coupon_value = 0
    if coupon_code != "":
        coupon = Coupon.objects.get(code=coupon_code)
        if coupon.can_use():
            coupon_value = coupon.value
            coupon.use()
    # Cart & Checkout
    cart = Cart(request)
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    items = []
    for item in cart:
        product = item['product']
        price = int(float(product.price) * 100) 
        if coupon_value > 0:
            price = int(price * (int(coupon_value) / 100))
        obj = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.title,
                },
                'unit_amount': price,
            },
            'quantity': item['quantity']
        }
        items.append(obj)

    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = items,
        mode = 'payment',
        success_url = 'http://127.0.0.1:8000/cart/success/',
        cancel_url = 'http://127.0.0.1:8000/cart/'
    )
    # Create Order
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']
    payment_intent = session.payment_intent
    order_id = checkout(request, first_name, last_name, email, address, zipcode, place)
    total_price = 0.00
    for item in cart:
        product = item['product']
        total_price += (float(product.price) * int(item['quantity']))
    paid = True
    if coupon_value > 0:
        total_price *= coupon_value / 100
    order = Order.objects.get(pk=order_id)
    order.payment_intent = payment_intent
    order.paid_amount = cart.get_total_cost()
    order.used_coupon = coupon_code
    order.save()
    cart.clear()
    return JsonResponse({'session': session})

def api_checkout(request):
    cart = Cart(request)
    data = json.loads(request.body)
    json_response = {'success': True}
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    phone = data['phone']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']
    #--------------------
    order_id = checkout(request, first_name, last_name, email, phone, address, zipcode, place)
    total_price = 0.00
    for item in cart:
        product = item['product']
        total_price += (float(product.price) * int(item['quantity']))
    paid = True
    if paid == True:
        order = Order.objects.get(pk=order_id)
        order.paid = True
        order.paid_amount = cart.get_total_cost()
        order.save()
        
    return JsonResponse(json_response)

def api_add_to_cart(request):
    data = json.loads(request.body)
    json_response = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    # Print request and product.name
    print(product)
    print(request.body)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    return JsonResponse(json_response)


def api_remove_from_cart(request):
    data = json.loads(request.body)
    json_response = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(json_response)
