from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

#receiver(post_save,signal=User)
def createProfile(sender,instance,created,**kwargs):
   
    if created:  # created is true when the user is created only and not when the user is updated
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )





def deleteUser(sender,instance,**kwargs):
    #instance here is a specific profile
    user=instance.user
    user.delete()


def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user #because there is one to  one relationship from profile to user and user to profile ->we can go both the way
    
    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()



        




post_save.connect(createProfile,sender=User)


post_delete.connect(deleteUser,sender=Profile)


post_save.connect(updateUser,sender=Profile)





"""
Absolutely! Let's break down Django signals and their practical applications.

What are Django Signals?

 Django signals are a way to allow certain senders to notify a set of receivers that some action has taken place.
 This decouples different parts of your application, making it more modular and extensible.
 An event happens, a signal is sent, and different parts of your website react to that signal.

Key Concepts:

Sender: The object that sends the signal.
Signal: The type of event that occurred (e.g., a model was saved).
Receiver: A function that is executed when a signal is sent.
Connect: The process of associating a receiver with a signal.


Common Django Built-in Signals:

pre_save: Sent before a model is saved.
post_save: Sent after a model is saved.
pre_delete: Sent before a model is deleted.
post_delete: Sent after a model is deleted.
m2m_changed: Sent when a many-to-many relationship changes.
request_started: Sent when a request begins processing.
request_finished: Sent when a request finishes processing.
user_logged_in: Sent when a user logs in.
user_logged_out: Sent when a user logs out.

"""


"""
 sender
What it is: The sender parameter refers to the model class that sent the signal.

Purpose: It tells you which model triggered the signal. For example, if this signal is connected to the User model, sender will be the User class.

Example: If the signal is triggered by the User model, sender will be User.

2. instance
What it is: The instance parameter is the actual model instance that triggered the signal.

Purpose: It represents the specific object (row in the database) that was saved, deleted, or updated, depending on the signal.

Example: If a User object with id=1 is saved, instance will be that specific User object.

3. created
What it is: The created parameter is a boolean value.

Purpose: It indicates whether the signal was triggered by the creation of a new instance (True) or the update of an existing instance (False).

Example:

If a new User is created, created will be True.

If an existing User is updated, created will be False.

4. **kwargs
What it is: The **kwargs parameter is a dictionary of additional keyword arguments passed to the signal.

Purpose: It provides extra context or data related to the signal. For example, in the post_save signal, it might include raw, using, or update_fields.

Common kwargs in post_save:

raw: A boolean indicating whether the model is saved exactly as presented (e.g., during fixture loading).

using: The database alias being used.

update_fields: The set of fields that were explicitly specified to be saved.





Summary of Parameters
Parameter	Description
sender	 ->The model class that sent the signal (e.g., User).
instance ->	The specific model instance being saved (e.g., a User object).
created  ->	A boolean indicating whether the instance was created (True) or updated (False).
**kwargs ->	Additional keyword arguments provided by the signal (e.g., raw, using).

"""