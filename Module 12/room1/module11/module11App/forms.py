from django import forms

class contact(forms.Form):
    name = forms.CharField(label='username')
    email = forms.EmailField()