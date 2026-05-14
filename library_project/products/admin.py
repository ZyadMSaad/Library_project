# from django.contrib import admin
# from .models import Product

# class ProductAdmin(admin.ModelAdmin):
  
#     list_display = ('name', 'book_id', 'author', 'category')
    
 
#     search_fields = ('name', 'author')


# admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Borrow, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','author','active','borrowed']
admin.site.register(Product, ProductAdmin)
admin.site.register(Borrow)