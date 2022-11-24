from itertools import product
from unicodedata import category
from django.contrib import auth
from email import message
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .models import Customer, Product, Categories, Cart, OrderedPlaced
import logging
 
# def home(request):
#   return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        malewears=Product.objects.filter(gender='M')
        femalewears=Product.objects.filter(gender='F')
        return render(request, 'app/home.html', {'malewears':malewears, 'femalewears':femalewears})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class  ProductDetailView(View):
    def get(self, request, pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def addCategory(request):
    if request.method=='POST':
        category=request.POST.get('category')
        category=Categories(category=category)
        category.save()
        return render(request, 'app/addCategory.html') 
    else:
        return render(request, 'app/addCategory.html')

def addProduct(request):
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        category=request.POST.get('category')
        brand=request.POST.get('brand')
        description=request.POST.get('description')
        specification=request.POST.get('specification')
        status=request.POST.get('status')
        gender=request.POST.get('gender')
        product_img=request.POST.get('image')
        product=Product(title=title,price=price,discount=discount,category=category,brand=brand,description=description,specification=specification,status=status,gender=gender,product_img=product_img)
        product.save()
        return redirect("/")     
    else:
        category=Categories.objects.all()
        catg={ 'category':category }
        return render(request, 'app/addProduct.html',catg)

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def gender(request,data):
    if data=='M':
        wears=Product.objects.filter(gender='M')
    else:
        wears=Product.objects.filter(gender='F')
    return render(request, 'app/gender.html', {'wears':wears})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return HttpResponse("Login Fail")
    else:
        return render(request, "app/login.html")
    
        
def logout(request):
    auth.logout(request)
    return redirect('/')

def registration(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        
        if (password==password2):
            user=User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=user_name, password=password)
            user.save()
            return render(request, "app/login.html")
        else:
            message.error(request,'Password Mismatched')
            return redirect('/')
    else:
        return render(request, "app/registration.html")
            
def checkout(request):
 return render(request, 'app/checkout.html')
