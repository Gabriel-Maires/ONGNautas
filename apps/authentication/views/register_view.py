from django.shortcuts import render
from authentication.models import User
from authentication.forms.register_form import RegisterForm


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        else:
            return render(request, 'register.html', {'form': register_form},)
