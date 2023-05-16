from django.urls import path
from . import views
from .views import StudentCreate
from .views import CourseCreate
from .views import StudentUpdateView
from .views import CourseUpdateView
from .views import StudentDeleteView


urlpatterns = [
    path('hello/', views.Hello, name='hello'),
    path('Welcome/', views.Welcome, name='Welcome'),
    path('names/', views.names_view, name='name'),
    path('courses/', views.courses_view, name='courses'),
    path('create-student/', StudentCreate.as_view()),
    path('create-course/', CourseCreate.as_view()),
    path('<pk>/update/', StudentUpdateView.as_view()),
    path('<pk>/update/', CourseUpdateView.as_view()),
    # <pk> is identification for id field,
    # slug can also be used
    path('<pk>/delete/', StudentDeleteView.as_view()),
    path('home/', views.home_view, name='home'),
    path('home2/', views.home_view2, name='home2'),




]
