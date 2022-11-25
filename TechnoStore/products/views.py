from django.shortcuts import render
from .models import Category, SubCategory, Products

# Create your views here.
def products(request):
    categoryes = Category.objects.all()
    return render(request, 'products.html', context={'categoryes': categoryes} )