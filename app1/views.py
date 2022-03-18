from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app1.models import Category, Product, Customer


#test

def categories(request):
    return{
        'categories':Category.objects.all()
    }

def productdetails(request,name):

    return {
        "product":Product.objects.all()
    }
def home(request):

    name="sudha"
    return render(request, 'app1/home.html',{"products" : Product.objects.all()})


def cart(request):

    user=request.user
    if user.is_anonymous:
        return HttpResponseRedirect(reverse("app1:login"))
    print(user)
    products=Customer.objects.all().filter(user=user)

    return render(request, 'app1/cart.html',{
        'products':products,
    })

def order(request):

    return render(request, 'app1/order.html')

def login(request):
    if request.method=='post':
        username=request.POST['username']
        password=request.POST['password']
        print('user',username)
        print(password)
        if not username or not password:
            return {
                "error":"some required fields is missing",

            }
        user=auth.authenticate(username=username,password=password)
        if not user:
            return {
                "error":"invalid credentials, user not exit",

            }
        print(user)
        return HttpResponseRedirect(reverse('app1:cart'))
    else:
        return render(request, 'app1/login.html',{

        })
def logout(request):
    auth.logout(request)
    return render(request, 'app1/home.html')

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



