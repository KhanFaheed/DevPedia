from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project,Tag,Review
def projects(request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    context={'project':projectobj}
    return render(request,'projects/single-project.html',context)

def createProject(request):
    return render(request,'projects/project_form.html')