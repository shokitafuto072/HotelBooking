from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def roomselection(request):
    return render(request,'roomselection.html')

def planselection(request):
    return render(request,'planselection.html')


def bookingmanage(request):
    return render(request,'bookingmanage.html')

def form_page(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        return render(request, 'next_page.html', {'data': data})
    return render(request, 'form_page.html')




# Create your views here.

