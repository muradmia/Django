from django import forms
from .models import Students

class Student(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
