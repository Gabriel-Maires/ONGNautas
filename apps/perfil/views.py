from django.shortcuts import render
from .forms import VoluntaryProjectsForm
from django.contrib import messages
from django.contrib.messages import constants

def index_view(request):
    return render(request, 'index.html')


def voluntary_view(request):
  user = request.user

  return render(request, '.html', {'is_voluntary': user.is_voluntary})


def supporter_view(request):
  user = request.user

  return render(request, '.html', {'is_supporter': user.is_supporter})


def project_registration(request):
    if request.method == 'GET':
        return render(request, 'voluntary.html')
    elif request.method == 'POST':
            projects_form = VoluntaryProjectsForm(request.POST)
            if projects_form.is_valid():
                try:
                    projects_form.save()
                except:
                    messages.add_message(
                                request, 
                                constants.ERROR, 
                                'Houve algum erro. Tente novamente mais tarde.'
                            )
            else:
                messages.add_message(request, constants.WARNING, 'Preencha os campos corretamente!')
                return render(request, 'voluntary.html', {'form':projects_form})
        