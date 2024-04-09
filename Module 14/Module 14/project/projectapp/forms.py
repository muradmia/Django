from django import forms
from .models import student
class students(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
        labels ={
            'name' : "Studnet Name :",
            'roll' : "Student Roll",

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'btn-danger'}),
            # 'roll' : forms.PasswordInput()
        }
        erorr_mesages = {
            'name'  : {'required': 'please enter your name'}
        }