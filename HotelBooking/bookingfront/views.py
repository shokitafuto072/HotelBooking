from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def roomselection(request):
    return render(request,'roomselection.html')

def planselection(request):
    return render(request,'planselection.html')




# Create your views here.

