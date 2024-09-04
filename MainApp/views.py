from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from .models import alumni,experience,projects,Seminar



# Create your views here.
context={}

def base(request):
   return render(request,'base.html')

def index(request):
  return render(request,'index.html')
  
def register(request):
  if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        name = request.POST['name']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']        

        # check for errorneous input
        if len(username)>10:
            # messages.error(request, " Your user name must be under 10 characters")
            return redirect('register')

        if not username.isalnum():
            # messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        
        if (pass1!= pass2):
            # messages.error(request, " Passwords do not match")
            return redirect('index')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = name
        myuser.save()
        user=authenticate(username=myuser.username,password=pass1)
        
        login(request,user)
        # messages.success(request, "Account Created Successfully!")
        
        
        return redirect(register)
  return render(request,'customer/register.html',context)


def loginPage(request):
  if request.method == "POST":
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']
    user=authenticate(username=loginusername,password=loginpassword)
    if user is not None:
      login(request,user)
      messages.success(request,"Successfully Logged In!")
      return redirect(index)
    else:
      messages.error(request,"Invalid Credentials")
  return render(request,'login.html',context)
    

def logoutPage(request):
  logout(request)
  return redirect(index)

def profile(request):
  alumni_det = alumni.objects.all()
  exp=experience.objects.all()
  project=projects.objects.all()
  context={'alumni':alumni_det,
           'project':project,
           'exp':exp
          }
  print(alumni)
  return render(request,'alumni_profile.html',context)

def seminar(request):
  seminar = Seminar.objects.all()
  context={'seminar':seminar}
  return render(request,'seminar.html',context)

def success(request):
    if request.method == 'POST':
        story = request.POST.get('story')
        alumni = alumni.objects.filter(user=request.user)
        # success = Success.objects.create()
        context = {
            'alumni' : alumni ,
            'success' : success,
        }
        return redirect(home,context)
      
def alumregister(request):
  # if request.method == "POST":
    
    
  # pass
  # if method
  return render(request,'alumni_register.html')
  
  

