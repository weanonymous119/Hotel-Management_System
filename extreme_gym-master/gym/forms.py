from django import forms

class User_form(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    age = forms.IntegerField()
    contact_number =forms.CharField(max_length=50)
    joining_date = forms.DateField()

