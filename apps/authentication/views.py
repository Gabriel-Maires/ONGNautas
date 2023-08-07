from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth

from django.contrib import messages
from django.contrib.messages import constants

from .forms import RegisterForm
from .models import Voluntary


def register_view(request):

    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                return redirect(reverse('home'))

            return render(request, 'register.html', {'form': RegisterForm()})
        
        case 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                if user.is_voluntary:
                    Voluntary.objects.create(user=user)

                    message: str
                    if user.is_voluntary and user.is_supporter:
                        message = 'Você se cadastrou como voluntário e apoiador!'
                    elif user.is_voluntary:
                        message = 'Você se cadastrou como voluntário!'
                    elif user.is_supporter:
                        message = 'Você se cadastrou como apoiador!'
                    
                    messages.add_message(request, constants.INFO, message)

                messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso!')

                return redirect(reverse('login'))
            
            messages.add_message(request, constants.WARNING, 'Preencha os campos corretamente!')
                
            return render(request, 'register.html', {'form': register_form},)


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
