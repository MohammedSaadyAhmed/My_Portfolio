from django.urls import path
from . import views


urlpatterns = [
    path('My_CV/',views.CV,name='My_CV'),
    path('welcome/',views.Welcome,name='Welcome'),
]
