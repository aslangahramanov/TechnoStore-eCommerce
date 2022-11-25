from django.shortcuts import render
from products.models import Category

# Create your views here.

def blog(request):
    categoryes = Category.objects.all()
    return render(request, 'blog.html', context={'categoryes': categoryes})