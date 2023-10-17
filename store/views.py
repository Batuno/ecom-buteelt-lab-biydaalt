from django.shortcuts import render, redirect
from .models import Product, Category, Customer
import sqlite3 as sql
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
import hashlib
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

#utils
def hash_password(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash

#views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {})

def all_products(request):
    return render(request, 'all_products.html')

def login_page(request):
    customer = Customer.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        hashed_password = hash_password(password)  
        
        try:
            suser = Customer.objects.get(username=username)
            if suser and hashed_password == suser.password:
                login(request, suser)
                print(login(request, suser))
                return redirect('home')  
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'login_page.html', {'error_message': error_message})
        except ObjectDoesNotExist:
            error_message = "User with this username does not exist. Please try again."
            return render(request, 'login_page.html', {'error_message': error_message})
        
    
    return render(request, 'login_page.html', {'customer':customer})

def user_logout(request):
    logout(request)
    print(logout(request))
    return redirect('home')

def register_page(request):
    form = CustomerRegistrationForm()

    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully')
            return redirect('login_page')

    return render(request, 'register_page.html', {'form':form})

def product(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    product = Product.objects.select_related('category').filter(category=category)    
    rcount = len(list(product))
    return render(request, 'product.html',{'product': product, 'rcount': rcount, 'category': Category.objects.all()})

def details(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category)
    return render(request, 'details.html', {'category': category, 'product': product, 'category': Category.objects.all()})


def list_products(request):
    product_list = Product.objects.order_by('-id').all()
    p = Paginator(product_list, 4)
    page = request.GET.get('page')
    sproduct = p.get_page(page)
    nums = sproduct.paginator.num_pages * 'a'
    return render(request, "list_products.html", {'sproduct': sproduct, 'nums': nums})


