from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout

from django.contrib.auth.models import User
from .models import Profile

from django.contrib import messages #flash messages

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
    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request) # this delete the session
    #after loging out take the user to the login page
    messages.success(request,'User was logged out!')
    return redirect('login')


        



        # action="{%url 'login'%}" after submiting the form routed to the same page


    #this will be done after the get request to the url localhost:8000/login/
    return render(request,'users/login_register.html')# login page is rendered