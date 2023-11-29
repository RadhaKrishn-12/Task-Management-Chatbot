from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('home/', views.Home, name= 'home'),
    path('login/', views.Login , name= 'Login'),
    path('signUp/', views.SignUp , name= 'signUp'),   
    path('logout/', views.SignOut, name='signout'),
    path('home/calender/', views.Calender, name='calender')
]