from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'authenticate'

urlpatterns = [
    path('register/', views.register, name="register"),  
    path('register/1/', views.register_student, name="register_student"),  
    path('register/2/', views.register_faculty, name="register_faculty"),  
    path('login/', views.user_login, name="user_login"),  
    path('logout/', views.user_logout, name="user_logout"), 
]
