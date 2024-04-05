from django import forms


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


class student(forms.Form):
    name = forms.CharField(widget = forms.TextInput)
    email = forms.EmailField(widget = forms.EmailInput)