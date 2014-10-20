from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required=False)
    gender = forms.CharField(max_length=10)
    branchid = forms.IntegerField()
    user_roles = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(required=False)
    email = forms.EmailField(max_length=255)
    mobile = forms.IntegerField(required=False)
    country = forms.CharField(required=False)
    state = forms.CharField(required=False)
    district = forms.CharField(required=False)
    city = forms.CharField(required=False)
    area = forms.CharField(required=False)
    pincode = forms.IntegerField(required=False)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)
