from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
     #null=true i.e that we are allowed to have this value empty in the database {null-->related to datbase}  blank=True i.e form can have this field as empty
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,
                        primary_key=True,editable=False)
    
    def __str__(self):
        return self.title
    
    


