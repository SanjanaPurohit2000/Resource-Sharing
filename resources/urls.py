from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
        path('',views.index,name="index"),
        path('edit/',views.edit_own_resources,name="edit"),
        path('upload/',views.upload_resources,name="upload"),
        path('delete/<int:file_id>/',views.delete_resource,name="delete"),
        path('download/<int:file_id>/',views.download,name="download"),
        path('stu_list/',views.stu_list,name="stu_list"),

]
