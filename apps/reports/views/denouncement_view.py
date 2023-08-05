from django.shortcuts import render
from reports.forms.reports_form import ReportsForm


def denouncement_view(request):
    if request.method == 'GET':
        return render(request, 'denouncement.html')
    elif request.method == 'POST':
        reports_form = ReportsForm(request.POST)
        if reports_form.is_valid():
            reports_form.save()
        else:
            return render(request, 'denouncement.html', {'form':reports_form})