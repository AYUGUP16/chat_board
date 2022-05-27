from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as aj_login,logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
import json

# Create your views here.
def hello(request):
    return render(request, 'login.html', {})

def signup(request):
    if request.method=="POST":
        usename=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if(pass1!= pass2):
            messages.error(request,"Enter correct password")
            return redirect('/login')
        else:
            myuser=User.objects.create_user(usename,email,pass1)
            myuser.save()
            return redirect('/login')


def home(request):
    return render(request,'index.html')

def handlelogin(request):
    if request.method == "POST":
        logusername=request.POST['usen']
        logpas=request.POST['pas']
        user = authenticate(username=logusername, password=logpas)
        if user is not None:
            aj_login(request,user)
            messages.success(request,"successfully loged in")
            return redirect('/home')
        else:
            return redirect('/login')

def handlelogout(request):
    logout(request)
    return redirect('/login')

def chat(request):
    return render(request,'chat.html')

@csrf_exempt
def chatbot(request):
    data = json.loads(request.body.decode("utf-8"))
    message = data['message']
    if "hi" in message.lower():
        return JsonResponse({"count":5,"messages":["Welcome to poornima "+request.user.username,"What kind of query do you have?"]})
    elif "admission" in message.lower():
        return JsonResponse({"count":5,"messages":["Thanks for asking, here are the details","For PIET Contact on 9509509507", "For PCE Contact 9509509507", "For PGI Contact 9509509507", "https://www.poornima.org/btech-at-poornima-group-of-colleges/"]})
    elif "placement" in message.lower():
        return JsonResponse({"count":7,"messages":["You would be amazed!!, here are our top companies.","1. Morgan Stanely", "2. Cognizant", "3. Capgemini", "Anything else?","refer to follow link","https://www.poornima.org/placement/overview/"]})
    elif "annual fests" in message.lower():
        return JsonResponse({"count":5,"messages":["You would be amazed!!, here are our top fests.","1. ARROHAN", "2. AADHAR", "3.KALANIDHI", "Anything else?"]})
    elif "hostel" in message.lower():
        return JsonResponse({"count":6,"messages":[" here are our hostels.","1. gurushikhar", "2. gayatri", "3. aravali", "Anything else?","https://www.poornima.org/hostel/basic-essentials/"]})
    elif "papers" in message.lower():
        return JsonResponse({"count":2,"messages":["refer to follow link:-","https://coolcollegebuddy.herokuapp.com/"]})
    elif "alumni" in message.lower():
        return JsonResponse({"count":2,"messages":["refer to follow link","http://pcas.poornima.org/"]})
    
    else:
        return JsonResponse({"mja":"Kon h be"})