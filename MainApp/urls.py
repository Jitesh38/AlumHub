"""
URL configuration for AlumHub project.

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
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('base', views.base, name='base'),
    path('register', views.register, name='home'),
    path('alumregister', views.alumregister, name='alumregister'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('profile/<str:slug>', views.profile, name='profile'),
    path('seminar', views.seminar, name='seminar'),
    path('alumni', views.alumniFunc, name='alumni'),
    path('search', views.search, name='alumni'),
    path('alumniexp', views.alumniExp, name='alumniexp'),
]
