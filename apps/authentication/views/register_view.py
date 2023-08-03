from django.shortcuts import render
from authentication.models.user import User

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        address = request.POST.get('address')
        complement = request.POST.get('complement')
        is_supporter = request.POST.get('supporter')
        is_voluntary = request.POST.get('voluntary')
        password = request.POST.get('password') if (request.POST.get('password') == request.POST.get('password_confirmation')
                                                    ) else None
        user = User(username=name, email=email, 
                    birth_date=birth_date, cpf=cpf, 
                    cep=cep, address=address, 
                    complement=complement, is_supporter=is_supporter,
                    is_voluntary=is_voluntary, password=password)
        user.save()