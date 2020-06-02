from django import forms
from .models import User,Student,Faculty,Department,USER_TYPE_CHOICES

# form classes
class StudentForm(forms.ModelForm):        
    password = forms.CharField(widget=forms.PasswordInput(),label="Password")
    department = forms.ModelChoiceField(
            queryset=Department.objects.all(),
            initial=1,
            widget=forms.Select(attrs={'style':'padding:0.8rem 1rem;height:3rem'})
        )
    semester = forms.CharField(widget=forms.TextInput(attrs={'style':'padding:0.8rem 1rem;height:3rem;-moz-appearance:textfield;-webkit-appearance:textfield;margin:0;','pattern':'[0-9]+', 'title':'Enter numbers Only'}),label="Semester")

    class Meta():
        model = Student
        fields = ('username','password','name','enrollment_no', 'semester', 'department')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-user'
            visible.field.widget.attrs['placeholder'] = visible.field.label          

        for field in self.Meta.fields:
            self.fields[field].required = True  

       

class FacultyForm(forms.ModelForm):        
    password = forms.CharField(widget=forms.PasswordInput(),label="Password")
    department = forms.ModelChoiceField(
            queryset=Department.objects.all(),
            initial=1,
            widget=forms.Select(attrs={'style':'padding:0.8rem 1rem;height:3rem'})
        )

    class Meta():
        model = Faculty
        fields = ('username','password','name', 'department')

    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-user'
            visible.field.widget.attrs['placeholder'] = visible.field.label          

        for field in self.Meta.fields:
            self.fields[field].required = True  
        
        
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="Password")

    class Meta():
        model = User
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-user'
            visible.field.widget.attrs['placeholder'] = visible.field.label
