from django import forms
from django.forms import ModelForm
from micro_admin.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'gender', 'branch', 'user_roles', 'username', 'password']

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


class ClientsForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=255,required=False)
    account_type = forms.CharField(max_length=20)
    account_number = forms.CharField(max_length=50)
    branchid = forms.IntegerField()
    date_of_birth = forms.DateField()
    blood_group = forms.CharField(max_length=10,required=False)
    occupation = forms.CharField(max_length=200)
    annual_income = forms.IntegerField()
    gender = forms.CharField(max_length=10)
    clent_role = forms.CharField(max_length=20)
    joined_date = forms.DateField()
    country = forms.CharField(max_length=50,required=False)
    state = forms.CharField(max_length=50,required=False)
    district = forms.CharField(max_length=50,required=False)
    city = forms.CharField(max_length=50,required=False)
    area = forms.CharField(max_length=150,required=False)
    mobile = forms.CharField(required=False)
    pincode = forms.CharField(required=False)

