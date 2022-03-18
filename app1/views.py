from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app1.models import Category, Product



def categories(request):
    return{
        'categories':Category.objects.all()
    }

def productdetails(request,name):

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

        if not username or not password:
            return {
                "error":"some required fields is missing",

            }
        user=auth.authenticate(username=username,password=password)
        if not user:
            return {
                "error":"invalid credentials, user not exit",

            }

        return HttpResponseRedirect(reverse('app1:cart'))
    else:
        return render(request, 'app1/login.html',{

        })
def logout(request):

    auth.logout(request)

    return HttpResponseRedirect(reverse('app1:home'))

def add_to_cart(request,slug):

    user=request.user
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))
    product=get_object_or_404(Product, slug=slug, is_available=True)
def remove_from_cart(request,slug):
    user=request.user

def register(request):

    return render(request, 'app1/register.html')

def your_order(request):

    return render(request, 'app1/yourorder.html')
# class login(generic.ListView):
#     template_name = 'app1/login.html'

# class logout(generic.ListView):
#     template_name = 'app1/logout.html'

# class register(generic.ListView):
#     template_name = 'app1/register.html'



