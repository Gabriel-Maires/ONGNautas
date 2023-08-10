from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth

from django.http import HttpRequest

from django.contrib import messages
from django.contrib.messages import constants

from rolepermissions.roles import assign_role

from .forms import RegisterForm, LoginForm
from .models import Voluntary


def register_view(request: HttpRequest):

    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                return redirect(reverse('home'))

            return render(request, 'register.html', {'form': RegisterForm()})
        
        case 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                try:
                    user = register_form.save()
                    if user.is_voluntary:
                        Voluntary.objects.create(user=user)

                    message: str
                    if user.is_voluntary and user.is_supporter:
                        message = 'Você se cadastrou como voluntário e apoiador!'

                        assign_role(user, 'voluntary')
                        assign_role(user, 'supporter')
                        
                    elif user.is_voluntary:
                        message = 'Você se cadastrou como voluntário!'

                        assign_role(user, 'voluntary')

                    elif user.is_supporter:
                        message = 'Você se cadastrou como apoiador!'

                        assign_role(user, 'supporter')

                    messages.add_message(request, constants.INFO, message)
                    messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso!')

                    return redirect(reverse('login'))
                
                except:
                    messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Erro interno do sistema. Tente novamente mais tarde.'
                    )

                    return render(request, 'register.html', {'form': register_form})
            
            messages.add_message(request, constants.WARNING, 'Preencha os campos corretamente!')
                
            return render(request, 'register.html', {'form': register_form},)


def login_view(request: HttpRequest):
    
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                return redirect(reverse('home'))

            return render(request, 'login.html', {'form': LoginForm()})
        
        case 'POST':
            login_form: LoginForm = LoginForm(request.POST)

            if login_form.is_valid():
                email = login_form.cleaned_data.get('email')
                password = login_form.cleaned_data.get('password')

                try:
                    user = auth.authenticate(username=email, password=password)

                    if user is not None:
                        auth.login(request, user)

                        return redirect(reverse('home'))
                    
                    messages.add_message(request, constants.WARNING, 'Credenciais incorretas!')

                    return render(request, 'login.html', {'form': login_form})

                except:
                    messages.add_message(
                        request,
                        constants.ERROR,
                        'Erro interno do sistema. Tente novamente mais tarde.'
                    )

                    return render(request, 'login.html', {'form': login_form})

            messages.add_message(request, constants.WARNING, 'Preencha os campos corretamente!')
            
            return render(request, 'login.html', {'form': login_form})


def logout_view(request: HttpRequest):

    auth.logout(request)
    return redirect(reverse('home'))
