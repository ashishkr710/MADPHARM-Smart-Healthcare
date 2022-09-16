"""MADPHARM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from lib2to3.pgen2.token import NAME
from django.contrib import admin
from django.urls import path, include
from TinyCoder import views

admin.site.site_header = "MADPHARM "
admin.site.site_title = "MADPHARM PORTAL"
admin.site.index_title = "MADPHARM WELCOMES U"

urlpatterns = [
    path("Article_Login", views.Article_Login, name='Article_Login'),
    path("", views.index, name='home'),
    path("Login", views.Login, name='Login'),
    path("Signup", views.Signup, name='Signup'),
    path("Article_main", views.Article_main, name='Article_main'),
    path("appointment", views.appointment, name='appointment'),

    path("saveEnquiry", views.saveEnquiry, name='saveEnquiry'),
    path("contactEnquiry", views.contactEnquiry, name="contactEnquiry"),
    # path("Log",views.Log,name="Log"),
    # path("Sign", views.Sign, name='Sign'),
    # path("doctors",views.doctor,name='doctor')
    path("Appointment", views.Appointment, name="Appointment"),
    # path('abcd', views.abcd, name='abcd')
]
