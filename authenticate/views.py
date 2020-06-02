# import django libs
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views import View

# import classes
from .forms import StudentForm,FacultyForm, LoginForm
from .models import User,Student,Faculty,Department

# register view
def register(request):
    if request.user.is_authenticated:
        return redirect('resources:index')
    return render(request,"authenticate/register.html")

# student registration view
def register_student(request):
    if request.user.is_authenticated:
        return redirect('resources:index')
    registered = False
    
    # return HttpResponse("Reg")
    if request.method == "POST":
        # get data from POST request
        print(request.POST)
        student_form = StudentForm(data=request.POST)

        # check if the username already exists
        validate_username(request.POST["username"])
        
        # validate data 
        if student_form.is_valid() :
            # save the user
            student = student_form.save(commit=False)

            #set the password
            student.set_password(student.password)
            student.type = "Student"
            student.save()

            registered = True
            status = "success"
            message = "Register Successfully! Now you can login from the login page."            
        else:
            # send error message
            status = "error"
            message = str(student_form.errors)
        student_form = StudentForm()
        return render(request,'authenticate/register_student.html', {"status":status,"message":message,"student_form":student_form})
    else:
        student_form = StudentForm()

    # render the registration form
    return render(request, 'authenticate/register_student.html', {'student_form':student_form, 'registered':registered })

# user registration view
def register_faculty(request):
    if request.user.is_authenticated:
        return redirect('resources:index')
    registered = False
    status = None
    message = None
    # return HttpResponse("Reg")
    if request.method == "POST":
        # get data from POST request
        print(request.POST)
        faculty_form = FacultyForm(data=request.POST)
        
        # check if username already exists
        validate_username(request.POST["username"])

        # validate data 
        if faculty_form.is_valid() :
            # save the user
            
            faculty = faculty_form.save(commit=False)

            #set the password
            faculty.set_password(faculty.password)
            faculty.type = "Faculty"
            faculty.save()

            registered = True
        
            status = "success"
            message = "Register Successfully! Now you can login from the login page."
        else:
            status = "error"
            message = str(faculty_form.errors)
        faculty_form = FacultyForm()
        return render(request,'authenticate/register_faculty.html', {"status":status,"message":message,"faculty_form":faculty_form})
    else:
        faculty_form = FacultyForm()

    # render the registration form
    return render(request, 'authenticate/register_faculty.html', {'faculty_form':faculty_form, 'registered':registered })

# check if the username already exists
def validate_username(username):
    # username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

# login view
def user_login(request):
    if request.user.is_authenticated:
        return redirect('resources:index')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                current_user = User.objects.get(pk =user.pk)
                if current_user.type == "Student":
                    request.session["department"] = Student.objects.get(pk=user.pk).department.id
                    request.session["semester"] = Student.objects.get(pk=user.pk).semester
                elif current_user.type == "Faculty":
                    request.session["department"] = Faculty.objects.get(pk=user.pk).department.id

                request.session["type"] = current_user.type               
                return redirect('resources:index')
            else:
                login_form = LoginForm()

                return render(request,'authenticate/login.html', {"errors":"Account is not active! Please contact System Adminnistrator!","login_form":login_form})
        else:
            login_form = LoginForm()

            return render(request,'authenticate/login.html', {"errors":"Invalid username or password!","login_form":login_form})
            
    else:
        login_form = LoginForm()
        return render(request, 'authenticate/login.html',{"login_form":login_form})

# logout view
@login_required(login_url="/auth/login")
def user_logout(request):
    logout(request)
    return redirect('resources:index')