from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def roomselection(request):
    return render(request,'roomselection.html')

def planselection(request):
    return render(request,'planselection.html')


def bookingmanage(request):
    return render(request,'bookingmanage.html')




# Create your views here.

