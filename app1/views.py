from django.shortcuts import render
from django.views import generic
# Create your views here.
# class home(generic.DetailView):
#     template_name = 'app1/home.html'
def home(request):
    return render(request, 'app1/home.html')
class login(generic.ListView):
    template_name = 'app1/login.html'

class logout(generic.ListView):
    template_name = 'app1/logout.html'

class register(generic.ListView):
    template_name = 'app1/register.html'

class cart(generic.ListView):
    template_name = 'app1/cart.html'

class order(generic.ListView):
    template_name = 'app1/order.html'