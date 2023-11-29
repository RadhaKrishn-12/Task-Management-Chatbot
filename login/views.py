from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout

#Required to create the object in the User table of django
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.hashers import make_password
# from passlib.hash import pbkdf2_sha256
from services.calender import create_new_user_calender, g4_response
import json

from login import forms

def Home(request):
    context = {
    }
    return render(request, 'home/homePage.html', context)

def Calender(request):
    error = None
    
    if request.method == "POST":
        # print(loginForm) For debug purpose
        chat = request.POST['chat']
        request_type = request.POST['action']
        print("Chatbot request:", chat)
        print("Request type: ", request_type)
        # Calling gp4 for response to create a calender
        g4_response(request, chat, request_type)
    else:
        error = "Error in text"

    # Load user_calender.json data from services/jsons/
    print(f"Login user name: {request.user}")
    user_calender = {}
    with open(f'./services/jsons/{request.user}_calender.json', 'r') as json_file:
        user_calender = json.load(json_file)

    context = {
        "user_calender": user_calender,
        "error": error
    } 
    return render(request, 'home/calender_2.html', context)

# Create your views here.
def Login(request):
    error = None
    
    if request.method == "POST":
        # print(loginForm) For debug purpose
        user_name = request.POST['UserName']
        pasw = request.POST['Password']
        # print(user_name, make_password(pasw) )
        user = authenticate(request, username = user_name, password = pasw)
        print("Login Data: ", user)
        if user:
            ## Before opening the page it authenticate the user
            auth_login(request, user)
            return redirect('/home/calender/')
        else:
            error = "Invalid username or password"
      
    context = {
        "error": error
    } 
    # return HttpResponse('Successfully Login in AMS.')
    return render(request, 'login/login.html', context)


def SignUp(request):
    signUp = forms.SignupForm(request.POST)
    message = None
    
    if request.method == "POST":
        print("All POST Data:", request.POST, signUp.is_valid())
        print("Form Errors:", signUp.errors)

        if signUp.is_valid():
            user_name = signUp.instance.UserName
            password = request.POST.get('pass1')
            print(user_name)

            password_2 = request.POST.get('pass2')
            if password != password_2:
                message = "Passwords's didn't match."
            else:
                student = User.objects.create_user(username= user_name, password= password)
                student.save()
                messages.success(request, "Your account has been created successfully.")

                signUp.save()
                message = "Your details are saved successfully."
                # Will call the calender.py to create a calender_json file for a new user
                create_new_user_calender(user_name)
                return render(request, 'login/login.html')
        else:
            message = "Some fields are wrong. Please again fill the form as user exist with following name."

    signUp =  forms.SignupForm()        
    context = {
        "form": signUp,
        "message": message
    } 
    return render(request, 'login/Signup.html', context)



def SignOut(request):
    logout(request)
    messages.success(request, "You are successfully logout")
    return render(request, 'login/logout.html')
