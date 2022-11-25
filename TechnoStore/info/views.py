from django.shortcuts import render
from products.models import Category, Products, SubCategory
from .models import SliderImage

# Create your views here.
def home(request):
    sliderimage = SliderImage.objects.all()
    categoryes = Category.objects.all()
    products = Products.objects.all()
    return render(request, 'index.html', context={'categoryes': categoryes, 'sliderimage': sliderimage, 'products': products})


def contact(request):
    categoryes = Category.objects.all()
    return render(request, 'contact.html', context={'categoryes': categoryes})


def about(request):
    categoryes = Category.objects.all()
    return render(request, 'about.html', context={'categoryes': categoryes})