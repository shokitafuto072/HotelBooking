from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def dashboard(request):
    return render(request, 'dashboard.html')

# Create your views here.
