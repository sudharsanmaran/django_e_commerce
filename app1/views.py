from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app1.models import Category, Product



def categories(request):
    return{
        'categories':Category.objects.all()
    }

def all_products_catogory(request, category_id):

    products=Product.objects.all().filter(category=category_id)
    return render(request, 'app1/home.html',
                  {"products" : products})

def productdetails(request):

    return {
        "product":Product.objects.all()
    }
def home(request):

    return render(request, 'app1/home.html',
                  {"products" : Product.objects.all()})


def cart(request):

    user=request.user
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))

    products=Product.objects.all().filter(user=user)

    return render(request, 'app1/cart.html',{
        'products':products,
    })

def order(request):

    return render(request, 'app1/order.html')

def login(request):
    if request.method=='post':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("@@@@@@@@@@@@@@@2",username,password)
        if not username or not password:
            return {
                "error":"some required fields is missing",
                'username':'missing',
            }
        user=auth.authenticate(username=username,password=password)
        if not user:
            return {
                "error":"invalid credentials, user not exit",
                'username':"invalid",
            }

        return HttpResponseRedirect(reverse('app1:cart'))
    else:
        return render(request, 'app1/login.html',{})
def logout(request):

    auth.logout(request)

    return HttpResponseRedirect(reverse('app1:home'))

def add_to_cart(request, product_id):

    user=request.user

    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))
    product=get_object_or_404(Product, pk=product_id, is_available=True)
    print(product)
    # product.user=user doesn't work for many to many field
    # for set method need instance of model,
    # not field of particular instance
    usr=User.objects.filter(username=user)
    product.user.set(usr)
    product.save()
    return HttpResponseRedirect(reverse("app1:cart"))
def remove_from_cart(request,product_id):
    user=request.user
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))
    product = get_object_or_404(Product, id=product_id, is_available=True)
    #product.user.set(None) None doesn't work
    product.user.clear()
    product.save()
    return HttpResponseRedirect(reverse("app1:cart"))
def register(request):

    return render(request, 'app1/register.html')

def your_order(request):

    return render(request, 'app1/yourorder.html')



