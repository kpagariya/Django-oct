from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User

from .models import PLanguage
# Create your views here.


def index(request):
   return render(request,'pages/index.html')

def about(request):
    #return HttpResponse('Hello, I am in About!')
    return render(request,'pages/about.html')

def welcome(request):
    #return HttpResponse('Hello, I am in About!')
    return render(request,'pages/welcome.html')

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
    		#Return to welcome page
    		return redirect('welcome')
    	else:
    		#messages.error(request,'username or password not correct')
    		print("Username/Password incorrect")
    		return redirect('login')
    else:
    	print("GET")
    	return render(request,'pages/login.html')

def pLangVote(request):
	if request.method == 'POST':
		# Retrive all selected languages
		mySelectedLangsList=request.POST.getlist('txtVote')
		for selectedLang in mySelectedLangsList:
			#Select name,vcount from planguage where name="SelectedLang"
			record = PLanguage.objects.get(name=selectedLang)
			if record:
				#print(ret.name)
				#print(ret.vcount)
				record.vcount=record.vcount+1
				# Update query
				record.save()
			else:
				print("ERROR")
		
		return render(request,'pages/index.html')
	else:
		# Request is GET
		#Select * from planguage
		allLanguages = PLanguage.objects.all()
		print(allLanguages)
		# Pass the context to vote html page
		context = {'allLangs' : allLanguages}
		return render(request,'pages/vote.html',context)
