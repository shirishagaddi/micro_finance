from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from micro_admin.models import User, Branch, Clients, Groups, Centers
from micro_admin.forms import UserForm, BranchForm, ClientsForm, GroupsForm, CentersForm
import datetime
from django.core.urlresolvers import reverse


def index(request):
    return render_to_response('base.html')


@csrf_exempt
def user_login(request):
    if request.user.is_authenticated():
        username = request.user
        user = User.objects.get(username=username)
        return render_to_response('index.html', {'user': user})
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
    users_list = User.objects.all()
    return render(request, 'list_of_users.html', {'users_list':users_list})


def groupslist(request):
    groups_list = Groups.objects.all()
    return render(request, 'list_of_groups.html', {'groups_list':groups_list})


def centerslist(request):
    centers_list = Centers.objects.all()
    return render(request, 'list_of_centers.html', {'centers_list':centers_list})


@csrf_exempt
def createuser(request):
    if request.method=="GET":
        branch = Branch.objects.all()
        return render(request, 'createuser.html', {'branch':branch})
    else:
        print request.POST
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print user_form.errors
            user_name = request.POST.get('username')
            user_password = request.POST.get('password')
            user = User.objects.create_user(username=user_name, password=user_password, branch=Branch.objects.get(id=request.POST.get('branch')))
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.gender = request.POST.get('gender')
            user.user_roles = request.POST.get('user_roles')
            user.email = request.POST.get('email')
            user.country = request.POST.get('country')
            user.state = request.POST.get('state')
            user.district = request.POST.get('district')
            user.city = request.POST.get('city')
            user.area = request.POST.get('area')
            user.pincode = request.POST.get('pincode')
            date_of_birth1 = request.POST.get("date_of_birth")
            mobile1 = request.POST.get('mobile')
            if mobile1:
                user.mobile = mobile1
            if date_of_birth1:
                datestring_format = datetime.datetime.strptime(request.POST.get("date_of_birth"),'%m/%d/%Y').strftime('%Y-%m-%d')
                dateconvert = datetime.datetime.strptime(datestring_format, "%Y-%m-%d")
                user.date_of_birth = dateconvert
            user.save()
            return HttpResponse("User created sucessfully")
        else:
            print user_form.errors
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
            return render_to_response("branch_profile.html", {'branch':branch})
        else:
            return HttpResponse("Invalid Data")


def branchprofile(request, branch):
    branch = Branch.objects.get(id=branch)
    return render(request, 'branch_profile.html', {'branch':branch})


def branch_list(request):
    branches_list = Branch.objects.all()
    return render(request,'list_of_branches.html',{'branches_list':branches_list })


@csrf_exempt
def create_client(request):
    if request.method == 'GET':
        branch = Branch.objects.all()
        return render(request, 'clientcreation.html',{'branch':branch})
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
            return render_to_response("client_profile.html" ,{'client':client })
        else:
            return HttpResponse("Invalid Data")


def client_list(request):
    clients_list = Clients.objects.all()
    return render(request,'list_of_clients.html',{'clients_list':clients_list})


def update_profile(request,client):
    if request.method =='GET':
        client = Clients.objects.get(id=client)
        return render(request,'update_clientprofile.html',{'client':client})
    else:
        client = Clients.objects.get(id=client)
        photo=request.FILES.get("photo")
        signature = request.FILES.get("signature")
        client.photo = photo
        client.signature = signature
        client.save()
        return render_to_response('client_profile.html',{'client':client })


def clientprofile(request, client):
    client = Clients.objects.get(id=client)
    return render(request, 'client_profile.html', {'client':client})


def deleteclient_profile(request,client):
    client = Clients.objects.get(id=client)
    client.delete()
    return HttpResponse('Deleted Client Profile')


