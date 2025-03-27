from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .models import Project,Tag,Review

from .forms import ProjectForm

def projects(request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    context={'project':projectobj}
    print(projectobj.featured_image.url)
    return render(request,'projects/single-project.html',context)

@login_required(login_url='login')# if the user is not logged in and they try Add Project then they are redirected to the login page
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()

    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')
        
    context={
        'form':form
    }
    return render(request,'projects/project_form.html',context)




"""
Let's break down the logic of form.save(commit=False) in your Django createProject view:

Understanding form.save()

When you call form.save(), Django does two main things:
It creates a new database object (in this case, a Project object) with the data from the form.
It immediately saves that object to the database (commits the changes).
The Role of commit=False

commit=False tells Django: "Create the object, but don't save it to the database yet."
Why would you want to do that?
Adding or modifying data before saving: In your case, you need to set the owner field of the Project object to the current user's profile (profile). You can only do this after the object is created but before it's saved.
Performing additional validation or processing: You might want to perform other checks or modifications on the object before it's permanently stored in the database.
Handling relationships: when dealing with many to many relationships, or other complex relations, it is sometimes neccesary to save the object first, before adding related items.
Step-by-Step Logic in Your Code

project = form.save(commit=False):
This creates a Project object from the form data, but it's not yet in the database.
project.owner = profile:
This sets the owner field of the Project object to the current user's profile.
project.save() (Implicit):
although not explicitly written in the code you provided, it is implied that after the owner is set, that you would then save the project to the database. if you do not save the project, it will not be stored in the database.
return redirect('projects'):
After the project is saved with the correct owner, the user is redirected to the 'projects' page.

"""




@login_required(login_url='login')
def updateProject(request,pk):
    #project=request.user.project
    #project=Project.objects.get(id=pk)

#such that only owner can update the project
    profile=request.user.profile
    project =profile.project_set.get(id=pk)

    form=ProjectForm(instance=project)
      #request is the object that carries the url information like form post data and files uploads
      #request.FILES->to deal with file uploads by user
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
        
    context={
        'form':form
    }
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    #project=Project.objects.get(id=pk)

    #make sure that only the owner can delete his projects and this would prevent hardcoding url from deleting from the other profiles

    profile=request.user.profile
    project=profile.project_set.get(id=pk)



    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request,'delete_template.html',context)  
