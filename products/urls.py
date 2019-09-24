"""hoteladmin URL Configuration

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
from django.urls import path,include
from products import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('', views.index, name='index'),
    path('restaurant-upload-menu', views.add_product, name='upload_menu'),
    path('view_menu', views.view_product, name='view_menu'),
    path('update_menu', views.update_product, name='update_menu'),
    path('delete_menu', views.delete_menu, name='delete_menu'),
    path('products/', views.Productlist.as_view()),
    path('procat/', views.ProductCategory.as_view()),
    path('restaurant-menu-one', views.menus_one, name='menus_one'),
    path('restaurant-menu-two', views.menus_two, name='menus_two'),
    path('restaurant-menu-three', views.menus_three, name='menus_three'),
    path('logout', views.logout, name='logout'),
    path('orders/',include('orders.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)