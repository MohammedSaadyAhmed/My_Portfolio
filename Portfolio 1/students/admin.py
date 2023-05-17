from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name",)

admin.site.register(Student, StudentAdmin)