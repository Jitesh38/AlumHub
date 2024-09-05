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
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        
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
          myuser.is_staff=True
          myuser.save()          
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
  if request.method == "POST":
    profilePic = request.POST['profilePic']
    course = request.POST['course']   
    startYear = request.POST['startYear'] 
    endYear = request.POST['endYear'] 
    gpa = request.POST['gpa']      
    alum = alumni(user=request.user,profile=profilePic,course=course,startyear=startYear,endyear=endYear,gpa=gpa)
    alum.save()
    messages.success(request,'Profile Updated Successfully')
    return redirect(alumExp)  
  return render(request,'alumni_register.html')  
    

def logoutPage(request):
  logout(request)
  messages.success(request,'Log out Successfully')
  return redirect(index)

def profile(request,slug):
  user=User.objects.get(username = slug)
  alumni_det = alumni.objects.filter(user = user).first()
  exp=experience.objects.filter(alumni=alumni_det)
  project=projects.objects.filter( alumni = alumni_det )
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


def alumniFunc(request):
  alumnis = alumni.objects.all()
  context={'alumni':alumnis}
  return render(request,'alumni_all.html',context)

def search(request):
  if request.method == 'GET':
    search = request.GET['search']
    if len(search) > 70:
        messages.error(request, "Enter a Valid Keyword to Search")
        alumnis = alumni.objects.none()            
    else:
      userFname=User.objects.filter(first_name__icontains=search)
      userLname=User.objects.filter(last_name=search)
      alluser=userFname.union(userLname)[0]
      alumnis=alumni.objects.filter(user=alluser)
      if alumnis.count() == 0:
        messages.warning(request, "Search Results not found.")
          #is staff logic
      else:
        context={'alumni':alumnis,'search':search}
        print(alumni)
        return render(request,'alumni_all.html',context)
  return redirect(alumniFunc)

def alumExp(request):
  if request.method == "POST":
    companyName = request.POST['companyName']
    yearsOfExperience = request.POST['yearsOfExperience']   
    print(companyName,yearsOfExperience)
    alumni1=alumni.objects.filter(user=request.user).first()
    exp=experience(alumni=alumni1,companyname=companyName,year=yearsOfExperience)
    exp.save()  
    print(alumni1)
    messages.success(request,"Added Experience Successfully.")
    return redirect(alumProject)
  return render(request,'alumni_exp.html') 



def alumProject(request):
  if request.method == "POST":
    projectName = request.POST['projectName']
    projectDescription = request.POST['projectDescription']   
    projectLink = request.POST['projectLink']   
    print(projectName,projectDescription,projectLink)
    alumni1=alumni.objects.filter(user=request.user).first()
    pr=projects(alumni=alumni1,projectname=projectName,projectdetails=projectDescription,link=projectLink)
    pr.save()  
    messages.success(request,"Added Education Details Successfully.")
    return redirect(alumProject)
  return render(request,'alumni_project.html') 

# def success(request):
#     if request.method == 'POST':
#         story = request.POST.get('story')
#         alumni = alumni.objects.filter(user=request.user)
#         # success = Success.objects.create()
#         context = {
#             'alumni' : alumni ,
#             'success' : success,
#         }
#         return redirect(home,context)  
