from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from micro_admin.models import User

# Create your views here.
def index(request):
    #return HttpResponse("MicroAdmin Index Page")
    return render_to_response('base.html')

@csrf_exempt
def login(request):
    if request.user.is_authenticated():
        return render_to_response('index.html')
    if request.method=="GET":
        data = {}
        return render_to_response('login.html', {'data':data})
    else:
        print "Post method"
        user_username = request.POST.get('user_username')
        user_password = request.POST.get('user_password')
        #user = authenticate(username=user_username, password=user_password)
        user = User.objects.get(username=user_username, password=user_password)
        if user is not None:
            if user.is_active:
                #login(request, user)
                data = {'error':False}
            else:
                data = {'error':True, 'message':"User is not active."}
        else:
            data = {'error':True, 'message':"Username and Password were incorrect."}
        return HttpResponse(json.dumps(data))

def sucesslogin(request):
    print request.user
    return render_to_response('index.html')