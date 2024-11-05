from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
############################私たちは総じておまんこが大好きです。############################
# Create your views here.

def index(request):
    template = loader.get_template("apps/index.html")
    return HttpResponse(template.render({}, request))