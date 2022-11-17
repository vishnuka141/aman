from django.shortcuts import render,HttpResponse,redirect
from product.models import Product,Category
from .forms import Signupform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

    
def signup(request):
    form = Signupform()
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'User created Successfully')
            return redirect('signin')
    return render(request,'signup.html',{'form':form})

def signin(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user =  authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login successful')
            return redirect("home")
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('home')