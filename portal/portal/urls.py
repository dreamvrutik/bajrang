"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bajrang import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('verify-login',views.check_login),
    path('register',views.register),
    path('home/<type>',views.home),
    path('add_to_cart/<product>',views.add_to_cart),
    path('cart',views.cart_page),
    path('update_cart/<product>',views.update_cart),
    path('delete/<product>',views.delete_cart),
    path('place_order',views.place_order),
    path('orders',views.prev_orders)
]
