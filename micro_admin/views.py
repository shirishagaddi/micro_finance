from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from micro_admin.models import User, Branch
from micro_admin.forms import UserForm

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
            print user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.gender = request.POST.get('gender')
            user.user_roles = request.POST.get('user_roles')
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