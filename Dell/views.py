import email
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail

from Dell.models import Login, registrationForm
#from django.contrib.auth import Login, authenticate

from . import forms
from django.contrib.auth.forms import AuthenticationForm
# Create your views here
from django.http import HttpResponse

def home(request):
    return render(request,"authentication/index.html")
def signup(request):
    return render(request,)


def signout(request):
        if request.session.get('remember_me', False):
            # if the session is set, don't delete it
         request.session['remember_me'] = True
         messages.alert("Logout Successfully")
        else:
        # if the session is not set, delete it
          del request.session['remember_me']
    # log the user out
        logout(request)
        return redirect('login')
      #  messages.alert("Logout Successfully")
   # return redirect(request,'authentication/index.html')

def dashboard(request):
    return render(request,"authentication/dassboard.html")

def register(request):
    #form = forms.RegistrationForm(request.POST)
    if request.method == 'POST':
        #form = forms.RegistrationForm(request.POST)
        #if form.is_valid():
           # user = forms.save()
           # user.refresh_from_db()
            name = request.POST.get('name')
            username = request.POST.get('email')
            password = request.POST.get('password1')
            password1 = request.POST.get('password2')
            if password != password1:
                messages.error(request, "Password and Confirm Password does not match")
            else:
                #user = authenticate(First_Name = name,username = Username,Password = password1,password = password)
            #  login(request,user,backend='django.contrib.auth.backends.modelbackend')
                # login user after signing up
                user = registrationForm(password1=password1,username=username,Password=password,First_Name=name)
                user.save()
                send_mail(
                    'thanks you',
                    'Thank you for show interest in the e-commerce website',
                    'bhanups292002@gmail.com',
                    ['bhanups292004@gmail.com'],
                    fail_silently=False,
                )
                #form.save()
                if user is not None:
                    #login(request, user)
                    messages.success(request, "Registration successful.")
                   # messages.success(request, f"New account created :{username} ",)
                    return redirect('Login')
            
             #   messages.error(request, "Registration failed Try again.")
                else:
                     messages.error(request, "Registration failed Try again.")   
   # else:                
         #form = forms.RegistrationForm()
    return render(request,"signupPage.html")

def testonomial(request):
    return HttpResponse("This is a e-commerce website")
def login(request):
       # form = forms.LoginForm()
    
    if request.method == 'POST':
        #form = forms.LoginForm(request.POST)
        #if form.is_valid():
         #username = form.cleaned_data['email'],
         #password = form.cleaned_data['password1'],
        username = request.POST.get('email'),
        password = request.POST.get('password1'),
         
        user = Login(Username=username, Password1=password)    
        user = authenticate(request,username=username,password1=password)
         #password = PasswordInput
         #user.save()
        # form.save()
        if user is not None:
           login(request, user)
           request.session['remember_me'] = True
           messages.info(request, f"You are now logged in as { username }.")
           return redirect('dashboard')
            #return HttpResponse("User has succuesfully created")
        
             #messages.error(request,"Invalid username or password.")
        else:
          return HttpResponse('Invalid username of password.')
    #else:
     # form = forms.LoginForm()
    return render(request,"authentication/Login.html")