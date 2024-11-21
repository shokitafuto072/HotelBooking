from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def dashboard(request):
    return render(request, 'dashboard.html')

def checkinlist(request):
    return render(request, 'checkinlist.html')

def checkoutlist(request):
    return render(request, 'checkoutlist.html')

def guests_list(request):
    return render(request, 'guests_list.html')

def clean_manage(request):
    return render(request, 'clean_manage.html')

def kyakusitu(request):
    return render(request, 'kyakusitu.html')

def edit_plans(request):
    return render(request, 'edit_plans.html')

def shukei(request):
    return render(request, 'shukei.html')

def room_status(request):
    return render(request, 'room_status.html')

# Create your views here.