@csrf_exempt
def create_group(request):
    if request.method == "GET":
        branches = Branch.objects.all()
        clients = Clients.objects.all()
        return render(request, 'creategroup.html', {'branches':branches, 'clients':clients})
    else:
        group_form = GroupsForm(request.POST)
        if group_form.is_valid():
            name = request.POST.get('name')
            account_type = request.POST.get('account_type')
            account_number = request.POST.get('account_number')
            datestring_format = datetime.datetime.strptime(request.POST.get("activation_date"),'%m/%d/%Y').strftime('%Y-%m-%d')
            dateconvert = datetime.datetime.strptime(datestring_format, "%Y-%m-%d")
            activation_date = dateconvert
            branch = Branch.objects.get(id=request.POST.get('branch'))
            clients = request.POST.getlist('clients')
            group = Groups.objects.create(name=name, account_type=account_type, account_number=account_number, activation_date=activation_date, branch=branch)
            for client in clients:
                client = Clients.objects.get(id=client)
                group.clients.add(client)
                group.save()
            data = {'error':False, 'group_id':group.id}
            return HttpResponse(json.dumps(data))
        else:
            data = {'error':True, 'message':group_form.errors}
            return HttpResponse(json.dumps(data))


@csrf_exempt
def create_center(request):
    if request.method == "GET":
        branches = Branch.objects.all()
        groups = Groups.objects.all()
        return render(request, 'createcenter.html', {'branches':branches, 'groups':groups})
    else:
        center_form = CentersForm(request.POST)
        if center_form.is_valid():
            name = request.POST.get('name')
            datestring_format = datetime.datetime.strptime(request.POST.get("created_date"),'%m/%d/%Y').strftime('%Y-%m-%d')
            dateconvert = datetime.datetime.strptime(datestring_format, "%Y-%m-%d")
            created_date = dateconvert
            branch = Branch.objects.get(id=request.POST.get('branch'))
            groups = request.POST.getlist('groups')
            center = Centers.objects.create(name=name, created_date=created_date, branch=branch)
            for group in groups:
                group = Groups.objects.get(id=group)
                center.groups.add(group)
                center.save()
            data = {'error':False, 'center_id':center.id}
            return HttpResponse(json.dumps(data))
        else:
            data = {'error':True, 'message':center_form.errors}
            return HttpResponse(json.dumps(data))


@csrf_exempt
def searchcenter(request):
    if request.method == "POST":
        if request.POST.get('searchelement'):
            branch = Branch.objects.get(name=request.POST.get('searchelement'))
            centers_list = Centers.objects.filter(branch=branch.id)
            return render(request, 'list_of_centers.html', {'centers_list':centers_list})
        else:
            return HttpResponse("Please type the name of the branch to search")


@csrf_exempt
def searchgroup(request):
    if request.method == "POST":
        if request.POST.get('searchelement'):
            branch = Branch.objects.get(name=request.POST.get('searchelement'))
            groups_list = Groups.objects.filter(branch=branch.id)
            return render(request, 'list_of_groups.html', {'groups_list':groups_list})
        else:
            return HttpResponse("Please type the name of the branch to search")


@csrf_exempt
def searchuser(request):
    if request.method == "POST":
        if request.POST.get('searchelement'):
            branch = Branch.objects.get(name=request.POST.get('searchelement'))
            users_list = User.objects.filter(branch=branch.id)
            return render(request, 'list_of_users.html', {'users_list':users_list})
        else:
            return HttpResponse("Please type the name of the branch to search")


def userprofile(request, user_id):
    userobject = User.objects.get(id=user_id)
    return render(request, 'user_profile.html', {'userobject':userobject})


def groupprofile(request, group_id):
    group = Groups.objects.get(id=group_id)
    clients_list = group.clients.all()
    active_clients_count = group.clients.filter(is_active=1).count()
    centers_list = group.centers_set.all()
    return render(request, 'group_profile.html', {'group':group, 'centers_list':centers_list,'clients_list':clients_list, 'active_clients_count':active_clients_count})


def centerprofile(request, center_id):
    center = Centers.objects.get(id=center_id)
    groups_list = center.groups.all()
    active_groups_count = center.groups.filter(is_active=1).count()
    active_groups_list = center.groups.filter(is_active=1)
    active_clients_count=0
    for active_group in active_groups_list:
        active_clients_count += active_group.clients.filter(is_active=1).count()
    return render(request, 'center_profile.html', {'centerobject':center, 'groups_list':groups_list,'active_groups_count':active_groups_count,'active_clients_count':active_clients_count})

