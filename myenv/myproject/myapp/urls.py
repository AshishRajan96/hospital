"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from.import views


urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('departments', views.departments, name='departments'),
    path('doctors', views.doctors, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('registration', views.registration, name='registration'),
    path('doctorregistration', views.doctorregistration, name='doctorregistration'),
    path('appoinment', views.appoinment, name='appoinment'),
    path('readmore', views.readmore, name='readmore'),
    path('deptreg', views.deptreg, name='deptreg'),
    path('login', views.login, name='login'),
    path('adminmodule', views.adminmodule, name='adminmodule'),
    path('usermodule', views.usermodule, name='usermodule'),
    path('drmodule', views.drmodule, name='drmodule'),
    path('signup', views.drmodule, name='signup'),
    path('viewpatient', views.viewpatient, name='viewpatient'),
    path('adminapprove', views.adminapprove, name='adminapprove'),
    path('LoginFrm',views.LoginFrm,name='signup'),

]
