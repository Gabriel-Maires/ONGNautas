from django.shortcuts import render


def denouncement_view(request):
    return render(request, 'denouncement.html')
