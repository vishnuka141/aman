from decimal import Decimal
from django.conf import settings
from product.models import Product

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product):
        product_id= str(product.pk)

        if product_id not in self.cart:
            self.cart[product_id]={'quantity':1,'price':str(product.price)}
        else:
            self.cart[product_id]['quantity'] +=   1
        
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price']= Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def remove(self,pk):
        product_id= str(pk)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        count=0
        for item in self.cart:
            count+= 1
        return count


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


