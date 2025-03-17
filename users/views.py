from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm

from django.contrib.auth.models import User
from .models import Profile

from django.contrib import messages #flash messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def profiles(request):
    profiles=Profile.objects.all()
    context={
        'profiles':profiles
    }
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topSkills=profile.skill_set.exclude(description__exact="")
    otherSkills=profile.skill_set.filter(description="")
    context={
        'profile':profile,
        'topSkills':topSkills,
        'otherSkills':otherSkills
    }
    return render(request,'users/user-profile.html',context)

def loginUser(request): # the request is GET request first to acess the localhost:8000/login/ ---->then next time when the user submits the form request is POST
    page="login"
    context={
        'page':page
    }
    
    #edge case if the user is already login and the request is made he should not see the login page [when making a get request to localhost:3000/login and the user is already login]
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=='POST':
        #access the username and the password from the request object of 'POST' type url
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username) #make sure that username exist in the database
           
        except:
            messages.error(request,'Username does not exist')
            
           

        user=authenticate(request,username=username,password=password) # query the database to check if a user with credential is present in the datbase an it will get that user

        if user is not None:
            login(request,user) #this will create a session for this user in the database
            #and also it is going to get that session and add it into our browser cookies
            return redirect('profiles')
        else:
            messages.error(request,"username or password is incorrect")
    return render(request,'users/login_register.html',context)

def logoutUser(request):
    logout(request) # this delete the session
    #after loging out take the user to the login page
    messages.info(request,'User was logged out!')
    return redirect('login')



def registerUser(request):
    page='register'
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            # directly we can just say  ->>>>   form.save()
            user=form.save(commit=False)
            #converting the username of anytype to complete lowercase
            user.username=user.username.lower()
            user.save()
            messages.success(request,'User account was created successfully!')
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'An error has occurred during registration!')


    context={
     'page':page,
     'form':form
    }
    return render(request,'users/login_register.html',context)



@login_required(login_url='login')
def userAccount(request):                  #request.user->logged in user
    profile=request.user.profile
    skills=profile.skill_set.all()
    projects=profile.project_set.all()
    
    context={
        'profile':profile,
        'skills':skills,
        'projects':projects
    }
    return render(request,'users/account.html',context)




        