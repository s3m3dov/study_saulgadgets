from django.shortcuts import render
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    productstring = ""
    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'])
        # Learn this type of writing
        productstring += b

    context = {
        'cart': cart,
        'productstring': productstring
    }
    return render(request, 'cart.html', context)
