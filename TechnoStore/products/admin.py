from django.contrib import admin
from .models import Category, SubCategory, Products

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Products)

# @admin.register(Products)
# class ProductsAdmin(admin.ModelAdmin):
#     fields = ['image','title','description', 'old_price', 'price', 'sub_category']
    