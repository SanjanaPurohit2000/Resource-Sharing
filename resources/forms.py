from django import forms
from .models import Resources

class FileUploadForm(forms.ModelForm):
    class  Meta:
        model = Resources
        fields = ('name','link_to_resource','type_id')
    
class EditFileForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ('name','link_to_resource','type_id')
    
    