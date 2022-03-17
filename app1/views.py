from django.shortcuts import render
from django.views import generic
# Create your views here.
# class home(generic.DetailView):
#     template_name = 'app1/home.html'
def home(request):

    return render(request, 'app1/home.html')

def cart(request):

    return render(request, 'app1/cart.html')

def order(request):

    return render(request, 'app1/order.html')

def login(request):

    return render(request, 'app1/login.html')
def logout(request):

    return render(request, 'app1/logout.html')
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



