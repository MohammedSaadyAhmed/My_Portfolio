from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def Welcome(request):
    return HttpResponse("Welcome to our site")

def CV(request):
    template = loader.get_template('My_CV.html')
    return HttpResponse(template.render())


# Create your views here.
