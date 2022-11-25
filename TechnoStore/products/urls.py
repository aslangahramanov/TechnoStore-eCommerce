from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products, name = 'products')
]
