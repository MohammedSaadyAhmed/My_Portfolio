from django.db import models


class Student(models.Model):
    f_Name = models.CharField(max_length=255)
    l_Name = models.CharField(max_length=255)
    

class Courses(models.Model):
    c_Name = models.CharField(max_length=255)

# Create your models here.
