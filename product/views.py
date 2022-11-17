from django.shortcuts import render
from .models import Product,Category
from django.shortcuts import get_object_or_404
# Create your views here.
def product_details(request,pk):
    detail=Product.objects.get(pk=pk)
    # detail=get_object_or_404(Product,pk=pk)
    return render(request,'product/productsingle.html',{'details':detail})

def product_list(request):
    # if request.method=='POST':
    #      check = request.GET.get('cat',0)
    #      if check:
    #         categories=Category.objects.
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        'products':products,
        'categories':categories
    }
    return render(request,'product/products.html',context)

def categories(request,pk):
    
    if request.method=='GET':
        check = request.GET.get('cat',0)
       
        if check:
            categories=Category.objects.get(pk=pk)
            # categories=Category.objects.filter(category_name="Cleaning")
            products=Product.objects.filter(category=categories)
            print(categories,'dfd------------------------------')
            
        else:
            products=Product.objects.all()
        return render(request,'product/products.html',{"products":products})