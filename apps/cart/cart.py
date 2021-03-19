from django.conf import  settings
from apps.store.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        prod_ids = self.cart.keys()
        prod_clean_ids = []
        for prod_id in prod_ids:
            prod_clean_ids.append(prod_id)
            self.cart[str(prod_id)]['product'] = Product.objects.get(pk=prod_id)
        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])
            yield item 

    def __len__(self):
        # return sum([item['quantity'] for item in self.cart.values()])
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def save(self):
        print('save')
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def get_total_length(self):
        return sum(int(item['quantity']) for item in self.cart.values())
    
    def get_total_cost(self):
        return sum(float(item['total_price']) for item in self.cart.values())