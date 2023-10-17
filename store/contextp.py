from .models import Category, Product
import sqlite3 as sql
from django.shortcuts import render, get_object_or_404

def home(request):
    productL = Product.objects.all()
    categoryL = Category.objects.all()
    return {'product': productL, 'category': categoryL}
def all_products(request):
    all_products = Product.objects.all()
    rcount = len(all_products)
    categories = Category.objects.all()
    return {'product': all_products, 'rcount': rcount, 'categories': categories}





    