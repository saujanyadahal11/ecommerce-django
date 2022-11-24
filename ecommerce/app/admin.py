from django.contrib import admin
from .models import(Customer, Categories, Product, Cart, OrderedPlaced)

# Register your models here.

@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=['id','category']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','address','district','zone']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','price','discount','description','brand','category','product_img','gender']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(OrderedPlaced)
class OrdermodelPlaced(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','orderedDate','status']

