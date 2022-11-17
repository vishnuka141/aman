from django.shortcuts import render,redirect
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem
# Create your views here.
def check_out(request):
    form = OrderForm()
    cart = Cart(request)

    context = {
        'form':form,
        'cart':cart
    }
    if request.method=='POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order= order,
                    product = item['product'],
                               
                )

            cart.clear()
            return redirect('success')
    return render(request,'checkout/Checkout.html',context)

def success_page(request):
    return render (request,'checkout/success.html')
