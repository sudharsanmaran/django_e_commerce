from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app1 import views

app_name='app1'
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:pk>/cart/',views.cart.as_view(),
         name='cart'),
    path('<int:pk>/order/',views.order.as_view(),
         name='order'),
    path('login/',views.login.as_view(),
         name='login'),
    path('logout/',views.logout.as_view(),
         name='logout'),
    path('register/',views.register.as_view(),
         name='register'),
    # path('login/',views.as_view(),
    # name='login'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)