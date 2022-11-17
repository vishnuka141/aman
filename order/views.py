from django.shortcuts import render
from checkout.models import  Order,OrderItem

# Create your views here.
def order(request):
    orders= Order.objects.filter(user=request.user)
    return render(request,'order/order.html',{'orders':orders})
def order_details(request,pk):
    order= Order.objects.get(pk=pk)
    order_details = OrderItem.objects.filter(order=order)

    return render(request,'order/ordersingle.html',{'details':order_details})