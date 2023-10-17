from django.contrib import admin
from .models import Category, Customer, Product, Order

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

