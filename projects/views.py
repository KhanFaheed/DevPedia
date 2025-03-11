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
    form=ProjectForm()

    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context={
        'form':form
    }
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)
      #request is the object that carries the url information like form post data and files uploads
      #request.FILES->to deal with file uploads by user
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context={
        'form':form
    }
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request,'projects/delete_template.html',context)  
