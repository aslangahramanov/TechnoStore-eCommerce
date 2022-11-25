from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    
    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=85, null=False, blank=False)
    description = models.TextField(max_length=90, null=False, blank=False)
    old_price = models.CharField(max_length=10, null=False, blank=True)
    price = models.CharField(max_length=10, null=False, blank=False)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    discount = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title