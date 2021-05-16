from django import forms
from teacher.models import TeacherDetails

class TeacherDetailsForm(forms.ModelForm):
    
    class Meta:
        model = TeacherDetails
        exclude = ['slug']