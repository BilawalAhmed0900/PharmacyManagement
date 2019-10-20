from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Medicine


def redirect_view(request):
    response = redirect('/login/')
    return response


def home(request):
    if not request.user.has_perm('Pharmacy.view_medicine'):
        return HttpResponse('Not authorized to view this page. Contact your admin...')

    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name', '')
        if medicine_name != '':
            objs = Medicine.objects.filter(name__contains=medicine_name)
            return render(request, 'home.html', {'data': objs})

    return render(request, 'home.html', {'data': None})


