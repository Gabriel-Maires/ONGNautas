from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth


def login_view(request):
    
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                return redirect(reverse('home'))

            return render(request, 'login.html')
        
        case 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = auth.authenticate(username=email, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect(reverse('home'))
            
            return redirect(reverse('login'))          
