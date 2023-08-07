from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def voluntary_view(request):
    return render(request, 'voluntary.html')

def supporter_view(request):
    return render(request, 'supporter.html')
