from django.shortcuts import render
from .forms import VoluntaryProjectsForm

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
            projects_form.save()
        else:
            return render(request, 'voluntary.html', {'form':projects_form})