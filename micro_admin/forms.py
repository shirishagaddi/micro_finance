from django import forms
from micro_admin.models import Branch

class BranchForm(forms.Form):
    name = forms.CharField(max_length=100)
    opening_date = forms.DateField()
    country = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    district = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    area = forms.CharField(max_length=150)
    phone_number = forms.IntegerField()
    pincode = forms.IntegerField()

