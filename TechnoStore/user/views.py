from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('info:default')
        else:
            return render(request, 'login.html', {'error': "Istifadeci adi ve ya sifre yanlisdir"})    
            
    return render(request, 'login.html')

def register_views(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request, 'register.html', {"error": "Username basqasi terefinden istifade olunur"})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, 'register.html', {"error": "E-mail basqa birine aiddir"})
                else:
                    user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
                    user.save()
                    return redirect('user:login')
                
        else:
            return render(request, 'register.html', {"error": "Sifreler uygun deyil"})

    return render(request, 'register.html')