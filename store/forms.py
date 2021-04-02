from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=100)
    flower_id = forms.IntegerField()