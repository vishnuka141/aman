from django.shortcuts import get_object_or_404, render,redirect
from .cart import Cart
from product.models import Product
# Create your views here.
def cart(request):
    cart=Cart(request)
    return render(request,'cart/cart.html',{'cart':cart})

def cart_add(request,pk):
    cart = Cart(request)
    product=get_object_or_404(Product,pk=pk)
    cart.add(product=product)
    return redirect('cart')

def cart_remove(request,pk):
    cart = Cart(request)
    cart.remove(pk)
    return redirect('cart')

def quantity_update(request):
    if request.method == 'POST':
        quantity=request.POST.get('qty88')
        cart=Cart(request)
        cart=quantity
        for i in cart:
            print(i,'================')
       
        
        return redirect('check_out')