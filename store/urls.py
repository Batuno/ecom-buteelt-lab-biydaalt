from django.urls import path
from . import views
from .models import Category

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login_page, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register_page, name='register'),
    path('list_products/', views.list_products, name='list_products'),
    path('all_products', views.all_products, name='all_products'),
    path('<slug:category_slug>/', views.product, name='product'),
    path('<slug:category_slug>/<slug:product_slug>/', views.details, name='details'),
    
]

