from django.db import models
#import the built in django user model
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    Profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github=models.CharField(max_length=300,blank=True,null=True)
    social_twitter=models.CharField(max_length=300,blank=True,null=True)
    social_linkedin=models.CharField(max_length=300,blank=True,null=True)
    social_website=models.CharField(max_length=300,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,
                        primary_key=True,editable=False)
    def __str__(self):
        return str(self.username)




class Skill(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)#foreign key
    name=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,
                        primary_key=True,editable=False)
    def __str__(self):
        return self.name

    """1. Understanding the Reverse Relationship

     When you define owner = models.ForeignKey(Profile, ...) in the Skill model,
     Django creates a reverse relationship on the Profile model. 
     By default, the name of this reverse relationship is skill_set (the model name in lowercase, followed by _set).

     2. Accessing Skills from a Profile Object
     To access the skills associated with a specific Profile object,
     profile=Profile.object.filter(name='Faheed Khan')        ->profile object
     you can use profile.skill_set.all(). This will return a
     queryset containing all Skill objects that have the given Profile as their owner.
   """
