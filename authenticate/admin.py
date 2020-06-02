from django.contrib import admin
from .models import Department, Faculty, Student, User 
# Register your models here.
admin.site.register(Department)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)