from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from micro_admin.forms import BranchForm
from micro_admin.models import Branch
import datetime


def base(request):
    return render_to_response('base.html')

def login(request):
    return render_to_response('login.html')

def create_branch(request):
    if request.method == 'GET':
        return render(request, 'branchcreate.html')
    else:
        form = BranchForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            datestring_format = datetime.datetime.strptime(request.POST.get("opening_date"),'%m/%d/%Y').strftime('%Y-%m-%d')
            dateconvert=datetime.datetime.strptime(datestring_format, "%Y-%m-%d")
            opening_date = dateconvert
            country = request.POST.get("country")
            state = request.POST.get("state")
            district = request.POST.get("district")
            city = request.POST.get("city")
            area = request.POST.get("area")
            phone_number = request.POST.get("phone_number")
            pincode = request.POST.get("pincode")
            branch = Branch.objects.create(name=name,opening_date=opening_date,country=country,state=state,district=district,city=city,area=area,phone_number=phone_number,pincode=pincode)
            return HttpResponse("Sucessfully Registered")
        else:
            return HttpResponse("Invalid Data")

