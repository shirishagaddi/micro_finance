from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
from micro_admin.forms import BranchForm,ClientsForm
from micro_admin.models import Branch,Clients
from django.views.decorators.csrf import csrf_exempt
import datetime

def base(request):
    return render_to_response('base.html')

def login(request):
    return render_to_response('login.html')

def create_branch(request):
    if request.method == 'GET':
        return render(request, 'branchcreate.html')
        print "hai"
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
            return render_to_response("successfuly_clientcreated.html" ,{'client':client })
        else:
            return HttpResponse("Invalid Data")


def client_list(request):
    return render(request,'list_of_clients.html')

def update_profile(request,client):
    if request.method =='GET':
        client = Clients.objects.get(id=client)
        return render(request,'update_clientprofile.html',{'client':client})
    else:
        print 'hi'
        client = Clients.objects.get(id=client)
        photo=request.FILES.get("photo")
        signature = request.FILES.get("signature")
        client.photo = photo
        client.signature = signature
        client.save()
        return render_to_response('uploaded_successfully.html')

def deleteclient_profile(request,client):
    client = Clients.objects.get(id=client)
    client.delete()
    return HttpResponse('Deleted Client Profile')



            

