from django.contrib import admin
from .models.item import Product
from .models.category import Categorie
from .models.customer import Customer
from .models.order import Order
# Register your models here.

class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','category']

class Admincategory(admin.ModelAdmin):
    list_display=['name']

class Admincustomer(admin.ModelAdmin):
    list_display=['name']

class Adminorder(admin.ModelAdmin):
    list_display=['customer','product','quantity','price','address','phone','date','delivered']

admin.site.register(Product,Adminproduct)
admin.site.register(Categorie,Admincategory)
admin.site.register(Customer,Admincustomer)
admin.site.register(Order,Adminorder)