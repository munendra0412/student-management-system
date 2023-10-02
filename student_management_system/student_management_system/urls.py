"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
                path('admin/', admin.site.urls),
                path('homepage', views.BASE, name='base'),
                path('', views.LOGIN, name='login'),
                path('doLogin', views.DOLOGIN, name='doLogin'),
                path('dologout', views.DOLOGOUT, name='logout'),

                #Hod Views
                path('Hod/Home', Hod_Views.HOME, name='hod_home'),
                path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),

                #Profile Update
                path('profile', views.PROFILE, name='profile'),
                path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
