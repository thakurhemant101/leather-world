from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
import time

#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
	def middleware(request):
		if request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/login/' or request.path=='/service/' or request.path=='/register/':
			request.session['sunm']=None
			request.session['srole']=None
			response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware

def home(request):
 return render(request,"home.html")

def about(request):
 return render(request,"about.html")

def ajaxResponse(request): 
 return HttpResponse("Its AJAX code working , Django");

def contact(request):
 return render(request,"contact.html")

def service(request):
 return render(request,"service.html",)

def register(request):
 if request.method=="GET":   
  return render(request,"register.html",{"output":""})
 else:   
  #recieve data on UI
  name=request.POST.get("name")
  username=request.POST.get("username")
  password=request.POST.get("password")
  mobile=request.POST.get("mobile")
  address=request.POST.get("address")
  city=request.POST.get("city")
  gender=request.POST.get("gender")
  dt=time.asctime()
  #print(request.POST)     

  p=models.Register(name=name,username=username,password=password,mobile=mobile,address=address,city=city,gender=gender,status=0,role="user",dt=dt)
  p.save()
  return render(request,"register.html",{"output":"User Register Successfully...."})

def checkEmailAJAX(request):
  emailid=request.GET.get("emailid")
  result=models.Register.objects.filter(username__contains=emailid)
  if len(result)>0:
   return HttpResponse(1)
  else:
   return HttpResponse(0)

def login(request):
  cunm,cpass="",""
  if request.COOKIES.get("cunm")!=None:
    cunm=request.COOKIES.get("cunm")
    cpass=request.COOKIES.get("cpass")
  if request.method=="GET":
    return render(request,"login.html",{"output":"","cunm":cunm,"cpass":cpass})
  else:
    username=request.POST.get("username")
    password=request.POST.get("password")
    chk=request.POST.get("chk")
    print(chk)

    userDetails=models.Register.objects.filter(username=username,password=password,status=1)
  
  if len(userDetails)>0:
    #to store user details in session
    request.session['sunm']=userDetails[0].username
    request.session['srole']=userDetails[0].role

    if userDetails[0].role=="admin":
      response=redirect("/myadmin/")
    else:
      response=redirect("/user/")
   
   #to store user details in cookies
    if chk!=None:
      response.set_cookie("cunm",username,max_age=3600)
      response.set_cookie("cpass",password,max_age=3600)

    return response      

  else:
    return render(request,"login.html",{"output":"Invalid user or verify your account....","cunm":cunm,"cpass":cpass})