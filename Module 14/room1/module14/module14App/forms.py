from django import forms
from django.core import validators
class LoginForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data['password']
        re_password2 = self.cleaned_data['re_password']
        if password1 != re_password2:
            raise forms.ValidationError("pass does't match password")

    # name = forms.CharField(widget=forms.TextInput)
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_pass = self.cleaned_data['password']
    #     con_pass = self.cleaned_data['confirm_password']
    #     if con_pass != val_pass:
    #         raise forms.ValidationError("password does;t match")