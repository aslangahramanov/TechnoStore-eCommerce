from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.home, name = 'default'),
    path('home/', views.home, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about')
    
]

