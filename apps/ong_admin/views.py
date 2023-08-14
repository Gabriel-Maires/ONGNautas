from django.shortcuts import render
from rolepermissions.decorators import has_role_decorator
from ong.forms import ProjectForm
from authentication.forms import RegisterForm
from rolepermissions.roles import assign_role
# Create your views here.

def ong_admin_view(request):
    return render(request, 'ong_admin.html') 


@has_role_decorator('admin')
def create_projects(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            try:
                project_form.save()
                messages.add_message(request, constants.SUCCESS, 'Ação criada com sucesso!')
            except:
                messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Houve algum erro. Tente novamente mais tarde.'
                    )


def register_admin(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            try:
                register_form.save()

                assign_role(user, 'admin')
                messages.add_message(request, constants.SUCCESS, 'Administrador criado com sucesso!')
            except:
                messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Houve algum erro. Tente novamente mais tarde.'
                    )


def allow_project_register(request):
    pass