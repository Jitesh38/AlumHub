from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout




# Create your views here.
context={}

def home(request):
  return render(request,'base.html')
  
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


