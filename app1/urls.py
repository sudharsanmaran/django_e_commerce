
from django.urls import path
from app1 import views

app_name='app1'
urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('yourorder/', views.your_order, name='your_order'),

]

