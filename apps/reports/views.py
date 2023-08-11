from django.http import HttpRequest

from django.urls import reverse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.messages import constants

from .forms import ReportsForm

from django.core.paginator import Paginator
from .models import Report


def denouncement_view(request: HttpRequest):

    match request.method:
        case 'GET':
            context = {
                'form': ReportsForm(),
                'open_denouncement_modal': False
            }

            return render(request, 'denouncement.html', context)
        
        case 'POST':

            reports_form = ReportsForm(request.POST, request.FILES)
            context = {
                'form': reports_form,
                'open_denouncement_modal': True
            }

            if reports_form.is_valid():
                try:
                    reports_form.save()
                    messages.add_message(request, constants.SUCCESS, 'Denúncia enviada com sucesso!')

                    return redirect(reverse('denouncement'))
                
                except:
                    messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')

                    return render(request, 'denouncement.html', context)
            
            print(reports_form.errors)

            messages.add_message(request, constants.WARNING, 'Preencha os campos corretamente!')    

            return render(request, 'denouncement.html', context)


def show_reports(request):
    reports = Report.objects.all()

    reports_paginator = Paginator(reports, 10)
    page_num = request.GET.get('page')
    page = reports_paginator.get_page(page_num)

    return render(request, 'denouncement.html', {'page':page})
