from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def roomselection(request):
    return render(request, 'roomselection.html')




# Create your views here.

