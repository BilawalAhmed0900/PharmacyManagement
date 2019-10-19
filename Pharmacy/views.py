from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def redirect_view(request):
    response = redirect('/login/')
    return response


@login_required
def home(request):
    return HttpResponse('Loged-in')
