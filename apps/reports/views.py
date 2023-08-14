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
            all_reports = Report.objects.all()
            paginator = Paginator(all_reports, 10)

            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)
            context = {
                'page': page,
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

                    all_reports = Report.objects.all()
                    paginator = Paginator(all_reports, 10)

                    page_number = request.GET.get('page')
                    page = paginator.get_page(page_number)

                    reports_form = ReportsForm(request.POST, request.FILES)
                    context = {
                        'page': page,
                        'form': reports_form,
                        'open_denouncement_modal': True
                    }

                    return render(request, 'denouncement.html', context)
                
                except:
                    messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')

                    return render(request, 'denouncement.html', context)
            
            print(reports_form.errors)

            messages.add_message(request, constants.WARNING, 'Preencha os campos corretamente!')    

            return render(request, 'denouncement.html', context)

def transparency_view(request):
    return render(request, 'transparency.html')
