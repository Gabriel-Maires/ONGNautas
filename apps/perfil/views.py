from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def voluntary_view(request):
  user = request.user

  return render(request, '.html', {'is_voluntary': user.is_voluntary})

def supporter_view(request):
  user = request.user

  return render(request, '.html', {'is_supporter': user.is_supporter})

