from django import forms
from django.core import validators


# wirgets == field to html input
class contact(forms.Form):
    name = forms.CharField(label='Full Name : ',initial="Rahim",help_text='Enter your name',required=False,disabled=False,widget = forms.Textarea(attrs = {'id' : 'textarea','class' : 'class1 class2'}))
    file = forms.FileField()
    email = forms.EmailField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs = {'type' : 'date'}))
    appointment = forms.DateTimeField()
    CHOIDES = [('s','Small'),('M',"Medium"),('L',"Large")]
    size = forms.ChoiceField(choices=CHOIDES)


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Erorr")
class student(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message="please enter at list 10 chracter")])
    emai = forms.EmailField(widget = forms.EmailInput,validators=[validators.EmailValidator("enter a valid email")])
    age = forms.IntegerField()
    # file = forms.FileField(validators = [validators.FileExtensionValidator(allowed_extensions=['pdf'])])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("enter a name arlist 10 chracter")
    #     return valname

    #    
    #     if '.com' not in valemail:
            
    #         raise forms.ValidationError("enter a correct email")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname =self.cleaned_data['name']
    #     valemail = self.cleaned_data['emai']

    #     if len(valname) < 10:
    #         raise forms.ValidationError("enter a name arlist 10 chracter")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("enter a correct email")

class password_check(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        if con_pass != val_pass:
            raise forms.ValidationError("password does;t match")
