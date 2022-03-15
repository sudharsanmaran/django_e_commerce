from django.urls import path
from app1 import views

app_name='app1'
urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('<int:pk>/cart/',views.cart.as_view(),name='cart'),
    path('<int:pk>/order/',views.order.as_view(),name='order'),
    path('login/',views.as_view(),name='login'),
    path('logout/',views.as_view(),name='logout'),
    path('register/',views.as_view(),name='register'),
    # path('login/',views.as_view(),name='login'),
]
