from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView
from .models import Hoge
############################私たちは総じておまんこが大好きです。###########################
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'app.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/')
    #template = loader.get_template("apps/index.html")
    #return HttpResponse(template.render({}, request))

class HogeListView(Listview):
    template_name = 'hoge_list.html'
    model = Hoge

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['user'] = self.request.user # これによって user という名前のデータがコンテキストに追加される
        return ctx