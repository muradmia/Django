from django import forms
from .models import Profiles

class Profile_form(forms.ModelForm):
    class Meta:
        model = Profiles
        fields ='__all__'

