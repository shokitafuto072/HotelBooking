from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'app.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/')
    #template = loader.get_template("apps/index.html")
    #return HttpResponse(template.render({}, request))