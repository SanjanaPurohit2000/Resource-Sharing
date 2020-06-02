from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from .forms import *
from .models import Resources
from authenticate.models import User, Student,Faculty
import mimetypes
import os
from share.settings import MEDIA_DIR


# Create your views here.
@login_required(login_url="/auth/login/")
def index(request):
    data_student = Resources.objects.filter(user_id__in = Student.objects.filter(department=request.session["department"]))
    data_faculty = Resources.objects.filter(user_id__in = Faculty.objects.filter(department=request.session["department"]))
    return render(request,"resources/dashboard.html",{'data_student':data_student , 'data_faculty':data_faculty})


def upload_resources(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.user_id = request.user
            file.save()
            status = "Success"
            message = "File Uploaded Successfully!!"
            form = FileUploadForm()
            return render(request,'resources/upload_file.html',{'status':status,'message':message,'form':form})
            
    else:
        form = FileUploadForm()
        return render(request,'resources/upload_file.html',{'form':form})

def edit_own_resources(request):
    data = Resources.objects.filter(user_id=request.user)
    print(data)
    return render(request,"resources/edit.html",{'data': data})


def delete_resource(request,file_id):

    data = Resources.objects.filter(pk=file_id)
    data.delete()
    data1 = Resources.objects.filter(user_id=request.user)
    return render(request,"resources/edit.html",{'data': data1})

def download(request,file_id):
    # fill these variables with real values
    filename = Resources.objects.filter(id=file_id).values('link_to_resource')[0]['link_to_resource']
    fl_path = os.path.join(MEDIA_DIR,filename)
    return serve(request, os.path.basename(fl_path), os.path.dirname(fl_path))


def stu_list(request):
    obj = Student.objects.all()
    return render(request,"resources/studentData.html",{'obj':obj})