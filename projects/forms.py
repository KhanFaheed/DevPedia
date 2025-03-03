from django.forms import ModelForm,widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    #It's used to provide metadata or configuration options for the form.
    #In this specific case, it's telling Django how to connect the form to a model.
    """In essence, class Meta within a ModelForm acts as a configuration block,
      providing instructions to Django about the relationship between the form and the underlying model. 
     It's how you link the form to your database structure and control which fields are displayed
     and editable in the form."""
    #meta refers to data about data
    class Meta:
        model=Project
        fields=['title','featured_image','description',
                'demo_link','source_link','tags']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
               }
        def __init__(self,*args,**kwargs):
            super(ProjectForm,self).__init__(*args,**kwargs)
            

            for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
            #self.fields['title'].widget.attrs.update({"class":"input"})
            #self.field['description'].widget.attrs.update({"class":"input"})
