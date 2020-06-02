from django.db import models
from authenticate.models import User,Department, Student, Faculty
from django import template

register = template.Library()

class ResourceType(models.Model):
    type = models.CharField(max_length = 50)

    def __str__(self):
        return self.type

class Resources(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type_id = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link_to_resource = models.FileField(upload_to = 'files/')

    def __str__(self):
        return self.name

    @register.filter(name='get_student_semester')
    def get_student_semester(self,user_id):
        return Student.objects.filter(id=user_id).values('semester')[0]['semester']