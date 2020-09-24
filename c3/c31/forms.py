from django import forms

class staff_form(forms.Form):
    fullname = forms.CharField(required = True) # True == not null
    email = forms.EmailField(required = False)
    age = forms.IntegerField()
    birthday = forms.DateField(required = False)

class pic_form(forms.Form):
    name = forms.CharField(required = True)
    img = forms.ImageField()