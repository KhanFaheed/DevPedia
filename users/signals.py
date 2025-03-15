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




post_save.connect(createProfile,sender=User)

post_delete.connect(deleteUser,sender=Profile)





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