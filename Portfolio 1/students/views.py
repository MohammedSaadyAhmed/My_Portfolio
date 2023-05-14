from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def welcome(request):
    return HttpResponse("Welcome home")

def hello(request):
    today = datetime.now().date()
    return render(request, "show.html", {"today" : today})
    template = loader.get_template('show.html')
    return HttpResponse(template.render())
# Create your views here.
