from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import Student
from .models import Course
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import InputForm
from .forms import StudentForm
from .models import Post
from .forms import PostForm
from . import views
from django.shortcuts import HttpResponse, render, redirect

def Welcome(request):

    return HttpResponse("Welcome to our site")

# Create your views here.

def Hello(request):
    today = datetime.now().date()
    return render(request, "show.html", {"today" : today})
def names_view(request):
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Student.objects.all()

    return render(request, "names_view.html", context)
def courses_view(request):
    context ={}
    # add the dictionary during initialization
    context["dataset"] = Course.objects.all()

    return render(request, "courses_view.html", context)

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)


def home_view2(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    # save the form data to model

    context ={}
    context['StudentForm'] =StudentForm()
    return render(request, "home2.html", context)



class StudentCreate(CreateView):
# specify the model for create view
    model = Student
# specify the fields to be displayed
    fields = ['f_name', 'l_name']

class CourseCreate(CreateView):
# specify the model for create view
    model = Course
# specify the fields to be displayed
    fields = ['c_name']

class StudentUpdateView(UpdateView):
# specify the model you want to use
    model = Student
# specify the fields
    fields = [
    "f_name",
    "l_name"
    ]
# can specify success url
# url to redirect after successfully
# updating details
    success_url ="/"

class CourseUpdateView(UpdateView):
# specify the model you want to use
    model = Course
# specify the fields
    fields = [
    "c_name"
    ]
# can specify success url
# url to redirect after successfully
# updating details
    success_url ="/"


class StudentDeleteView(DeleteView):
    # specify the model you want to use
    model = Student

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/"

    template_name = "students/student_confirm_delete.html"

# Create your views here.


