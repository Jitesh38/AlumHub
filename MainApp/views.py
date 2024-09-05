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
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']        
        role = request.POST['role']        

        # check for errorneous input
        # if len(username)>10:
        #     # messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('register')

        # if not username.isalnum():
        #     # messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('index')
        
        if (pass1!= pass2):
            messages.error(request, "Passwords do not match")
            return redirect('index')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name=lname
        myuser.save()
        user=authenticate(username=myuser.username,password=pass1)        
        login(request,user)
        messages.success(request, "Account Created Successfully!") 
        request.session['role'] = role
        if role == 'alumni':
          return redirect(alumregister)        
        return redirect(index)

  return render(request,'register.html',context)


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


def alumregister(request):
  # if  request.session['role'] != 'alumni':
  #   return redirect(index)
  if request.method == "POST":
    profilePic = request.POST['profilePic']
    course = request.POST['course']   
    startYear = request.POST['startYear'] 
    endYear = request.POST['endYear'] 
    gpa = request.POST['gpa']  
    
    alum = alumni(user=request.user,profile=profilePic,course=course,startyear=startYear,endyear=endYear,gpa=gpa)
    alum.save()
    messages.success(request,'Profile Updated Successfully')
    return redirect(index)
  
  return render(request,'alumni_register.html')
  # if request.method == "POST":
    
    
  # pass
  # if method
  
    

def logoutPage(request):
  logout(request)
  return redirect(index)

def profile(request,slug):
  user=User.objects.get(username = slug)
  alumni_det = alumni.objects.filter(user = user).first()
  exp_all=experience.objects.filter(alumni=alumni_det).first()
  exp=experience.objects.filter(alumni=alumni_det).first()
  project=projects.objects.filter(company = exp )
  context={'alumni':alumni_det,'exp':exp,'project':project}
  print(user)
  print(alumni_det)
  print(exp)
  print(project)
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
