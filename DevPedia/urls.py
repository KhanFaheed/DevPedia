"""
URL configuration for DevPedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/',include('projects.urls')),
    path('',include('users.urls'))
  
]

#urls to tell django where to find the static files and mediaa files
if settings.DEBUG:  # Very important: Only in development!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns() # For static files too
    #or urlpatterns+=static(settings.STATIC,document_root=settings.MEDIA_ROOT)

#because DEBUG=False in the production environment







"""
Purpose of staticfiles_urlpatterns():
  -> This function generates the URL patterns needed to serve these
   static files directly from your Django project during development.
   It looks in the directories specified by STATICFILES_DIRS and the static directories inside your apps.
Why it's needed in development: 
   ->It makes it easy to see how your static files look on your pages while you're developing without having to set up a separate static file server.
"""


"""
Purpose of static():
  -> This function generates the URL patterns needed
     to serve these media files (user uploads) directly
     from your local file system during development.
     It uses the MEDIA_URL and MEDIA_ROOT settings you define in settings.py.
Why it's needed in development: 
   ->It lets you see the uploaded files on your pages during development.
"""


"""
The crucial difference is the type of file they serve:

staticfiles_urlpatterns(): Serves static files (CSS, JS, design images).
static(): Serves media files (user uploads).

=>They are both needed in development because Django's development server, when DEBUG is True,
 can serve both types of files directly.
 However, they are handled differently because they are stored in different locations and accessed via different URLs:

=>Static files: Are typically stored in static directories within your apps or in locations specified by STATICFILES_DIRS.
 They are accessed using the STATIC_URL prefix (e.g., /static/).

=>Media files: Are stored in the directory specified by MEDIA_ROOT 
(usually a media directory outside of your apps). They are accessed using the MEDIA_URL prefix (e.g., /media/).

"""


"""
IMPORTANT NOTES:
In Production:

=>You will not use either of these functions in your urls.py in production.

=>You will configure your web server (Nginx, Apache, or WhiteNoise)
 to serve both static and media files directly. This is much more efficient and secure. 
 You'll use collectstatic to gather all your static files into one place (STATIC_ROOT)
 and then configure your web server to serve from there.
 You'll also configure your web server to serve media files from MEDIA_ROOT.

"""
