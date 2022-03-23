from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app1.models import Category, Product


# to load name of categories
def categories(request):
    return{
        'categories':Category.objects.all()
    }
# to load all the products within category
def all_products_catogory(request, category_id):

    messages.add_message(request,messages.SUCCESS,
                         'filter applied')
    products=Product.objects.all().filter(category=category_id)
    return render(request, 'app1/home.html',
                  {"products" : products})

def home(request):

    products = Product.objects.all()
    return render(request, 'app1/home.html',
                      {"products": products})

def cart(request):

    user=request.user
    print("userrrr in cart",user)
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))

    products=Product.objects.all().filter(user=user)
    total_price=0
    if not products:
        messages.add_message(request,messages.WARNING,
                             'no item in cart')
    for p in products:
        for uq in range(p.user_quantity):
            total_price = total_price + p.price

    return render(request, 'app1/cart.html',{
        'products':products,
        'total_price': total_price,
    })

def order(request):
    return render(request, 'app1/order.html')

def login(request):
    #always use POST instead of post
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("@@@@@@@@@@@@@@@2",username,password)
        user=auth.authenticate(username=username,password=password)
        print("userrrrrrrrrrrrrr in login ",user)
        if user:
            return HttpResponseRedirect(reverse('app1:cart'))

        return render(request, 'app1/login.html')
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
    if product.quantity > 0:
        product.quantity -= 1
        product.user_quantity +=1
        # product.user=user doesn't work for many to many field
        # for set method need instance of model,
        # not field of particular instance
        usr=User.objects.filter(username=user)
        product.user.set(usr)
        product.save()
        messages.add_message(request, messages.SUCCESS,
                             'successfully added to cart')
        return HttpResponseRedirect(reverse("app1:home"))
    else:
        messages.add_message(request, messages.WARNING,
                             'out of stack')
        return HttpResponseRedirect(reverse("app1:home"))

def remove_from_cart(request,product_id):
    user=request.user
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))
    product = get_object_or_404(Product, id=product_id, is_available=True)
    if product:
        product.quantity+=1
        if product.user_quantity > 1:
            product.user_quantity -= 1
            product.save()
            return HttpResponseRedirect(reverse('app1:cart'))
        product.user_quantity -=1
        #product.user.set(None) None doesn't work
        product.user.clear()
        product.save()
        messages.add_message(request, messages.SUCCESS,
                             'sucessfully removed')
        return HttpResponseRedirect(reverse("app1:cart"))
def register(request):

    return render(request, 'app1/register.html')

def your_order(request):

    return render(request, 'app1/yourorder.html')



