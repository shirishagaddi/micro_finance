from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from micro_admin.models import User, Branch, Clients
from micro_admin.forms import UserForm, BranchForm, ClientsForm
import datetime

def index(request):
    return render_to_response('base.html')

@csrf_exempt
def user_login(request):
    if request.user.is_authenticated():
        return render_to_response('index.html')
    if request.method=="GET":
        data = {}
        return render_to_response('login.html', {'data':data})
    else:
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data = {'error':False}
            else:
                data = {'error':True, 'message':"User is not active."}
        else:
            data = {'error':True, 'message':"Username and Password were incorrect."}
        return HttpResponse(json.dumps(data))

def user_logout(request):
    if not request.user.is_authenticated():
        return HttpResponse('')
    logout(request)
    return HttpResponseRedirect('/')

def userslist(request):
    return HttpResponse("Dispalys users list")

@csrf_exempt
def createuser(request):
    if request.method=="GET":
        branch = Branch.objects.all()
        return render_to_response('createuser.html', {'branch':branch})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = request.POST.get('user_name')
            user_password = request.POST.get('user_password')
            branchid = request.POST.get('branchid')
            branch = Branch.objects.get(id=branchid)
            user = User.objects.create_user(username=user_name, password=user_password, branch=branch)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.gender = request.POST.get('gender')
            user.user_roles = request.POST.get('user_roles')
            datestring_format = datetime.datetime.strptime(request.POST.get("date_of_birth"),'%m/%d/%Y').strftime('%Y-%m-%d')
            dateconvert = datetime.datetime.strptime(datestring_format, "%Y-%m-%d")
            user.date_of_birth = dateconvert
            user.email = request.POST.get('email')
            user.mobile = request.POST.get('mobile')
            user.country = request.POST.get('country')
            user.state = request.POST.get('state')
            user.district = request.POST.get('district')
            user.city = request.POST.get('city')
            user.area = request.POST.get('area')
            user.pincode = request.POST.get('pincode')
            user.save()
            return HttpResponse("User created sucessfully")
        else:
            return HttpResponse("Invalid Data")

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
            return render_to_response("successfuly_branchcreated.html", {'branch':branch})
        else:
            return HttpResponse("Invalid Data")

@csrf_exempt
def create_client(request):
    if request.method == 'GET':
        branch = Branch.objects.all()
        return render_to_response('clientcreation.html',{'branch':branch})
    else:
        form = ClientsForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            gender = request.POST.get("gender")
            branchid = request.POST.get("branchid")
            branch=Branch.objects.get(id=request.POST.get("branchid"))
            clent_role = request.POST.get("clent_role")
            datestring_format = datetime.datetime.strptime(request.POST.get("joined_date"),'%m/%d/%Y').strftime('%Y-%m-%d')
            dateconvert=datetime.datetime.strptime(datestring_format, "%Y-%m-%d")
            joined_date = dateconvert
            birth_datestring_format = datetime.datetime.strptime(request.POST.get("date_of_birth"),'%m/%d/%Y').strftime('%Y-%m-%d')
            birth_dateconvert=datetime.datetime.strptime(birth_datestring_format, "%Y-%m-%d")
            date_of_birth = birth_dateconvert
            account_type = request.POST.get("account_type")
            account_number = request.POST.get("account_number")
            occupation = request.POST.get("occupation")
            annual_income = request.POST.get("annual_income")
            blood_group = request.POST.get("blood_group")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            country = request.POST.get("country")
            state = request.POST.get("state")
            district = request.POST.get("district")
            city = request.POST.get("city")
            area = request.POST.get("area")
            pincode = request.POST.get("pincode")
            client = Clients.objects.create(first_name=first_name,last_name=last_name,gender=gender,date_of_birth=date_of_birth,clent_role=clent_role,mobile=mobile,joined_date=joined_date,account_number=account_number,branch=branch,account_type=account_type,email=email,country=country,state=state,district=district,city=city,area=area,pincode=pincode,occupation=occupation,annual_income=annual_income,blood_group=blood_group)
            return HttpResponse("Client Successfully Registered")
        else:
            return HttpResponse("Invalid Data")
