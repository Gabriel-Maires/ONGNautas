from django.shortcuts import render

# Create your views here.

def ong_admin_view(request):
    return render(request, 'ong_admin.html') 