from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.


def index(request):
   return render(request,'pages/index.html')

def about(request):
    #return HttpResponse('Hello, I am in About!')
    return render(request,'pages/about.html')

def login(request):
    print("IN LOGIN")
    if request.method == 'POST':
    	#Retrieve info
    	username = request.POST['username']
    	password = request.POST['password']

    	user = auth.authenticate(username=username, password=password)
    	if user is not None:
    		#Create the session
    		auth.login(request,user)
    		return redirect('home')
    	else:
    		#messages.error(request,'username or password not correct')
    		print("Username/Password incorrect")
    		return redirect('login')
    else:
    	print("GET")
    	return render(request,'pages/login.html')
