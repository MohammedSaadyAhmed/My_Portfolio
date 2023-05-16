from django.db import models

# Create your models here.

class Student(models.Model):

    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)

class Course(models.Model):

    c_name = models.CharField(max_length=50)


