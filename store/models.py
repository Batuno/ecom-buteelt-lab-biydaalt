from django.db import models
import datetime
from django.urls import reverse
from django.utils import timezone
import hashlib

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=8)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    last_login = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Hash the password using hashlib before saving
        password_hash = hashlib.sha256(self.password.encode()).hexdigest()
        self.password = password_hash
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=11)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    slug = models.SlugField(null=False)
    stock = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', args=[self.category.slug, self.slug])
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=8, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product
    
