from django.db import models
from django.contrib.auth.models import AbstractUser

# User types choices
USER_TYPE_CHOICES = (
    ("Student","Student"),
    ("Faculty","Faculty"),
)

#department model
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# user model
class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=1000,unique=True)
    type = models.CharField(max_length=15,choices=USER_TYPE_CHOICES, default="Student")

    def __str__(self):
        return self.username

# student model    
class Student(User):
    enrollment_no = models.CharField(max_length=15)
    semester = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

# faculty model
class Faculty(User):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.username
